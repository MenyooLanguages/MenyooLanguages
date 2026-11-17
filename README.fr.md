<p align="center"><img src="assets/banner.svg" alt="Menyoo Language Packs — 16 languages, 100% coverage" width="100%"></p>

<div align="center">

# 🌍 Menyoo Language Packs — Français

**Traduction française de l'interface Menyoo — 3164 chaînes, 100 % de couverture.**

[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](#-pack) [![Strings](https://img.shields.io/badge/strings-3164-blue)](#-pack) [![License](https://img.shields.io/badge/license-MIT-important)](LICENSE) [![GTA V](https://img.shields.io/badge/GTA%20V-Enhanced%20%26%20Legacy-orange)](#-installation)

[English](README.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Polski](README.pl.md) · [Українська](README.uk.md) · [Čeština](README.cs.md) · [Nederlands](README.nl.md) · [Türkçe](README.tr.md) · [日本語](README.ja.md) · [简体中文](README.zh.md) · [繁體中文](README.zh-TW.md) · [한국어](README.ko.md)

</div>

---

## 🚀 Installation

```text
1. Language/French.json  ->  <GTA V>/menyooStuff/Language/
2. en jeu :  Settings → Language → French
3. en jeu :  Settings → Reload Language Files   (ou relance le jeu)
```

Facultatif dans `menyooStuff/menyooConfig.ini` : `language = French`

## 📦 Paquet

| Fichier | Clés | Couverture |
|:--|--:|--:|
| `French.json` | 3164 | 100 % |

Toute l'interface est traduite (menus, bascules joueur/véhicule, réglages, météo, messages). Les noms de modèles, les ID d'effets FX et les listes d'animations/cutscenes restent en latin volontairement : ce sont des identifiants d'assets.

## ✅ Vérifier

```bash
python tools/validate.py French
python tools/translate.py --pack French --target FR --backend google   # combler les trous
```

Documentation complète (anglais/russe) : [README.md](README.md) · [README.ru.md](README.ru.md)

## 🏆 Crédits

Menyoo — MAFINS / itsjustcurtis · traductions et outils — MIT ([LICENSE](LICENSE)).

Les corrections sont bienvenues : modifie la valeur dans le JSON et ouvre une PR — la CI vérifie la structure et les marqueurs.
