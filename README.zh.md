<p align="center"><img src="assets/banner.svg" alt="Menyoo Language Packs — 16 languages, 100% coverage" width="100%"></p>

<div align="center">

# 🌍 Menyoo Language Packs — 简体中文

**Menyoo 界面简体中文翻译 — 3164 条字符串，覆盖率 100%。**

[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](#-pack) [![Strings](https://img.shields.io/badge/strings-3164-blue)](#-pack) [![License](https://img.shields.io/badge/license-MIT-important)](LICENSE) [![GTA V](https://img.shields.io/badge/GTA%20V-Enhanced%20%26%20Legacy-orange)](#-installation)

[English](README.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Polski](README.pl.md) · [Українська](README.uk.md) · [Čeština](README.cs.md) · [Nederlands](README.nl.md) · [Türkçe](README.tr.md) · [日本語](README.ja.md) · [简体中文](README.zh.md) · [繁體中文](README.zh-TW.md) · [한국어](README.ko.md)

</div>

---

## 🚀 安装

```text
1. 把 Language/Chinese.json 复制到  <GTA V>/menyooStuff/Language/
2. 游戏内:  Settings → Language → Chinese
3. 游戏内:  Settings → Reload Language Files   （或重启游戏）
```

可选：在 `menyooStuff/menyooConfig.ini` 中写 `language = Chinese`

## 📦 语言包

| 文件 | 键数 | 覆盖率 |
|:--|--:|--:|
| `Chinese.json` | 3164 | 100% |

整个界面均已翻译（菜单、玩家/载具开关、设置、天气、提示）。模型名称、FX 特效 ID、动作与过场动画列表有意保留拉丁字母——它们是资源标识符，不是界面文本。

## ✅ 校验

```bash
python tools/validate.py Chinese
python tools/translate.py --pack Chinese --target ZH --backend google   # 补齐缺失项
```

完整文档（英文/俄文）：[README.md](README.md) · [README.ru.md](README.ru.md)

## 🏆 致谢

Menyoo — MAFINS / itsjustcurtis · 本仓库的翻译与工具 — MIT（见 [LICENSE](LICENSE)）。

欢迎提交修正：修改 JSON 中的值并开 PR，CI 会校验结构和标记。
