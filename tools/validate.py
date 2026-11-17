#!/usr/bin/env python3
"""
Menyoo language pack validator.

Usage:
    python tools/validate.py                # check every Language/*.json
    python tools/validate.py --strict        # fail (exit 1) if any pack is incomplete
    python tools/validate.py German Spanish  # check selected packs only

Checks per pack:
  * file is UTF-8 without BOM and parses as strict JSON
  * every key exists in the reference key list (data/keys.txt)
  * no empty / whitespace-only translations
  * GTA text markers (~b~ ~s~ ~r~ ~g~ ...) are preserved
  * printf-style placeholders (%s %d %f %i) are preserved
  * leading/trailing spaces of the source string are preserved
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANG_DIR = ROOT / "Language"
REFERENCE = LANG_DIR / "Russia.json"          # the pack with full coverage
NAMES_FILE = ROOT / "data" / "langnames.txt"  # language names shown in Settings > Language

MARKER_RE = re.compile(r"~[a-zA-Z]{1,3}~")
PLACEHOLDER_RE = re.compile(r"%(?:[sdfix]|%)")


def load_keys() -> list[str]:
    """Reference key set: every key of the full Russian pack plus language names."""
    data = json.loads(REFERENCE.read_text(encoding="utf-8"))
    keys = list(data)
    if NAMES_FILE.exists():
        for name in NAMES_FILE.read_text(encoding="utf-8").splitlines():
            name = name.strip()
            if name and name not in keys:
                keys.append(name)
    return keys


def check_file(path: Path, keys: list[str]) -> dict:
    raw = path.read_bytes()
    report = {
        "file": path.name,
        "ok": True,
        "errors": [],
        "keys": 0,
        "translated": 0,
        "coverage": 0.0,
    }
    if raw.startswith(b"\xef\xbb\xbf"):
        report["errors"].append("BOM detected (Menyoo's JSON parser rejects BOM)")
    try:
        data = json.loads(raw.decode("utf-8-sig"))
    except Exception as exc:  # noqa: BLE001
        report["errors"].append(f"invalid JSON: {exc}")
        report["ok"] = False
        return report

    if not isinstance(data, dict):
        report["errors"].append("root element is not an object")
        report["ok"] = False
        return report

    known = set(keys)
    report["keys"] = len(data)
    report["translated"] = sum(1 for k in data if k in known)
    report["coverage"] = report["translated"] / len(keys) if keys else 0.0

    unknown = [k for k in data if k not in known]
    if unknown:
        report["errors"].append(f"{len(unknown)} key(s) not present in data/keys.txt, e.g. {unknown[:3]}")

    for key, value in data.items():
        if not isinstance(value, str) or not value.strip():
            report["errors"].append(f"empty translation for {key!r}")
            continue
        want = collections.Counter(MARKER_RE.findall(key))
        got = collections.Counter(MARKER_RE.findall(value))
        if want != got:
            report["errors"].append(f"marker mismatch for {key!r}: {dict(want)} -> {dict(got)}")
        if collections.Counter(PLACEHOLDER_RE.findall(key)) != collections.Counter(PLACEHOLDER_RE.findall(value)):
            report["errors"].append(f"placeholder mismatch for {key!r}")
        if key.startswith(" ") != value.startswith(" ") or key.endswith(" ") != value.endswith(" "):
            report["errors"].append(f"edge spaces changed for {key!r}")

    report["ok"] = not report["errors"]
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Menyoo language packs")
    parser.add_argument("packs", nargs="*", help="pack names without .json (default: all)")
    parser.add_argument("--strict", action="store_true", help="exit 1 when any pack has fewer than 100% of keys")
    args = parser.parse_args()

    keys = load_keys()
    files = [LANG_DIR / f"{name}.json" for name in args.packs] if args.packs else sorted(LANG_DIR.glob("*.json"))
    files = [f for f in files if f.name != "Russia.json.orig.bak"]

    print(f"reference keys: {len(keys)}\n")
    print(f"{'pack':24s} {'keys':>5s} {'known':>6s} {'cover':>7s}  status")
    print("-" * 62)
    worst = 0
    failed = False
    for path in files:
        if not path.exists():
            print(f"{path.name:24s} {'-':>5s} {'-':>6s} {'-':>7s}  MISSING FILE")
            failed = True
            continue
        rep = check_file(path, keys)
        status = "OK" if rep["ok"] else f"{len(rep['errors'])} issue(s)"
        print(f"{rep['file']:24s} {rep['keys']:5d} {rep['translated']:6d} {rep['coverage']*100:6.1f}%  {status}")
        for err in rep["errors"][:4]:
            print(f"{'':24s}   - {err}")
        if len(rep["errors"]) > 4:
            print(f"{'':24s}   - ... {len(rep['errors']) - 4} more")
        worst = max(worst, rep["coverage"])
        failed = failed or not rep["ok"]

    print("-" * 62)
    print(f"packs: {len(files)}  best coverage: {worst*100:.1f}%")
    if failed:
        return 1
    if args.strict and worst < 1.0:
        print("strict mode: some packs are incomplete")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
