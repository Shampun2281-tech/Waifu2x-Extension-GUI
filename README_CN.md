<p align="center">
<img src="/.github/README/ICON.png" height="150">
</p>

<h2 align="center"> Waifu2x-Extension-GUI </h2>

<h3 align="center"> 使用机器学习放大 图片/视频/GIF 以及 视频插帧(补帧). </h3>
<h3 align="center"> 支持 AMD / Nvidia / Intel 显卡 </h3>

<p align="center">
<img src="https://img.shields.io/github/v/release/aaronfeng753/waifu2x-extension-gui?label=Latest%20stable%20release&style=flat-square&color=brightgreen">
<img src="https://img.shields.io/badge/Support-Windows%20x64-blue?logo=Windows&style=flat-square">
</p>

### [📜English README](https://github.com/AaronFeng753/Waifu2x-Extension-GUI/blob/master/README.md) | [🔗GitHub](https://github.com/AaronFeng753/Waifu2x-Extension-GUI) | [🔗Gitee 码云](https://gitee.com/aaronfeng0711/Waifu2x-Extension-GUI)

如果README内的图片无法正常加载,请[🔗点击本链接查看码云内存储的README](https://gitee.com/aaronfeng0711/Waifu2x-Extension-GUI/blob/master/README_CN.md). 码云上的内容并非与Github实时同步, 请以[🔗官方Github为准](https://github.com/AaronFeng753/Waifu2x-Extension-GUI).

# [💾下载最新稳定版本 (Windows x64)](https://github.com/AaronFeng753/Waifu2x-Extension-GUI/releases/latest)
下载最新版本的绿色版安装包, 适用于拥有`Intel/AMD/Nvidia`显卡的`Windows 64位`系统个人电脑.

下载最新版: https://github.com/AaronFeng753/Waifu2x-Extension-GUI/releases/latest

#### [📝点击查看完整更新日志](https://github.com/AaronFeng753/Waifu2x-Extension-GUI/blob/master/Change_log_CN.md)

支持的语言: English, 简体中文, 繁體中文, Русский.

[🔗点击访问位于Gitee(码云, 开源中国)的安装包下载页面](https://gitee.com/aaronfeng0711/Waifu2x-Extension-GUI/releases/latest)

# Waifu2x-Extension-GUI是什么?

### 借助深度卷积神经网络对`图片` & `GIF` & `视频`进行`超分辨率`放大(即放大与降噪) 以及 对视频进行 `插帧(即补帧)`.

### ✨主要特性:
- #### 💡简单无门槛: 解压即用. 内置 快捷预设 功能, 可帮助您一键调整各种设置. 
- #### 📺自动化处理多种媒体: 支持处理 图片 的同时,实现了自动化处理 动态GIF&APNG&WebP 和 视频.
- #### 😍全图像风格支持: 内置多种算法, 无论是 二次元动漫 还是 您日常拍摄的照片&录像 ,都可以进行清晰化处理.
- #### 🎞视频插帧(补帧): 在对视频进行超分辨率后,自动对视频进行插帧以改进视频流畅度.
- #### ⚡视频画面分析: 通过智能分析视频画面,来加快视频处理速度以及改进视频画质.
- #### ✅强大的兼容性: 内置多个引擎, 几乎与所有现代 Windows PC 兼容.
- 📊灵活的多线程设定: 在为每个引擎提供完备的设置项的同时,您也可以自由调整线程数量,充分利用PC的一切性能.
- 🚀🚀🚀多GPU支持: 内置的所有引擎均可支持多显卡,充分利用您的PC的所有性能.
- 🛠众多自定义设置: 您可以通过调整软件内的众多自定义设置实现自动化的工作流.
- 🤖智能设定: 本软件可根据您的PC硬件信息和您要处理文件的信息自动调整部分软件设定.
- 😉易于使用的图形用户界面.
- 📨持续的维护与更新.

<p align="left">
<img src="/.github/README/Powered_by_nvidia.jpg" height="70">
</p>

```
内置超分辨率算法:
Waifu2x / SRMD / RealSR / Real-ESRGAN/ Real-CUGAN / Anime4K
ACNet / RTX Super Resolution (RTX VSR / RTX Video Super Resolution)

内置超分辨率引擎:
Waifu2x-caffe / Waifu2x-converter / Waifu2x-ncnn-vulkan
SRMD-ncnn-vulkan / RealSR-ncnn-vulkan / Anime4KCPP / SRMD-CUDA
RealESRGAN-NCNN-Vulkan / Real-CUGAN-ncnn-vulkan / RTX Super Resolution

内置插帧算法:
RIFE / CAIN / DAIN / IFRNet

内置插帧引擎:
rife-ncnn-vulkan / cain-ncnn-vulkan / dain-ncnn-vulkan
IFRNet-ncnn-vulkan
```

#### ✅已经在 `AMD` RX 550, `NVIDIA` GeForce RTX 3060/4060 和 `Intel` UHD 620 上通过测试.

![mainwindow](/Screenshot/mainwindow_cn.jpg)

![Engine_Settings](/Screenshot/Engine_Settings_CN.jpg)

![VideoSettings_CN](/Screenshot/VideoSettings_CN.jpg)

![Additional_Settings](/Screenshot/Additional_Settings_CN.jpg)

# [示例👀](https://github.com/AaronFeng753/Waifu2x-Extension-GUI/tree/master/Samples/)

### [➡对比(3D写实)](https://imgsli.com/NjQ4NzY)
#### [原照片来自Unsplash,由Jonatan Pie拍摄.](https://unsplash.com/photos/Yv9WbjBgZXY)
![Comparison](/Samples/image/Comparison_3D_Real-life.png)

### [➡对比(2D动漫)](https://imgsli.com/MjUyNDAx)
![Comparison](/Samples/image/Comparison.jpg)

#### 原图 2D动漫图片 480x300:
![Original Imgae](/Samples/image/Original_[480x300].jpg)

#### 经过4x放大&降噪,以及JPG压缩后 1920x1200: [🔗对比](https://imgsli.com/MjUyNDA0)
![Scaled Imgae](/Samples/image/Waifu2x_4x_[1920x1200].jpg)

#### 原图 GIF 500 x 372:
![Original GIF](/Samples/gif/GIF_2_original.gif)

#### 经过2x放大&降噪,以及gif优化后 1000 x 744:
![Original GIF](/Samples/gif/GIF_2_waifu2x.gif)

### `github不支持在线播放视频, 请点击下方链接查看视频示例:`

### **`视频`** : https://github.com/AaronFeng753/Waifu2x-Extension-GUI/tree/master/Samples/video

# ❤ 捐赠 ❤ (推荐使用 支付宝 或者 微信)

<p align="left">
<a href="https://www.patreon.com/aaronfeng"><img src="https://github.com/AaronFeng753/Waifu2x-Extension-GUI/blob/master/.github/BecomePatron.jpg?raw=true" alt="Patreon donate button" height="35"/> </a>
</p>

# [PayPal](https://www.paypal.me/aaronfeng753)

# [爱发电(众筹)](https://afdian.net/@AaronFeng)

![donate_new](/donate_new.jpg)

#### 如果捐赠二维码图片无法正常加载,请[打开此链接查看](https://gitee.com/aaronfeng0711/Waifu2x-Extension-GUI/raw/master/donate_new.jpg).

# [📄许可协议](https://github.com/AaronFeng753/Waifu2x-Extension-GUI/blob/master/LICENSE)

#### Waifu2x-Extension-GUI仅许可个人免费使用.

#### 如果您想获得Waifu2x-Extension-GUI的商业使用许可, 请在Patreon获取Premium版本:
#### https://www.patreon.com/aaronfeng

# 隐私政策🙈🙉🙊

我们尊重您的隐私,所以本软件的隐私政策如下:
```
1. 本软件不会向互联网上传任何数据, 所以我们不会收集您的任何信息, 我们甚至没有服务器.

2. 本软件仅在检查更新与更新捐赠页的二维码时会连接互联网, 此时将从Github和码云下载两个.ini文件和两个.jpg文件.
(码云是一个类似Github的网站, 由中华人民共和国政府监管, 您可以在附加设置内启用[禁止连接码云]以禁止本软件从码云下载数据.)

总之, 我们不会收集您的任何信息.
```

# 💝鸣谢💝:
- ❤捐赠者们❤
- 感谢 [@CAFUCSteven](https://github.com/CAFUCSteven) 长期以来帮助我测试软件，并反馈了许多Bug与建议.
- 感谢 [@MrZihan](https://github.com/MrZihan) 编写 [SRMD-CUDA](https://github.com/MrZihan/Super-resolution-SR-CUDA) 引擎并帮助我将其集成到Waifu2x-Extension-GUI中.
- Anime4K: https://github.com/bloc97/Anime4K
- Anime4KCPP: https://github.com/TianZerL/Anime4KCPP
- APNG Assembler: https://sourceforge.net/projects/apngasm/
- APNG Disassembler: https://sourceforge.net/projects/apngdis/
- APNG Optimizer: https://sourceforge.net/projects/apng/files/APNG_Optimizer/
- Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/
- cain-ncnn-vulkan: https://github.com/nihui/cain-ncnn-vulkan
- Channel Attention Is All You Need for Video Frame Interpolation: https://github.com/myungsub/CAIN
- DAIN ncnn Vulkan: https://github.com/nihui/dain-ncnn-vulkan
- DAIN (Depth-Aware Video Frame Interpolation): https://github.com/baowenbo/DAIN
- FFmpeg: https://ffmpeg.org/
- FFmpeg Builds - gyan.dev: https://www.gyan.dev/ffmpeg/builds/
- FFmpeg Builds - Zeranoe(该网站已停止运营): https://ffmpeg.zeranoe.com/builds/
- Gifsicle: https://www.lcdf.org/gifsicle/
- GIMP: https://www.gimp.org/
- GNU Wget: https://www.gnu.org/software/wget/
- IFRNet: https://github.com/ltkong218/IFRNet
- ifrnet-ncnn-vulkan: https://github.com/nihui/ifrnet-ncnn-vulkan
- ImageMagick: http://www.imagemagick.org/
- ImDisk Toolkit: https://sourceforge.net/projects/imdisk-toolkit/
- NCNN: https://github.com/Tencent/ncnn
- NirCmd: https://www.nirsoft.net/utils/nircmd.html
- NSIS: https://nsis.sourceforge.io/
- Nvidia: https://www.nvidia.com/
- OpenCV: https://opencv.org/
- Pillow: https://python-pillow.org/
- PyInstaller: https://github.com/pyinstaller/pyinstaller
- Python: https://www.python.org/
- QT: https://www.qt.io/
- Real-CUGAN: https://github.com/bilibili/ailab
- realcugan-ncnn-vulkan: https://github.com/nihui/realcugan-ncnn-vulkan
- Real-ESRGAN: https://github.com/xinntao/Real-ESRGAN
- RealSR-ncnn-vulkan: https://github.com/nihui/realsr-ncnn-vulkan
- Real-World Super-Resolution: https://github.com/jixiaozhong/RealSR
- rife-ncnn-vulkan: https://github.com/nihui/rife-ncnn-vulkan
- RIFE Video Frame Interpolation: https://github.com/hzwer/arXiv2020-RIFE
- SoX: http://sox.sourceforge.net/
- SRMD: https://github.com/cszn/SRMD
- SRMD-ncnn-Vulkan: https://github.com/nihui/srmd-ncnn-vulkan
- Super-resolution-SR-CUDA: https://github.com/MrZihan/Super-resolution-SR-CUDA
- Waifu2x: https://github.com/nagadomi/waifu2x
- Waifu2x-caffe: https://github.com/lltcggie/waifu2x-caffe
- Waifu2x-converter: https://github.com/DeadSix27/waifu2x-converter-cpp
- Waifu2x-Extension: https://github.com/AaronFeng753/Waifu2x-Extension
- Waifu2x-ncnn-vulkan: https://github.com/nihui/waifu2x-ncnn-vulkan
- [psd2waifu2x配布・サポートページ | 投稿者: HIMAKIKUROGANE](https://gkalumnium.com/devlog/psd2waifu2x%e9%85%8d%e5%b8%83%e3%83%bb%e3%82%b5%e3%83%9d%e3%83%bc%e3%83%88%e3%83%9a%e3%83%bc%e3%82%b8/)
- 图标作者: [Freepik](https://www.flaticon.com/authors/freepik) & [Roundicons](https://www.flaticon.com/authors/roundicons) & [Icongeek26](https://www.flaticon.com/authors/Icongeek26) 来自 Flaticon : https://www.flaticon.com/
- [psd2waifu2x配布・サポートページ | 投稿者: HIMAKIKUROGANE](https://gkalumnium.com/devlog/psd2waifu2x%e9%85%8d%e5%b8%83%e3%83%bb%e3%82%b5%e3%83%9d%e3%83%bc%e3%83%88%e3%83%9a%e3%83%bc%e3%82%b8/)
- 感謝 [@uimee](https://github.com/AaronFeng753/Waifu2x-Extension-GUI/issues/85) 協助進行繁體中文翻譯.
- 感谢 [@Nova-Aurora](https://github.com/Nova-Aurora) 协助修复英文版README中的语法和拼写错误.
- 感谢 [@Michael18751](https://github.com/AaronFeng753/Waifu2x-Extension-GUI/issues/118) 为提示音添加了淡出效果.
- 感谢 [@CaptainStabs](https://github.com/CaptainStabs) 协助修复多个英语语法错误.
