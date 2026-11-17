#!/usr/bin/env python3
"""
Normalise leading/trailing spaces of every translation.

Menyoo appends dynamic values after some labels (`"Invalid flagID entered: "`,
`"Colour ID: "`, `"~b~Error:~s~ "` ...). If a machine translation strips the
trailing space, the next value glues to the label: "ID цвета:12" instead of
"ID цвета: 12". This script restores edge spaces exactly as in the English key.

Usage:
    python tools/fix_edge_spaces.py            # fix all packs
    python tools/fix_edge_spaces.py German     # fix one pack
    python tools/fix_edge_spaces.py --dry-run  # report only
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANG_DIR = ROOT / "Language"


def fix_pack(path: Path, dry_run: bool) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    changed = 0
    for key, value in list(data.items()):
        if not isinstance(value, str):
            continue
        want_lead = key.startswith(" ")
        want_trail = key.endswith(" ")
        have_lead = value.startswith(" ")
        have_trail = value.endswith(" ")
        if want_lead and not have_lead:
            value = " " + value
        elif not want_lead and have_lead and value.strip():
            value = value.lstrip(" ")
        if want_trail and not value.endswith(" "):
            value = value + " "
        elif not want_trail and value.endswith(" ") and value.strip():
            value = value.rstrip(" ")
        if value != data[key]:
            data[key] = value
            changed += 1
    if changed and not dry_run:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{path.name:24s} {'would fix' if dry_run else 'fixed'} {changed} value(s)")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Restore leading/trailing spaces of translations")
    parser.add_argument("packs", nargs="*", help="pack names without .json (default: all)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    files = [LANG_DIR / f"{name}.json" for name in args.packs] if args.packs else sorted(LANG_DIR.glob("*.json"))
    total = sum(fix_pack(path, args.dry_run) for path in files if path.exists())
    print(f"\n{'needs fixing' if args.dry_run else 'fixed'}: {total} value(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
