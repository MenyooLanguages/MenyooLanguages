<div align="center">

# 🤝 Contributing

**You don't need to code to improve this repo — one line of JSON is a valid contribution.**

[English](#-fix-your-language-3-minutes) · [Русский](#-починить-свой-язык-3-минуты) · [Translators](TRANSLATORS.md)

</div>

---

## 🇬🇧 Fix your language (3 minutes)

1. Open `Language/<YourLanguage>.json`.
2. Find the line that reads badly. Every key is the English source, the value is the translation:

   ```json
   "Infinite Ammo In Clip": "Unendlich Munition im Magazin",
   ```

   → replace the value with better wording. **Never touch the key on the left.**
3. Open a PR (or an [issue](https://github.com/MenyooLanguages/MenyooLanguages/issues/new/choose) if git is not your thing — paste the old and new line, it will be applied).

### Rules that the CI enforces

| Rule | Why |
|:--|:--|
| UTF-8 **without BOM** | Menyoo's parser rejects files with a BOM |
| keep `~r~ ~b~ ~s~ ~g~` markers | they colour the text in the subtitle bar |
| keep `%s`, `%d`, `%f` placeholders | values are injected by the game |
| keep trailing spaces (`"ID: "` stays `"ID: "`) | the game concatenates text right after it |
| no empty values | an empty string renders as a blank menu row |

Local check before pushing:

```bash
python tools/validate.py <PackName>     # same checks as CI
python tools/fix_edge_spaces.py         # repairs stripped edge spaces
```

### Want a brand-new language?

```bash
1. add Language/<Name>.json            (may start as {})
2. add <Name> to data/langnames.txt
3. python tools/translate.py --pack <Name> --target <code> --backend google
4. python tools/validate.py <Name>
```

Machine output is a starting point, not a finish line — a half-native pass over the menus is already a big win.

## 🇷🇺 Починить свой язык (3 минуты)

1. Открой `Language/<СвойЯзык>.json`.
2. Найди кривую строку: слева английский оригинал (ключ), справа перевод (значение):

   ```json
   "Infinite Ammo In Clip": "Бесконечные патроны в магазине",
   ```

   → правь **только значение справа**. Ключ не трогай — по нему Menyoo ищет строку.
3. Открой PR. Если git не твой инструмент — создай [issue](https://github.com/MenyooLanguages/MenyooLanguages/issues/new/choose) и вставь строку «было / стало», я применю.

Что проверяет CI: UTF-8 без BOM, сохранённые маркеры `~r~ ~b~ ~s~ ~g~`, плейсхолдеры `%s / %d / %f`, пробелы по краям и отсутствие пустых значений.

## Beyond translation

Bug in `tools/*.py`, a broken link, a better README in your language, a screenshot of the menu in your language — all welcome. Open an issue first if the change is large.

Be decent in issues and PRs: this is a hobby project maintained by people who play the game.

---

<div align="center">

**Fix one line today → your name lands in [TRANSLATORS.md](TRANSLATORS.md).**

</div>
