<p align="center"><img src="assets/banner.svg" alt="Menyoo Language Packs — 16 languages, 100% coverage" width="100%"></p>

<div align="center">

# 🌍 Menyoo Language Packs — Deutsch

**Deutsche Übersetzung der Menyoo-Oberfläche — 3164 Zeichenketten, 100 % Abdeckung.**

[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](#-pack) [![Strings](https://img.shields.io/badge/strings-3164-blue)](#-pack) [![License](https://img.shields.io/badge/license-MIT-important)](LICENSE) [![GTA V](https://img.shields.io/badge/GTA%20V-Enhanced%20%26%20Legacy-orange)](#-installation)

[English](README.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Polski](README.pl.md) · [Українська](README.uk.md) · [Čeština](README.cs.md) · [Nederlands](README.nl.md) · [Türkçe](README.tr.md) · [日本語](README.ja.md) · [简体中文](README.zh.md) · [繁體中文](README.zh-TW.md) · [한국어](README.ko.md)

</div>

---

## 🚀 Installation

```text
1. Language/German.json  ->  <GTA V>/menyooStuff/Language/
2. im Spiel:  Settings → Language → German
3. im Spiel:  Settings → Reload Language Files   (oder Spiel neu starten)
```

Optional in `menyooStuff/menyooConfig.ini`: `language = German`

## 📦 Paket

| Datei | Schlüssel | Abdeckung |
|:--|--:|--:|
| `German.json` | 3164 | 100 % |

Übersetzt wird die komplette Oberfläche (Menüs, Spieler-/Fahrzeug-Schalter, Einstellungen, Wetter, Meldungen). Modellnamen, FX-IDs, Animations- und Cutscene-Listen bleiben absichtlich lateinisch — das sind Asset-IDs, kein UI-Text.

## ✅ Prüfen

```bash
python tools/validate.py German
python tools/translate.py --pack German --target DE --backend google   # Lücken füllen
```

Volle Dokumentation (Englisch/Russisch): [README.md](README.md) · [README.ru.md](README.ru.md)

## 🏆 Credits

Menyoo — MAFINS / itsjustcurtis · Übersetzungen und Tools hier — MIT ([LICENSE](LICENSE)).

Verbesserungen willkommen: Wert in der JSON ändern, PR öffnen — CI prüft Struktur und Marker.
