# -*- coding: utf-8 -*-
"""Minimal Qt Linguist .ts -> .qm compiler (Qt 5 QM format, SaveStripped)."""
from __future__ import annotations

import struct
import xml.etree.ElementTree as ET
from pathlib import Path

MAGIC = bytes(
    [0x3C, 0xB8, 0x64, 0x18, 0xCA, 0xEF, 0x9C, 0x95, 0xCD, 0x21, 0x1C, 0xBF, 0x60, 0xA1, 0xBD, 0xDD]
)

TAG_END = 1
TAG_TRANSLATION = 3
TAG_SOURCE_TEXT = 6
TAG_CONTEXT = 7
TAG_COMMENT = 8

SECTION_CONTEXTS = 0x2F
SECTION_HASHES = 0x42
SECTION_MESSAGES = 0x69
SECTION_LANGUAGE = 0xA7

PREFIX_HASH = 1
PREFIX_HASH_CONTEXT = 2
PREFIX_HASH_CONTEXT_SOURCE = 3
PREFIX_HASH_CONTEXT_SOURCE_COMMENT = 4


def elf_hash(data: bytes) -> int:
    h = 0
    for b in data:
        h = (h << 4) + b
        g = h & 0xF0000000
        if g:
            h ^= g >> 24
            h &= ~g
        h &= 0xFFFFFFFF
    return h or 1


def pack_u8(value: int) -> bytes:
    return struct.pack(">B", value)


def pack_u16(value: int) -> bytes:
    return struct.pack(">H", value)


def pack_u32(value: int) -> bytes:
    return struct.pack(">I", value)


def q_bytearray(data: bytes) -> bytes:
    return pack_u32(len(data)) + data


def q_string(text: str) -> bytes:
    encoded = text.encode("utf-16-be")
    return pack_u32(len(encoded)) + encoded


class Message:
    __slots__ = ("context", "source", "comment", "translation")

    def __init__(self, context: str, source: str, comment: str, translation: str) -> None:
        self.context = context.encode("utf-8")
        self.source = source.encode("utf-8")
        self.comment = comment.encode("utf-8")
        self.translation = translation

    def sort_key(self) -> tuple:
        return (self.context, self.source, self.comment)


def msg_hash(msg: Message) -> int:
    return elf_hash(msg.source + msg.comment)


def common_prefix(a: Message, b: Message) -> int:
    if msg_hash(a) != msg_hash(b):
        return 0
    if a.context != b.context:
        return PREFIX_HASH
    if a.source != b.source:
        return PREFIX_HASH_CONTEXT
    if a.comment != b.comment:
        return PREFIX_HASH_CONTEXT_SOURCE
    return PREFIX_HASH_CONTEXT_SOURCE_COMMENT


def write_message(msg: Message, prefix: int) -> bytes:
    out = bytearray()
    out += pack_u8(TAG_TRANSLATION) + q_string(msg.translation)
    if prefix <= PREFIX_HASH or prefix >= PREFIX_HASH_CONTEXT_SOURCE_COMMENT:
        out += pack_u8(TAG_COMMENT) + q_bytearray(msg.comment)
        out += pack_u8(TAG_SOURCE_TEXT) + q_bytearray(msg.source)
        out += pack_u8(TAG_CONTEXT) + q_bytearray(msg.context)
    elif prefix == PREFIX_HASH_CONTEXT_SOURCE:
        out += pack_u8(TAG_SOURCE_TEXT) + q_bytearray(msg.source)
        out += pack_u8(TAG_CONTEXT) + q_bytearray(msg.context)
    elif prefix == PREFIX_HASH_CONTEXT:
        out += pack_u8(TAG_CONTEXT) + q_bytearray(msg.context)
    else:
        out += pack_u8(TAG_COMMENT) + q_bytearray(msg.comment)
        out += pack_u8(TAG_SOURCE_TEXT) + q_bytearray(msg.source)
        out += pack_u8(TAG_CONTEXT) + q_bytearray(msg.context)
    out += pack_u8(TAG_END)
    return bytes(out)


def build_context_array(contexts: list[bytes]) -> bytes:
    unique = sorted(set(contexts))
    count = len(unique)
    if count < 200:
        h_table_size = 151 if count < 60 else 503
    elif count < 2500:
        h_table_size = 1511 if count < 750 else 5003
    else:
        h_table_size = 15013 if count < 10000 else 3 * count // 2

    buckets: dict[int, list[bytes]] = {}
    for ctx in unique:
        buckets.setdefault(elf_hash(ctx) % h_table_size, []).append(ctx)

    h_table = [0] * h_table_size
    pool = bytearray(pack_u16(0))
    upto = 2

    for index in range(h_table_size):
        entries = buckets.get(index)
        if not entries:
            continue
        h_table[index] = upto >> 1
        for ctx in entries:
            raw = ctx[:255]
            pool += pack_u8(len(raw)) + raw
            upto += 1 + len(raw)
        if upto & 1:
            pool += pack_u8(0)
            upto += 1

    header = pack_u16(h_table_size) + b"".join(pack_u16(v) for v in h_table)
    return header + bytes(pool)


def parse_ts(path: Path) -> tuple[str, list[Message]]:
    tree = ET.parse(path)
    root = tree.getroot()
    language = root.get("language") or "ru"
    messages: list[Message] = []
    for ctx in root.findall("context"):
        ctx_name = ctx.findtext("name") or ""
        for node in ctx.findall("message"):
            if node.get("numerus") == "yes":
                continue
            source = node.findtext("source") or ""
            trans_el = node.find("translation")
            if trans_el is None:
                continue
            if trans_el.get("type") in {"unfinished", "vanished", "obsolete"}:
                text = (trans_el.text or "").strip()
                if not text:
                    continue
            translation = trans_el.text or ""
            if translation == "":
                continue
            comment = node.findtext("comment") or ""
            messages.append(Message(ctx_name, source, comment, translation))
    return language, messages


def compile_qm(messages: list[Message], language: str) -> bytes:
    messages = sorted(messages, key=lambda m: m.sort_key())
    message_array = bytearray()
    offsets: list[tuple[int, int]] = []
    cp_next = 0
    for i, msg in enumerate(messages):
        cp_prev = cp_next
        if i + 1 < len(messages):
            cp_next = common_prefix(msg, messages[i + 1])
        else:
            cp_next = 0
        prefix = max(cp_prev, cp_next + 1)
        offsets.append((msg_hash(msg), len(message_array)))
        message_array += write_message(msg, prefix)

    offsets.sort()
    offset_array = b"".join(pack_u32(h) + pack_u32(o) for h, o in offsets)
    context_array = build_context_array([m.context for m in messages])

    out = bytearray(MAGIC)
    lang = language.encode("utf-8")
    out += pack_u8(SECTION_LANGUAGE) + pack_u32(len(lang)) + lang
    out += pack_u8(SECTION_HASHES) + pack_u32(len(offset_array)) + offset_array
    out += pack_u8(SECTION_MESSAGES) + pack_u32(len(message_array)) + message_array
    out += pack_u8(SECTION_CONTEXTS) + pack_u32(len(context_array)) + context_array
    return bytes(out)


def ts_to_qm(ts_path: Path, qm_path: Path) -> int:
    language, messages = parse_ts(ts_path)
    qm_path.write_bytes(compile_qm(messages, language))
    return len(messages)


if __name__ == "__main__":
    import sys

    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    count = ts_to_qm(src, dst)
    print(f"Wrote {dst} ({count} messages)")
