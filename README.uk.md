<p align="center"><img src="assets/banner.svg" alt="Menyoo Language Packs — 16 languages, 100% coverage" width="100%"></p>

<div align="center">

# 🌍 Menyoo Language Packs — Українська

**Український переклад інтерфейсу Menyoo — 3164 рядки, 100 % покриття.**

[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](#-pack) [![Strings](https://img.shields.io/badge/strings-3164-blue)](#-pack) [![License](https://img.shields.io/badge/license-MIT-important)](LICENSE) [![GTA V](https://img.shields.io/badge/GTA%20V-Enhanced%20%26%20Legacy-orange)](#-installation)

[English](README.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Polski](README.pl.md) · [Українська](README.uk.md) · [Čeština](README.cs.md) · [Nederlands](README.nl.md) · [Türkçe](README.tr.md) · [日本語](README.ja.md) · [简体中文](README.zh.md) · [繁體中文](README.zh-TW.md) · [한국어](README.ko.md)

</div>

---

## 🚀 Встановлення

```text
1. Language/Ukrainian.json  ->  <тека GTA V>/menyooStuff/Language/
2. у грі:  Settings → Language → Ukrainian
3. у грі:  Settings → Reload Language Files   (або перезапусти гру)
```

Можна зафіксувати мову в `menyooStuff/menyooConfig.ini`: `language = Ukrainian`

## 📦 Пакет

| Файл | Ключів | Покриття |
|:--|--:|--:|
| `Ukrainian.json` | 3164 | 100 % |

Перекладено весь інтерфейс (меню, перемикачі гравця й транспорту, налаштування, погода, повідомлення). Назви моделей, ID ефектів FX і списки анімацій та катсцен навмисно лишаються латиницею — це ідентифікатори ассетів, а не текст інтерфейсу.

## ✅ Перевірка

```bash
python tools/validate.py Ukrainian
python tools/translate.py --pack Ukrainian --target UK --backend google   # дозаповнити пропуски
```

Повна документація (англійська/російська): [README.md](README.md) · [README.ru.md](README.ru.md)


## 🤝 Help your language

Fix one line in `Language/<Pack>.json` → [CONTRIBUTING.md](CONTRIBUTING.md) · credits: [TRANSLATORS.md](TRANSLATORS.md)

---
## 🏆 Автори

Menyoo — MAFINS / itsjustcurtis · переклади й інструменти — MIT ([LICENSE](LICENSE)).

Правки вітаються: зміни значення у JSON і відкрий PR — CI перевіряє структуру та маркери.
