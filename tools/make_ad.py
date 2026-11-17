#!/usr/bin/env python3
"""Render assets/ad.html into an MP4 ad (headless Chrome frames + ffmpeg).

    python tools/make_ad.py                 # 1280x720, 30 fps, 12.5 s
    python tools/make_ad.py --fps 60        # smoother, twice the frames
    python tools/make_ad.py --workers 6     # more parallel browser instances

Needs Chrome/Edge (screenshots) and ffmpeg with libx264 (encoding).
The animation is a pure function of `?t=<seconds>`, so every frame is exact
and the render is reproducible.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import glob
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "assets" / "ad.html"
OUT = ROOT / "assets" / "menyoo-language-packs-ad.mp4"
POSTER = ROOT / "assets" / "ad-poster.png"
FRAMES = ROOT / "build" / "ad_frames"

BROWSERS = [
    r"C:/Program Files/Google/Chrome/Application/chrome.exe",
    r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
    r"C:/Program Files/Microsoft/Edge/Application/msedge.exe",
    r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]


def find_browser() -> str:
    env = os.environ.get("CHROME")
    if env and Path(env).exists():
        return env
    for path in BROWSERS:
        if Path(path).exists():
            return path
    for name in ("chrome", "chromium", "google-chrome", "msedge"):
        found = shutil.which(name)
        if found:
            return found
    sys.exit("no Chrome/Edge/Chromium found — set CHROME=/path/to/browser")


def find_ffmpeg() -> str:
    found = shutil.which("ffmpeg")
    if found:
        return found
    local = os.environ.get("LOCALAPPDATA", "")
    for pattern in (
        f"{local}/Microsoft/WinGet/Packages/*ffmpeg*/**/ffmpeg.exe",
        f"{local}/Microsoft/WinGet/Links/ffmpeg.exe",
        "/usr/bin/ffmpeg",
        "/opt/homebrew/bin/ffmpeg",
    ):
        hits = glob.glob(pattern, recursive=True)
        if hits:
            return hits[0]
    sys.exit("ffmpeg not found — winget install Gyan.FFmpeg, or set PATH")


def grab(browser: str, t: float, dest: Path, width: int, height: int, profile: str) -> Path:
    url = PAGE.as_uri() + f"?t={t:.4f}"
    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-extensions",
        "--force-device-scale-factor=1",
        f"--window-size={width},{height}",
        f"--user-data-dir={profile}",
        f"--screenshot={dest}",
        url,
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    if not dest.exists():
        raise RuntimeError(f"no screenshot for t={t}")
    return dest


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--duration", type=float, default=12.6)
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--height", type=int, default=720)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--keep-frames", action="store_true")
    args = ap.parse_args()

    if not PAGE.exists():
        sys.exit(f"missing page: {PAGE}")
    browser, ffmpeg = find_browser(), find_ffmpeg()

    if FRAMES.exists():
        shutil.rmtree(FRAMES)
    FRAMES.mkdir(parents=True)

    total = int(round(args.fps * args.duration))
    profiles = [tempfile.mkdtemp(prefix=f"adchrome{i}-") for i in range(args.workers)]
    jobs = [(i, i / args.fps, profiles[i % args.workers]) for i in range(total)]

    done = 0
    with cf.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(grab, browser, t, FRAMES / f"{i:05d}.png", args.width, args.height, prof): i
            for i, t, prof in jobs
        }
        for fut in cf.as_completed(futures):
            fut.result()
            done += 1
            if done % 25 == 0 or done == total:
                print(f"  frames {done}/{total}", flush=True)

    for prof in profiles:
        shutil.rmtree(prof, ignore_errors=True)

    out = Path(args.out)
    cmd = [
        ffmpeg, "-y", "-framerate", str(args.fps), "-i", str(FRAMES / "%05d.png"),
        "-c:v", "libx264", "-preset", "slow", "-crf", "18",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    poster_frame = FRAMES / f"{int(1.6 * args.fps):05d}.png"
    if poster_frame.exists():
        shutil.copyfile(poster_frame, POSTER)

    size_mb = out.stat().st_size / 1024 / 1024
    print(f"wrote {out.relative_to(ROOT)}  {args.width}x{args.height}  "
          f"{args.fps} fps  {args.duration}s  {size_mb:.1f} MB")
    if POSTER.exists():
        print(f"wrote {POSTER.relative_to(ROOT)}")

    if not args.keep_frames:
        shutil.rmtree(FRAMES, ignore_errors=True)


if __name__ == "__main__":
    main()
