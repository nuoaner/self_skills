#!/usr/bin/env python3
import argparse
import re
import shutil
import subprocess
import zipfile
from collections import Counter

TYPEFACE_RE = re.compile(r'typeface="([^"]+)"')


def normalize(name):
    return re.sub(r"[^a-z0-9]", "", name.lower())


def collect_fonts(path):
    counts = Counter()
    with zipfile.ZipFile(path) as zf:
        for name in zf.namelist():
            if not name.endswith(".xml"):
                continue
            if not name.startswith(("ppt/slides/", "ppt/notesSlides/", "ppt/slideLayouts/", "ppt/slideMasters/")):
                continue
            try:
                text = zf.read(name).decode("utf-8", errors="ignore")
            except Exception:
                continue
            for font in TYPEFACE_RE.findall(text):
                if font and not font.startswith(("+mj-", "+mn-")):
                    counts[font] += 1
    return counts


def fc_match(font):
    if not shutil.which("fc-match"):
        return None
    try:
        out = subprocess.check_output(["fc-match", "-f", "%{family}\n", font], text=True, stderr=subprocess.DEVNULL)
        return out.strip().splitlines()[0] if out.strip() else ""
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser(description="Report explicit PPTX fonts and current-environment substitution risk.")
    ap.add_argument("pptx")
    args = ap.parse_args()

    fonts = collect_fonts(args.pptx)
    print("Explicit font families: %d" % len(fonts))
    has_fc = shutil.which("fc-match") is not None
    if not has_fc:
        print("fontconfig unavailable; substitution check skipped")
    for font, count in fonts.most_common():
        match = fc_match(font) if has_fc else None
        if match is None:
            status = "UNKNOWN"
        else:
            requested = normalize(font)
            matched = normalize(match.split(",")[0])
            status = "OK" if requested and requested in matched else "SUBSTITUTED"
        suffix = " -> %s" % match if match is not None else ""
        print("%s | %s | refs=%d%s" % (status, font, count, suffix))


if __name__ == "__main__":
    main()
