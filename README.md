<p align="center"><img src="assets/banner.svg" alt="Menyoo Language Packs — 16 languages, 100% coverage" width="100%"></p>

<div align="center">

# 🌍 Menyoo Language Packs

**16 languages · 50 624 translated strings · 100 % UI coverage**

[![Languages](https://img.shields.io/badge/languages-16-2ea44f)](#-coverage)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](#-coverage)
[![Strings](https://img.shields.io/badge/strings-3164%20per%20pack-blue)](#-coverage)
[![License](https://img.shields.io/badge/license-MIT-important)](LICENSE)
[![GTA V](https://img.shields.io/badge/GTA%20V-Enhanced%20%26%20Legacy-orange)](#-installation)
[![validate](https://github.com/MenyooLanguages/MenyooLanguages/actions/workflows/validate.yml/badge.svg)](https://github.com/MenyooLanguages/MenyooLanguages/actions/workflows/validate.yml)
[![stars](https://img.shields.io/github/stars/MenyooLanguages/MenyooLanguages?color=e3b341)](https://github.com/MenyooLanguages/MenyooLanguages/stargazers)

Translations for the [Menyoo](https://github.com/itsjustcurtis/MenyooSP) trainer — every English label Menyoo draws, in your language.

**English** · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Polski](README.pl.md) · [Українська](README.uk.md) · [Čeština](README.cs.md) · [Nederlands](README.nl.md) · [Türkçe](README.tr.md) · [日本語](README.ja.md) · [简体中文](README.zh.md) · [繁體中文](README.zh-TW.md) · [한국어](README.ko.md)

</div>

---

## 🚀 Installation

```text
1. copy  Language/*.json      ->  <GTA V folder>/menyooStuff/Language/
2. in game:  Settings → Language → <your language>
3. in game:  Settings → Reload Language Files        (or just restart the game)
```

### One click (Windows)

Download the ZIP (**Code → Download ZIP**), keep `install.bat` next to `Language/`, run it and drag your GTA V folder onto the window — it copies every pack into `menyooStuff/Language/` and backs up whatever it overwrites.

Optional — pin the language in `menyooStuff/menyooConfig.ini`:

```ini
language = Russia
```

> Menyoo scans every `*.json` in that folder, so **one file = one new language**. Packs are plain UTF-8, no BOM (the parser rejects BOM).

---

## 📦 Coverage

Reference set: **3164 keys** — every English label Menyoo 2.4.4 renders, plus the language names shown in `Settings → Language`.

| | Pack | Language | Keys | Coverage |
|:--|:--|:--|--:|--:|
| 🇷🇺 | `Russia.json` | Русский | 3164 | ![](https://img.shields.io/badge/-100%25-brightgreen) |
| 🇬🇧 | `English.json` | English (diff reference) | 3164 | ![](https://img.shields.io/badge/-100%25-brightgreen) |
| 🇫🇷 | `French.json` | Français | 3164 | ![](https://img.shields.io/badge/-100%25-brightgreen) |
| 🇩🇪 | `German.json` | Deutsch | 3164 | ![](https://img.shields.io/badge/-100%25-brightgreen) |
| 🇪🇸 | `Spanish.json` | Español | 3164 | ![](https://img.shields.io/badge/-100%25-brightgreen) |
| 🇮🇹 | `Italian.json` | Italiano | 3164 | ![](https://img.shields.io/badge/-100%25-brightgreen) |
| 🇧🇷 | `Portuguese.json` | Português (BR) | 3164 | ![](https://img.shields.io/badge/-100%25-brightgreen) |
| 🇵🇱 | `Polish.json` | Polski | 3164 | ![](https://img.shields.io/badge/-100%25-brightgreen) |
| 🇺🇦 | `Ukrainian.json` | Українська | 3164 | ![](https://img.shields.io/badge/-100%25-brightgreen) |
| 🇨🇿 | `Czech.json` | Čeština | 3164 | ![](https://img.shields.io/badge/-100%25-brightgreen) |
| 🇳🇱 | `Dutch.json` | Nederlands | 3164 | ![](https://img.shields.io/badge/-100%25-brightgreen) |
| 🇹🇷 | `Turkish.json` | Türkçe | 3164 | ![](https://img.shields.io/badge/-100%25-brightgreen) |
| 🇯🇵 | `Japanese.json` | 日本語 | 3164 | ![](https://img.shields.io/badge/-100%25-brightgreen) |
| 🇨🇳 | `Chinese.json` | 简体中文 | 3164 | ![](https://img.shields.io/badge/-100%25-brightgreen) |
| 🇹🇼 | `ChineseTraditional.json` | 繁體中文 | 3164 | ![](https://img.shields.io/badge/-100%25-brightgreen) |
| 🇰🇷 | `Korean.json` | 한국어 | 3164 | ![](https://img.shields.io/badge/-100%25-brightgreen) |

**50 624 strings total.** `python tools/validate.py --strict` is green for all packs.

Large but never translated on purpose: vehicle / ped / prop **model names**, **FX effect ids** (`Scr Sol1 Plane Wreck`), animation, cutscene and script lists. Those are asset identifiers, not UI text.

---

## 🧰 Tools

| Script | What it does |
|:--|:--|
| `tools/translate.py` | Fills any pack up to 100 % with a chosen engine. Never overwrites existing translations, so hand edits survive forever. Caches progress in `tools/.cache/`. |
| `tools/validate.py` | Strict checker: JSON, BOM, unknown keys, empty values, lost `~b~ ~s~ ~r~` markers, lost `%s`/`%d` placeholders, stripped edge spaces. `--strict` exits 1 on any gap. |
| `tools/fix_edge_spaces.py` | Restores leading/trailing spaces (`"Entry ID: " + value` must not become `"ID:12"`). |

```bash
python tools/validate.py              # coverage table for all packs
python tools/validate.py German       # one pack
python tools/validate.py --strict     # CI mode
python tools/fix_edge_spaces.py       # repair edge spaces after MT
```

---

## ⚙️ Translation engines

DeepL is **not required** — it blocks Belarus, so the pipeline never depends on it.

| Engine | Key | Works from | Notes |
|:--|:--|:--|:--|
| `google` *(default)* | — | BY, RU, EU | public `translate.googleapis.com` endpoint, batched by newline |
| `yandex` | Api-Key + folder | BY, RU, KZ | Yandex Cloud Translate, free starter grant |
| `libre` | — | anywhere | your own LibreTranslate in docker, no limits |
| `argos` | — | anywhere, **offline** | needs a release Python build (numpy fails on 3.12 *alpha*) |
| `mymemory` | — | anywhere | small free quota, good for smoke tests |
| `echo` | — | — | rebuilds the English reference pack |

```bash
# everything, no registration, no keys
python tools/translate.py --all --backend google

# one language, or a 50-string smoke test
python tools/translate.py --pack German --target DE --backend google --limit 50

# Yandex Cloud
python tools/translate.py --all --backend yandex --key <API_KEY> --folder <FOLDER_ID>

# self-hosted LibreTranslate
docker run -ti --rm -p 5000:5000 libretranslate/libretranslate
python tools/translate.py --all --backend libre --url http://localhost:5000

# fully offline
pip install argostranslate
python tools/translate.py --all --backend argos
```

Safety nets built in:

* `~b~ ~s~ ~r~ ~g~` markers and `%s %d %f` placeholders are swapped for tokens before translation and restored after;
* if a batched reply comes back with a different line count, the batch is retried string by string;
* HTTP 429 is retried with backoff.

---

## 🗂 Structure

```text
Language/                  ready packs, 3164 keys each
data/langnames.txt         language names for Settings → Language
tools/translate.py         fill a pack to 100 % (google / yandex / libre / argos / mymemory)
tools/validate.py          strict validation
tools/fix_edge_spaces.py   edge-space repair
assets/                    banner.svg + social-preview.png (1280x640)
install.bat                one-click installer for Windows
CONTRIBUTING.md            fix a string in 3 minutes
TRANSLATORS.md             credit table
tools/make_social_preview.py  re-render the social card via headless Chrome
.github/workflows/         CI: validator + edge spaces on every push
README.<lang>.md           docs in 16 languages
```

### Adding a language

```bash
1. create Language/<Name>.json        (may start as {})
2. add <Name> to data/langnames.txt
3. add "<Name>": "<code>" to PACKS in tools/translate.py   (optional)
4. python tools/translate.py --pack <Name> --target <code> --backend google
5. python tools/validate.py <Name>
```

---

## ❓ FAQ

<details>
<summary><b>Why 3164 strings and not “everything”?</b></summary>

Menyoo 2.4.4 draws exactly 3164 translatable labels; that is the whole UI. Model names, FX ids, animation and cutscene lists are asset identifiers — translating them breaks nothing but looks like noise, so they stay Latin. Padding the file with fake keys to look bigger would just be visible on GitHub.
</details>

<details>
<summary><b>Square boxes instead of letters</b></summary>

GTA V ships fonts for EN, FR, IT, DE, ES, PT, PL, RU, JA, KO, ZH. If you run the game in English while using a CJK pack, glyphs may be missing — switch the game language or use `Settings → Menu Fonts → Normalish`. Languages GTA V never localized (Arabic, Hindi, Thai, Hebrew) are intentionally absent: the game fonts can't render them, and Arabic also needs RTL shaping.
</details>

<details>
<summary><b>How good is the translation?</b></summary>

`Russia.json` is hand-written and menu-checked (the reference). The core of every other pack (top menus, player/vehicle toggles, settings, weather, prompts) is hand-written too; the remaining ~3000 strings per language come from a machine engine — structurally valid but not native-reviewed. Fixes are welcome: edit the value, `translate.py` will never touch it again.
</details>

<details>
<summary><b>Does it work on GTA V Enhanced?</b></summary>

Yes. Language packs are read by Menyoo itself, independent of the game build — Legacy and Enhanced use the same `menyooStuff/Language/` folder.
</details>

<details>
<summary><b>Can I ship my own language?</b></summary>

Yes — one JSON file. Run the validator, open a PR; CI rejects broken JSON, lost markers and stripped edge spaces.
</details>

---

## 🤝 Contribute

| | |
|:--|:--|
| **Fix your language** | Edit one value in `Language/<Pack>.json` and open a PR — 3 minutes, no code: [CONTRIBUTING.md](CONTRIBUTING.md) |
| **Get credited** | Every accepted fix lands in [TRANSLATORS.md](TRANSLATORS.md) |
| **Report a bad string** | [translation fix form](https://github.com/MenyooLanguages/MenyooLanguages/issues/new?template=translation-fix.yml) |
| **Ask for a new language** | [language request](https://github.com/MenyooLanguages/MenyooLanguages/issues/new?template=new-language.yml) |
| **Share it** | Posting the repo in your language's GTA community is worth more than any README tweak |

---

## 🏆 Credits

* **Menyoo** — MAFINS / itsjustcurtis, the mod's own licence applies.
* **Translations & tooling in this repo** — MIT, see [LICENSE](LICENSE).
* Language names in `Settings → Language` come from file names; the `<Name>` key inside each pack is written in that language (`Deutsch`, `日本語`, `한국어`).

<div align="center">

**If a pack helped you — ⭐ the repo and send a fix for your language.**

</div>
