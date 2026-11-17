<p align="center"><img src="assets/banner.svg" alt="Menyoo Language Packs — 16 languages, 100% coverage" width="100%"></p>

<div align="center">

# 🌍 Menyoo Language Packs — 繁體中文

**Menyoo 介面繁體中文翻譯 — 3164 條字串，覆蓋率 100%。**

[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](#-pack) [![Strings](https://img.shields.io/badge/strings-3164-blue)](#-pack) [![License](https://img.shields.io/badge/license-MIT-important)](LICENSE) [![GTA V](https://img.shields.io/badge/GTA%20V-Enhanced%20%26%20Legacy-orange)](#-installation)

[English](README.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Polski](README.pl.md) · [Українська](README.uk.md) · [Čeština](README.cs.md) · [Nederlands](README.nl.md) · [Türkçe](README.tr.md) · [日本語](README.ja.md) · [简体中文](README.zh.md) · [繁體中文](README.zh-TW.md) · [한국어](README.ko.md)

</div>

---

## 🚀 安裝

```text
1. 將 Language/ChineseTraditional.json 複製到  <GTA V>/menyooStuff/Language/
2. 遊戲內:  Settings → Language → ChineseTraditional
3. 遊戲內:  Settings → Reload Language Files   （或重新啟動遊戲）
```

可選：在 `menyooStuff/menyooConfig.ini` 中寫 `language = ChineseTraditional`

## 📦 語言包

| 檔案 | 鍵數 | 覆蓋率 |
|:--|--:|--:|
| `ChineseTraditional.json` | 3164 | 100% |

整個介面皆已翻譯（選單、玩家／載具開關、設定、天氣、提示）。模型名稱、FX 特效 ID、動作與過場動畫清單刻意保留拉丁字母——它們是資源識別碼，不是介面文字。

## ✅ 驗證

```bash
python tools/validate.py ChineseTraditional
python tools/translate.py --pack ChineseTraditional --target ZH-HANT --backend google
```

完整文件（英文／俄文）：[README.md](README.md) · [README.ru.md](README.ru.md)

## 🏆 致謝

Menyoo — MAFINS / itsjustcurtis · 本倉庫的翻譯與工具 — MIT（見 [LICENSE](LICENSE)）。

歡迎提交修正：修改 JSON 中的值並開 PR，CI 會驗證結構與標記。
