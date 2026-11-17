<p align="center"><img src="assets/banner.svg" alt="Menyoo Language Packs — 16 languages, 100% coverage" width="100%"></p>

<div align="center">

# 🌍 Menyoo Language Packs — 日本語

**Menyoo の UI 日本語訳 — 3164 文字列、カバレッジ 100%。**

[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](#-pack) [![Strings](https://img.shields.io/badge/strings-3164-blue)](#-pack) [![License](https://img.shields.io/badge/license-MIT-important)](LICENSE) [![GTA V](https://img.shields.io/badge/GTA%20V-Enhanced%20%26%20Legacy-orange)](#-installation)

[English](README.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Polski](README.pl.md) · [Українська](README.uk.md) · [Čeština](README.cs.md) · [Nederlands](README.nl.md) · [Türkçe](README.tr.md) · [日本語](README.ja.md) · [简体中文](README.zh.md) · [繁體中文](README.zh-TW.md) · [한국어](README.ko.md)

</div>

---

## 🚀 インストール

```text
1. Language/Japanese.json  ->  <GTA V>/menyooStuff/Language/
2. ゲーム内:  Settings → Language → Japanese
3. ゲーム内:  Settings → Reload Language Files  （またはゲーム再起動）
```

任意: `menyooStuff/menyooConfig.ini` に `language = Japanese`

## 📦 パッケージ

| ファイル | キー数 | カバレッジ |
|:--|--:|--:|
| `Japanese.json` | 3164 | 100% |

メニュー、プレイヤー／車両のトグル、設定、天気、通知まで UI 全体を翻訳済み。モデル名、FX エフェクト ID、アニメーション／カットシーン一覧は意図的にラテン文字のままにしています（これらはアセット ID で、UI テキストではありません）。

## ✅ 検証

```bash
python tools/validate.py Japanese
python tools/translate.py --pack Japanese --target JA --backend google   # 未訳を補完
```

詳細ドキュメント（英語／ロシア語）: [README.md](README.md) · [README.ru.md](README.ru.md)

## 🏆 クレジット

Menyoo — MAFINS / itsjustcurtis · 翻訳とツール — MIT ([LICENSE](LICENSE))。

修正歓迎: JSON の値を書き換えて PR を送ってください。CI が構造とマーカーを検証します。
