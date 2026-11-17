<p align="center"><img src="assets/banner.svg" alt="Menyoo Language Packs — 16 languages, 100% coverage" width="100%"></p>

<div align="center">

# 🌍 Menyoo Language Packs — Türkçe

**Menyoo arayüzünün Türkçe çevirisi — 3164 dize, %100 kapsam.**

[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](#-pack) [![Strings](https://img.shields.io/badge/strings-3164-blue)](#-pack) [![License](https://img.shields.io/badge/license-MIT-important)](LICENSE) [![GTA V](https://img.shields.io/badge/GTA%20V-Enhanced%20%26%20Legacy-orange)](#-installation)

[English](README.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Polski](README.pl.md) · [Українська](README.uk.md) · [Čeština](README.cs.md) · [Nederlands](README.nl.md) · [Türkçe](README.tr.md) · [日本語](README.ja.md) · [简体中文](README.zh.md) · [繁體中文](README.zh-TW.md) · [한국어](README.ko.md)

</div>

---

## 🚀 Kurulum

```text
1. Language/Turkish.json  ->  <GTA V>/menyooStuff/Language/
2. oyunda:  Settings → Language → Turkish
3. oyunda:  Settings → Reload Language Files   (veya oyunu yeniden başlat)
```

İsteğe bağlı olarak `menyooStuff/menyooConfig.ini` içinde: `language = Turkish`

## 📦 Paket

| Dosya | Anahtar | Kapsam |
|:--|--:|--:|
| `Turkish.json` | 3164 | %100 |

Arayüzün tamamı çevrildi (menüler, oyuncu/araç anahtarları, ayarlar, hava durumu, bildirimler). Model adları, FX efekt kimlikleri ve animasyon/cutscene listeleri bilinçli olarak Latin kalıyor: bunlar varlık kimlikleri, arayüz metni değil.

## ✅ Doğrulama

```bash
python tools/validate.py Turkish
python tools/translate.py --pack Turkish --target TR --backend google   # eksikleri doldur
```

Tam dokümantasyon (İngilizce/Rusça): [README.md](README.md) · [README.ru.md](README.ru.md)


## 🤝 Help your language

Fix one line in `Language/<Pack>.json` → [CONTRIBUTING.md](CONTRIBUTING.md) · credits: [TRANSLATORS.md](TRANSLATORS.md)

---
## 🏆 Emeği geçenler

Menyoo — MAFINS / itsjustcurtis · çeviriler ve araçlar — MIT ([LICENSE](LICENSE)).

Düzeltmeler memnuniyetle karşılanır: JSON'daki değeri değiştir ve PR aç — CI yapıyı ve işaretleyicileri doğrular.
