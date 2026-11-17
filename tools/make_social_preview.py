#!/usr/bin/env python3
"""Rasterise assets/social-card.html into assets/social-preview.png (1280x640).

GitHub wants 1280x640 for a repository social preview. The card is plain
HTML/CSS, so a headless Chrome/Edge does the rendering: full Unicode, real
system fonts, no extra dependencies.

    python tools/make_social_preview.py
    python tools/make_social_preview.py --width 1280 --height 640

Set CHROME=/path/to/chrome to override browser autodetection.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARD = ROOT / "assets" / "social-card.html"
OUT = ROOT / "assets" / "social-preview.png"

CANDIDATES = [
    r"C:/Program Files/Google/Chrome/Application/chrome.exe",
    r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
    r"C:/Program Files/Microsoft/Edge/Application/msedge.exe",
    r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]


def find_browser() -> str:
    env = os.environ.get("CHROME")
    if env and Path(env).exists():
        return env
    for path in CANDIDATES:
        if Path(path).exists():
            return path
    for name in ("chrome", "chromium", "google-chrome", "msedge"):
        found = shutil.which(name)
        if found:
            return found
    sys.exit("no Chrome/Edge/Chromium found — set CHROME=/path/to/browser")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--height", type=int, default=640)
    args = ap.parse_args()

    if not CARD.exists():
        sys.exit(f"missing card: {CARD}")

    browser = find_browser()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        f"--window-size={args.width},{args.height}",
        f"--screenshot={OUT}",
        CARD.as_uri(),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if not OUT.exists():
        sys.exit("browser produced no screenshot")

    size_kb = OUT.stat().st_size // 1024
    try:  # report the real pixel size without importing anything heavy
        import struct

        with OUT.open("rb") as fh:
            fh.read(16)
            w, h = struct.unpack(">II", fh.read(8))
        print(f"wrote {OUT.relative_to(ROOT)}  {w}x{h}  {size_kb} KB")
    except Exception:
        print(f"wrote {OUT.relative_to(ROOT)}  {size_kb} KB")


if __name__ == "__main__":
    main()
