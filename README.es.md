<p align="center"><img src="assets/banner.svg" alt="Menyoo Language Packs — 16 languages, 100% coverage" width="100%"></p>

<div align="center">

# 🌍 Menyoo Language Packs — Español

**Traducción al español de la interfaz de Menyoo — 3164 cadenas, 100 % de cobertura.**

[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](#-pack) [![Strings](https://img.shields.io/badge/strings-3164-blue)](#-pack) [![License](https://img.shields.io/badge/license-MIT-important)](LICENSE) [![GTA V](https://img.shields.io/badge/GTA%20V-Enhanced%20%26%20Legacy-orange)](#-installation)

[English](README.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Polski](README.pl.md) · [Українська](README.uk.md) · [Čeština](README.cs.md) · [Nederlands](README.nl.md) · [Türkçe](README.tr.md) · [日本語](README.ja.md) · [简体中文](README.zh.md) · [繁體中文](README.zh-TW.md) · [한국어](README.ko.md)

</div>

---

## 🚀 Instalación

```text
1. Language/Spanish.json  ->  <GTA V>/menyooStuff/Language/
2. en el juego:  Settings → Language → Spanish
3. en el juego:  Settings → Reload Language Files   (o reinicia el juego)
```

Opcional en `menyooStuff/menyooConfig.ini`: `language = Spanish`

## 📦 Paquete

| Archivo | Claves | Cobertura |
|:--|--:|--:|
| `Spanish.json` | 3164 | 100 % |

Se traduce toda la interfaz (menús, interruptores de jugador y vehículo, ajustes, clima, avisos). Los nombres de modelos, los ID de efectos FX y las listas de animaciones/cutscenes se quedan en latín a propósito: son identificadores de recursos, no texto de interfaz.

## ✅ Comprobar

```bash
python tools/validate.py Spanish
python tools/translate.py --pack Spanish --target ES --backend google   # rellenar huecos
```

Documentación completa (inglés/ruso): [README.md](README.md) · [README.ru.md](README.ru.md)


## 🤝 Help your language

Fix one line in `Language/<Pack>.json` → [CONTRIBUTING.md](CONTRIBUTING.md) · credits: [TRANSLATORS.md](TRANSLATORS.md)

---
## 🏆 Créditos

Menyoo — MAFINS / itsjustcurtis · traducciones y herramientas — MIT ([LICENSE](LICENSE)).

Se aceptan mejoras: cambia el valor en el JSON y abre un PR — la CI valida estructura y marcadores.
