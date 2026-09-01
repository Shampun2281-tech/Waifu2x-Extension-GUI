# -*- coding: utf-8 -*-
"""Build language_Russian.ts / .qm from English.ts and RU string lists."""
from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "SRC_v3.41.01-beta" / "Waifu2x-Extension-QT"
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ru_part1 import RU_0_249
from ru_part2 import RU_250_499
from ru_part3 import RU_485_625
from ts2qm import ts_to_qm


def load_sources(en_ts: Path) -> list[str]:
    tree = ET.parse(en_ts)
    sources: list[str] = []
    for ctx in tree.getroot().findall("context"):
        for node in ctx.findall("message"):
            sources.append(node.findtext("source") or "")
    return sources


def indent_xml(elem: ET.Element, level: int = 0) -> None:
    pad = "\n" + "    " * level
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = pad + "    "
        for child in elem:
            indent_xml(child, level + 1)
        if not child.tail or not child.tail.strip():
            child.tail = pad
    if level and (not elem.tail or not elem.tail.strip()):
        elem.tail = pad


def main() -> int:
    ru = list(RU_0_249) + list(RU_250_499) + list(RU_485_625)
    en_ts = SRC / "language_English.ts"
    sources = load_sources(en_ts)
    print(
        "counts:",
        len(RU_0_249),
        len(RU_250_499),
        len(RU_485_625),
        "total",
        len(ru),
        "expected",
        len(sources),
    )
    if len(ru) != len(sources):
        print("LENGTH MISMATCH")
        n = min(len(ru), len(sources))
        for i in range(n):
            if i < 3 or (i % 50 == 0):
                print(f"  [{i}] en={sources[i][:40]!r}")
        extra = abs(len(ru) - len(sources))
        print("delta", extra)
        return 1

    mapping = dict(zip(sources, ru))
    tree = ET.parse(en_ts)
    root = tree.getroot()
    root.set("language", "ru")
    missing = 0
    filled = 0
    for ctx in root.findall("context"):
        for node in ctx.findall("message"):
            source = node.findtext("source") or ""
            trans_el = node.find("translation")
            if trans_el is None:
                trans_el = ET.SubElement(node, "translation")
            text = mapping.get(source)
            if text is None:
                missing += 1
                trans_el.set("type", "unfinished")
                trans_el.text = ""
                continue
            if "type" in trans_el.attrib:
                del trans_el.attrib["type"]
            trans_el.text = text
            filled += 1

    indent_xml(root)
    out_ts = SRC / "language_Russian.ts"
    xml_body = ET.tostring(root, encoding="unicode")
    out_ts.write_text(
        '<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE TS>\n' + xml_body + "\n",
        encoding="utf-8",
    )
    print("filled", filled, "missing", missing, "->", out_ts)

    out_qm = SRC / "language_Russian.qm"
    count = ts_to_qm(out_ts, out_qm)
    print("qm messages", count, "size", out_qm.stat().st_size, "->", out_qm)
    return 0 if missing == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
