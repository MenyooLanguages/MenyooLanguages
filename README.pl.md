<p align="center"><img src="assets/banner.svg" alt="Menyoo Language Packs — 16 languages, 100% coverage" width="100%"></p>

<div align="center">

# 🌍 Menyoo Language Packs — Polski

**Polskie tłumaczenie interfejsu Menyoo — 3164 ciągi, 100 % pokrycia.**

[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](#-pack) [![Strings](https://img.shields.io/badge/strings-3164-blue)](#-pack) [![License](https://img.shields.io/badge/license-MIT-important)](LICENSE) [![GTA V](https://img.shields.io/badge/GTA%20V-Enhanced%20%26%20Legacy-orange)](#-installation)

[English](README.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Polski](README.pl.md) · [Українська](README.uk.md) · [Čeština](README.cs.md) · [Nederlands](README.nl.md) · [Türkçe](README.tr.md) · [日本語](README.ja.md) · [简体中文](README.zh.md) · [繁體中文](README.zh-TW.md) · [한국어](README.ko.md)

</div>

---

## 🚀 Instalacja

```text
1. Language/Polish.json  ->  <GTA V>/menyooStuff/Language/
2. w grze:  Settings → Language → Polish
3. w grze:  Settings → Reload Language Files   (albo uruchom grę ponownie)
```

Opcjonalnie w `menyooStuff/menyooConfig.ini`: `language = Polish`

## 📦 Pakiet

| Plik | Klucze | Pokrycie |
|:--|--:|--:|
| `Polish.json` | 3164 | 100 % |

Przetłumaczony jest cały interfejs (menu, przełączniki gracza i pojazdu, ustawienia, pogoda, komunikaty). Nazwy modeli, ID efektów FX oraz listy animacji i cutscenek celowo zostają po łacinie — to identyfikatory zasobów, a nie tekst UI.

## ✅ Sprawdzenie

```bash
python tools/validate.py Polish
python tools/translate.py --pack Polish --target PL --backend google   # uzupełnianie braków
```

Pełna dokumentacja (angielski/rosyjski): [README.md](README.md) · [README.ru.md](README.ru.md)


## 🤝 Help your language

Fix one line in `Language/<Pack>.json` → [CONTRIBUTING.md](CONTRIBUTING.md) · credits: [TRANSLATORS.md](TRANSLATORS.md)

---
## 🏆 Autorzy

Menyoo — MAFINS / itsjustcurtis · tłumaczenia i narzędzia — MIT ([LICENSE](LICENSE)).

Poprawki mile widziane: zmień wartość w JSON-ie i otwórz PR — CI sprawdza strukturę i znaczniki.
