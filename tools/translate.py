#!/usr/bin/env python3
"""
Fill a Menyoo language pack up to 100% coverage with machine translation.

The English strings are the JSON keys of Menyoo's language files, so the source
text is always the key itself. Existing hand-written translations are never
overwritten - only missing keys are translated and appended.

Backends (pick one that is reachable from your country):

  google  free public endpoint, no key, not blocked in BY/RU - batch mode
  argos   fully offline, no key, no network after the first package download
  yandex  Yandex Cloud / Yandex Translate API (works in BY/RU/KZ, free grant)
  libre   self-hosted LibreTranslate in docker (no limits, no key)
  mymemory free public API, no key, small daily quota (good for smoke tests)
  echo    identity backend, builds the English reference pack

Examples
--------
    # Google public endpoint: no key, no registration, works from Belarus
    python tools/translate.py --all --backend google

    # offline, nothing blocked (needs a release build of Python, not 3.12 alpha)
    pip install argostranslate
    python tools/translate.py --all --backend argos

    # Yandex Cloud API v2 (Api-Key + folder id)
    python tools/translate.py --all --backend yandex --key <API_KEY> --folder <FOLDER_ID>

    # Yandex legacy v1.5 key (no folder needed)
    python tools/translate.py --all --backend yandex --key <KEY> --yandex-v1

    # self-hosted LibreTranslate
    docker run -ti --rm -p 5000:5000 libretranslate/libretranslate
    python tools/translate.py --all --backend libre --url http://localhost:5000

    # quick check on 50 strings
    python tools/translate.py --pack German --target DE --backend mymemory --limit 50

Progress is cached in tools/.cache/<Pack>.json, so an interrupted run continues
where it stopped and re-runs only translate new keys.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANG_DIR = ROOT / "Language"
CACHE_DIR = Path(__file__).resolve().parent / ".cache"
REFERENCE = LANG_DIR / "Russia.json"

# pack file name -> target language code used by the engines
PACKS = {
    "French": "FR",
    "German": "DE",
    "Spanish": "ES",
    "Italian": "IT",
    "Portuguese": "PT-BR",
    "Polish": "PL",
    "Ukrainian": "UK",
    "Czech": "CS",
    "Dutch": "NL",
    "Turkish": "TR",
    "Japanese": "JA",
    "Chinese": "ZH",
    "ChineseTraditional": "ZH-HANT",
    "Korean": "KO",
}

MARKER_RE = re.compile(r"~[a-zA-Z]{1,3}~")
PLACEHOLDER_RE = re.compile(r"%(?:[sdfix]|%)")


def protect(text: str) -> tuple[str, list[str]]:
    """Replace GTA colour markers and printf placeholders with stable tokens."""
    parts: list[str] = []

    def sub(match: re.Match) -> str:
        parts.append(match.group(0))
        return f"<x{len(parts) - 1}>"

    protected = MARKER_RE.sub(sub, text)
    protected = PLACEHOLDER_RE.sub(sub, protected)
    return protected, parts


def restore(text: str, parts: list[str]) -> str:
    def sub(match: re.Match) -> str:
        idx = int(match.group(1))
        return parts[idx] if idx < len(parts) else match.group(0)

    out = re.sub(r"<x(\d+)>", sub, text)
    for idx, original in enumerate(parts):  # engines sometimes mangle the brackets
        out = out.replace(f"< X{idx} >", original).replace(f"<x {idx}>", original)
    return out


def normalise(target: str, backend: str) -> str:
    base = target.split("-")[0].lower()
    if backend == "argos":
        # argos uses "zt" for traditional Chinese, "pt" for Portuguese
        return {"zh-hant": "zt", "pt-br": "pt", "zh-hans": "zh"}.get(target.lower(), base)
    if backend in ("yandex",):
        return base
    if backend == "mymemory":
        return base
    if backend == "google":
        return {"zh": "zh-CN", "zh-hant": "zh-TW", "pt-br": "pt"}.get(target.lower(), base)
    return base


class Backend:
    name = "base"

    def translate(self, texts: list[str], target: str) -> list[str]:
        raise NotImplementedError


class Google(Backend):
    """Public translate.googleapis.com endpoint: no key, no quota page, batch-friendly."""

    name = "google"
    URL = "https://translate.googleapis.com/translate_a/single"

    def __init__(self, delay: float = 0.15) -> None:
        self.delay = delay

    @staticmethod
    def _code(target: str) -> str:
        upper = target.upper()
        if upper in ("ZH", "ZH-HANS", "ZH-CN"):
            return "zh-CN"
        if upper in ("ZH-HANT", "ZH-TW"):
            return "zh-TW"
        if upper == "PT-BR":
            return "pt"
        return target.split("-")[0].lower()

    def _request(self, texts: list[str], code: str) -> list[str]:
        joined = chr(10).join(texts)
        params = {"client": "gtx", "sl": "en", "tl": code, "dt": "t", "q": joined}
        url = self.URL + "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=90) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        text = "".join(part[0] for part in payload[0] if part[0])
        return text.split(chr(10))

    def translate(self, texts: list[str], target: str) -> list[str]:
        code = self._code(target)
        for attempt in range(1, 5):
            try:
                out = self._request(texts, code)
                if len(out) == len(texts):
                    time.sleep(self.delay)
                    return out
                break  # line count drifted: fall back to one-by-one
            except Exception as exc:  # noqa: BLE001
                if "429" in str(exc) or "Too Many" in str(exc):
                    time.sleep(5 * attempt)
                    continue
                raise
        single: list[str] = []
        for text in texts:
            single.append(self._request([text], code)[0])
            time.sleep(self.delay * 2)
        return single


class Echo(Backend):
    """Identity backend: emits an English (source) pack and smoke-tests the pipeline."""

    name = "echo"

    def translate(self, texts: list[str], target: str) -> list[str]:
        return list(texts)


class Argos(Backend):
    """Fully offline. First run downloads the ~200 MB language package once."""

    name = "argos"

    def __init__(self) -> None:
        try:
            import argostranslate.package  # noqa: F401
            import argostranslate.translate  # noqa: F401
        except ImportError:
            sys.exit("argos: сначала установи пакет —  pip install argostranslate")
        from argostranslate import package as _pkg
        from argostranslate import translate as _tr

        self._pkg = _pkg
        self._tr = _tr
        self._ready = False
        self._pairs: dict[str, object] = {}

    def _install(self, code: str) -> None:
        if not self._ready:
            print("argos: обновляю индекс пакетов...")
            self._pkg.update_package_index()
            self._ready = True
        available = self._pkg.get_available_packages()
        candidates = [p for p in available if p.from_code == "en" and p.to_code == code]
        if not candidates:
            raise RuntimeError(f"argos: нет пакета en->{code} (доступные: "
                               f"{sorted({p.to_code for p in available if p.from_code == 'en'})})")
        package = candidates[0]
        print(f"argos: скачиваю пакет en->{code} ...")
        self._pkg.install_from_path(package.download())

    def translate(self, texts: list[str], target: str) -> list[str]:
        code = normalise(target, self.name)
        if code not in self._pairs:
            installed = self._tr.get_installed_languages()
            src = next((lang for lang in installed if lang.code == "en"), None)
            dst = next((lang for lang in installed if lang.code == code), None)
            if not src or not dst:
                self._install(code)
                installed = self._tr.get_installed_languages()
                src = next((lang for lang in installed if lang.code == "en"), None)
                dst = next((lang for lang in installed if lang.code == code), None)
            if not src or not dst:
                raise RuntimeError(f"argos: пакет en->{code} не установился")
            self._pairs[code] = src.get_translation(dst)
        engine = self._pairs[code]
        return [engine.translate(t) for t in texts]


class Yandex(Backend):
    """Yandex Translate: works in BY/RU/KZ. v2 (Api-Key + folder) or legacy v1.5 key."""

    name = "yandex"

    def __init__(self, key: str, folder: str | None, legacy_v1: bool) -> None:
        if not key:
            sys.exit("yandex: нужен --key (https://cloud.yandex.ru/docs/translate/)")
        self.key = key
        self.folder = folder
        self.v1 = legacy_v1

    def translate(self, texts: list[str], target: str) -> list[str]:
        code = normalise(target, self.name)
        if self.v1:
            body = [("key", self.key), ("lang", f"en-{code}"), ("format", "plain")]
            body += [("text", t) for t in texts]
            req = urllib.request.Request(
                "https://translate.yandex.net/api/v1.5/tr.json/translate",
                data=urllib.parse.urlencode(body).encode("utf-8"),
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            return payload["text"]

        if not self.folder:
            sys.exit("yandex: для API v2 нужен --folder <FOLDER_ID> (или используй --yandex-v1)")
        body = {
            "folderId": self.folder,
            "sourceLanguageCode": "en",
            "targetLanguageCode": code,
            "format": "PLAIN_TEXT",
            "texts": texts,
        }
        req = urllib.request.Request(
            "https://translate.api.cloud.yandex.net/translate/v2/translate",
            data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
            headers={"Content-Type": "application/json", "Authorization": f"Api-Key {self.key}"},
        )
        with urllib.request.urlopen(req, timeout=120) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        return [item["text"] for item in payload["translations"]]


class LibreTranslate(Backend):
    name = "libre"

    def __init__(self, url: str, key: str | None = None) -> None:
        self.url = (url or "http://localhost:5000").rstrip("/")
        self.key = key

    def translate(self, texts: list[str], target: str) -> list[str]:
        code = normalise(target, self.name)
        out: list[str] = []
        for text in texts:
            body = {"q": text, "source": "en", "target": code, "format": "text"}
            if self.key:
                body["api_key"] = self.key
            req = urllib.request.Request(
                self.url + "/translate",
                data=json.dumps(body).encode("utf-8"),
                headers={"Content-Type": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                out.append(json.loads(resp.read().decode("utf-8"))["translatedText"])
            time.sleep(0.2)
        return out


class MyMemory(Backend):
    """Free public API, no key. ~500 bytes per request, small daily quota."""

    name = "mymemory"

    def __init__(self, email: str | None = None) -> None:
        self.email = email

    def translate(self, texts: list[str], target: str) -> list[str]:
        code = normalise(target, self.name)
        out: list[str] = []
        for text in texts:
            params = {"q": text, "langpair": f"en|{code}"}
            if self.email:
                params["de"] = self.email
            url = "https://api.mymemory.translated.net/get?" + urllib.parse.urlencode(params)
            with urllib.request.urlopen(url, timeout=120) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            out.append(payload["responseData"]["translatedText"])
            time.sleep(0.4)
        return out


def build_backend(args) -> Backend:
    if args.backend == "echo":
        return Echo()
    if args.backend == "google":
        return Google()
    if args.backend == "argos":
        return Argos()
    if args.backend == "yandex":
        return Yandex(args.key, args.folder, args.yandex_v1)
    if args.backend == "libre":
        return LibreTranslate(args.url, args.key)
    if args.backend == "mymemory":
        return MyMemory(args.email)
    raise SystemExit(f"unknown backend {args.backend}")


def load_reference() -> list[str]:
    return list(json.loads(REFERENCE.read_text(encoding="utf-8")))


def run_pack(pack: str, target: str, backend: Backend, keys: list[str], limit: int | None,
             batch_size: int) -> None:
    path = LANG_DIR / f"{pack}.json"
    existing: dict[str, str] = {}
    if path.exists():
        existing = json.loads(path.read_text(encoding="utf-8"))

    CACHE_DIR.mkdir(exist_ok=True)
    cache_path = CACHE_DIR / f"{pack}.json"
    cache: dict[str, str] = json.loads(cache_path.read_text(encoding="utf-8")) if cache_path.exists() else {}

    missing = [k for k in keys if k not in existing and k not in cache and k.strip()]
    missing += [k for k in keys if k in cache and k not in existing]

    to_translate = [k for k in keys if k not in existing and k not in cache and k.strip()]
    if limit:
        to_translate.sort(key=lambda k: -len(k))
        to_translate = to_translate[:limit]

    print(f"[{pack}/{target}] есть {len(existing)}, в кэше {len(cache)}, "
          f"перевести {len(to_translate)} (всего не хватает {len(missing)})")

    batch: list[str] = []
    payloads: list[tuple[str, list[str]]] = []

    def flush() -> None:
        if not batch:
            return
        for attempt in range(1, 4):
            try:
                translated = backend.translate(list(batch), target)
                break
            except Exception as exc:  # noqa: BLE001
                print(f"  повтор {attempt}/3: {exc}")
                time.sleep(2 * attempt)
        else:
            print("  пропускаю пачку после 3 неудач")
            batch.clear()
            payloads.clear()
            return
        for (key, parts), text in zip(payloads, translated):
            cache[key] = restore(text, parts)
        cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=0), encoding="utf-8")
        batch.clear()
        payloads.clear()

    for key in to_translate:
        protected, parts = protect(key)
        batch.append(protected)
        payloads.append((key, parts))
        if len(batch) >= batch_size:
            flush()
    flush()

    for key in keys:
        if key in existing:
            continue
        value = cache.get(key)
        if value:
            existing[key] = value

    if pack == "ChineseTraditional":
        existing.setdefault(pack, "繁體中文")

    ordered = {key: existing[key] for key in keys if key in existing}
    for key, value in existing.items():  # keep extra keys (language names etc.)
        ordered.setdefault(key, value)

    path.write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    covered = sum(1 for k in keys if k in ordered)
    print(f"[{pack}/{target}] записано {len(ordered)} ключей "
          f"({covered}/{len(keys)} = {covered / len(keys) * 100:.1f}%) -> {path.name}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Translate Menyoo packs to 100% coverage")
    parser.add_argument("--pack", help="pack file name without .json, e.g. German")
    parser.add_argument("--target", help="target language code for the engine, e.g. DE, pt, zh-Hant")
    parser.add_argument("--all", action="store_true", help="process every pack from PACKS")
    parser.add_argument("--backend", choices=("google", "argos", "yandex", "libre", "mymemory", "echo"),
                        default="google", help="translation engine (default: google, no key needed)")
    parser.add_argument("--key", help="API key (Yandex, or LibreTranslate if it needs one)")
    parser.add_argument("--folder", help="Yandex Cloud folder id (API v2 only)")
    parser.add_argument("--yandex-v1", action="store_true", help="use legacy Yandex API v1.5 key")
    parser.add_argument("--url", help="LibreTranslate base url, default http://localhost:5000")
    parser.add_argument("--email", help="e-mail for a larger MyMemory quota")
    parser.add_argument("--limit", type=int, help="translate only N missing keys (smoke test)")
    parser.add_argument("--batch", type=int, default=40, help="strings per request (default 40)")
    args = parser.parse_args()

    keys = load_reference()
    backend = build_backend(args)

    if args.all:
        for pack, target in PACKS.items():
            run_pack(pack, target, backend, keys, args.limit, args.batch)
        return 0

    if not args.pack:
        parser.error("нужен --pack NAME или --all")
    target = args.target or PACKS.get(args.pack)
    if not target:
        parser.error("для этого пакета нужен --target")
    run_pack(args.pack, target, backend, keys, args.limit, args.batch)
    return 0


if __name__ == "__main__":
    sys.exit(main())
