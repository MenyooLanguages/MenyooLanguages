<p align="center"><img src="assets/banner.svg" alt="Menyoo Language Packs — 16 languages, 100% coverage" width="100%"></p>

<div align="center">

# 🌍 Menyoo Language Packs — Italiano

**Traduzione italiana dell'interfaccia Menyoo — 3164 stringhe, copertura 100 %.**

[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](#-pack) [![Strings](https://img.shields.io/badge/strings-3164-blue)](#-pack) [![License](https://img.shields.io/badge/license-MIT-important)](LICENSE) [![GTA V](https://img.shields.io/badge/GTA%20V-Enhanced%20%26%20Legacy-orange)](#-installation)

[English](README.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Polski](README.pl.md) · [Українська](README.uk.md) · [Čeština](README.cs.md) · [Nederlands](README.nl.md) · [Türkçe](README.tr.md) · [日本語](README.ja.md) · [简体中文](README.zh.md) · [繁體中文](README.zh-TW.md) · [한국어](README.ko.md)

</div>

---

## 🚀 Installazione

```text
1. Language/Italian.json  ->  <GTA V>/menyooStuff/Language/
2. nel gioco:  Settings → Language → Italian
3. nel gioco:  Settings → Reload Language Files   (o riavvia il gioco)
```

Opzionale in `menyooStuff/menyooConfig.ini`: `language = Italian`

## 📦 Pacchetto

| File | Chiavi | Copertura |
|:--|--:|--:|
| `Italian.json` | 3164 | 100 % |

È tradotta tutta l'interfaccia (menu, interruttori giocatore/veicolo, impostazioni, meteo, avvisi). Nomi dei modelli, ID degli effetti FX e liste di animazioni/cutscene restano in latino di proposito: sono identificatori di asset.

## ✅ Verifica

```bash
python tools/validate.py Italian
python tools/translate.py --pack Italian --target IT --backend google   # riempi i vuoti
```

Documentazione completa (inglese/russo): [README.md](README.md) · [README.ru.md](README.ru.md)


## 🤝 Help your language

Fix one line in `Language/<Pack>.json` → [CONTRIBUTING.md](CONTRIBUTING.md) · credits: [TRANSLATORS.md](TRANSLATORS.md)

---
## 🏆 Crediti

Menyoo — MAFINS / itsjustcurtis · traduzioni e strumenti — MIT ([LICENSE](LICENSE)).

Correzioni benvenute: cambia il valore nel JSON e apri una PR — la CI controlla struttura e marcatori.
