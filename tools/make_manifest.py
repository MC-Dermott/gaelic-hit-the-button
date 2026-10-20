#!/usr/bin/env python3
"""Rebuild audio/manifest.json from the .mp3 files in audio/.
Run from anywhere:  python3 tools/make_manifest.py
Also reports which words in audio/words.csv still have no recording."""
import csv, json, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
audio = root / "audio"
have = sorted(p.stem for p in audio.glob("*.mp3"))
(audio / "manifest.json").write_text(json.dumps(have, ensure_ascii=False) + "\n")

with open(audio / "words.csv", newline="", encoding="utf-8") as f:
    wanted = [r["filename"][:-4] for r in csv.DictReader(f)]
unknown = [h for h in have if h not in wanted]
missing = [w for w in wanted if w not in have]
print(f"{len(have)} recordings listed; {len(missing)} of {len(wanted)} words still missing")
if unknown:
    print("files not matching any word (check spelling):", ", ".join(unknown))
