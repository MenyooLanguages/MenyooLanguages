<p align="center"><img src="assets/banner.svg" alt="Menyoo Language Packs — 16 languages, 100% coverage" width="100%"></p>

<div align="center">

# 🌍 Menyoo Language Packs — Português (BR)

**Tradução da interface do Menyoo — 3164 strings, 100 % de cobertura.**

[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](#-pack) [![Strings](https://img.shields.io/badge/strings-3164-blue)](#-pack) [![License](https://img.shields.io/badge/license-MIT-important)](LICENSE) [![GTA V](https://img.shields.io/badge/GTA%20V-Enhanced%20%26%20Legacy-orange)](#-installation)

[English](README.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Polski](README.pl.md) · [Українська](README.uk.md) · [Čeština](README.cs.md) · [Nederlands](README.nl.md) · [Türkçe](README.tr.md) · [日本語](README.ja.md) · [简体中文](README.zh.md) · [繁體中文](README.zh-TW.md) · [한국어](README.ko.md)

</div>

---

## 🚀 Instalação

```text
1. Language/Portuguese.json  ->  <GTA V>/menyooStuff/Language/
2. no jogo:  Settings → Language → Portuguese
3. no jogo:  Settings → Reload Language Files   (ou reinicie o jogo)
```

Opcional em `menyooStuff/menyooConfig.ini`: `language = Portuguese`

## 📦 Pacote

| Arquivo | Chaves | Cobertura |
|:--|--:|--:|
| `Portuguese.json` | 3164 | 100 % |

A interface inteira é traduzida (menus, chaves de jogador/veículo, configurações, clima, avisos). Nomes de modelos, IDs de efeitos FX e listas de animações/cutscenes ficam em latim de propósito: são identificadores de assets.

## ✅ Verificar

```bash
python tools/validate.py Portuguese
python tools/translate.py --pack Portuguese --target PT-BR --backend google   # completar lacunas
```

Documentação completa (inglês/russo): [README.md](README.md) · [README.ru.md](README.ru.md)


## 🤝 Help your language

Fix one line in `Language/<Pack>.json` → [CONTRIBUTING.md](CONTRIBUTING.md) · credits: [TRANSLATORS.md](TRANSLATORS.md)

---
## 🏆 Créditos

Menyoo — MAFINS / itsjustcurtis · traduções e ferramentas — MIT ([LICENSE](LICENSE)).

Correções são bem-vindas: altere o valor no JSON e abra um PR — o CI valida estrutura e marcadores.
