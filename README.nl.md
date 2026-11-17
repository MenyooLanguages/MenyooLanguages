<p align="center"><img src="assets/banner.svg" alt="Menyoo Language Packs — 16 languages, 100% coverage" width="100%"></p>

<div align="center">

# 🌍 Menyoo Language Packs — Nederlands

**Nederlandse vertaling van de Menyoo-interface — 3164 strings, 100 % dekking.**

[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](#-pack) [![Strings](https://img.shields.io/badge/strings-3164-blue)](#-pack) [![License](https://img.shields.io/badge/license-MIT-important)](LICENSE) [![GTA V](https://img.shields.io/badge/GTA%20V-Enhanced%20%26%20Legacy-orange)](#-installation)

[English](README.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Polski](README.pl.md) · [Українська](README.uk.md) · [Čeština](README.cs.md) · [Nederlands](README.nl.md) · [Türkçe](README.tr.md) · [日本語](README.ja.md) · [简体中文](README.zh.md) · [繁體中文](README.zh-TW.md) · [한국어](README.ko.md)

</div>

---

## 🚀 Installatie

```text
1. Language/Dutch.json  ->  <GTA V>/menyooStuff/Language/
2. in het spel:  Settings → Language → Dutch
3. in het spel:  Settings → Reload Language Files   (of herstart het spel)
```

Optioneel in `menyooStuff/menyooConfig.ini`: `language = Dutch`

## 📦 Pakket

| Bestand | Sleutels | Dekking |
|:--|--:|--:|
| `Dutch.json` | 3164 | 100 % |

De hele interface is vertaald (menu's, speler- en voertuigschakelaars, instellingen, weer, meldingen). Modelnamen, FX-effect-ID's en animatie-/cutscenelijsten blijven bewust Latijn: dat zijn asset-ID's, geen UI-tekst.

## ✅ Controleren

```bash
python tools/validate.py Dutch
python tools/translate.py --pack Dutch --target NL --backend google   # gaten vullen
```

Volledige documentatie (Engels/Russisch): [README.md](README.md) · [README.ru.md](README.ru.md)


## 🤝 Help your language

Fix one line in `Language/<Pack>.json` → [CONTRIBUTING.md](CONTRIBUTING.md) · credits: [TRANSLATORS.md](TRANSLATORS.md)

---
## 🏆 Credits

Menyoo — MAFINS / itsjustcurtis · vertalingen en tools — MIT ([LICENSE](LICENSE)).

Verbeteringen welkom: pas de waarde in de JSON aan en open een PR — CI controleert structuur en markers.
