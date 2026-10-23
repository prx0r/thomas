#!/usr/bin/env python3
"""Merge keyword + gemma candidates into a review bundle with served images.

Candidates per essay:
  - gemma top-5 (from thumbnail-ranks.json, if present)
  - keyword top-3 (from thumbnail-matches.json)
  - fill up to N with next keyword candidates (local images only)

Copies every unique candidate image into review-images/ (dedup by filename)
and writes review-bundle.json for taste-server.py to serve.
"""
import json, os, shutil, sys
from pathlib import Path

ESSAYS = Path("/root/projects/ochema2/essays")
BUNDLE = ESSAYS / "review-bundle.json"
IMG_DIR = ESSAYS / "review-images"
FILL = 8  # max candidates per essay

# reuse matcher internals
sys.path.insert(0, str(ESSAYS))
from match_thumbnails import build_catalog, index_essays, essay_keywords, score, SOURCE_BOOST


def main():
    matches = json.loads((ESSAYS / "thumbnail-matches.json").read_text())
    ranks = {}
    rp = ESSAYS / "thumbnail-ranks.json"
    if rp.exists():
        ranks = json.loads(rp.read_text())

    catalog = build_catalog()
    by_id = {c["id"]: c for c in catalog}
    local = [c for c in catalog if c.get("local_path")]

    IMG_DIR.mkdir(exist_ok=True)
    copied = set()
    bundle = {}

    essays = index_essays()
    for e in essays:
        key = f"{e['collection']}/{e['file']}"
        kws = essay_keywords(e)
        cands = {}

        # 1. gemma picks
        r = ranks.get(key)
        if r:
            for p in r.get("rankings", []):
                i = p.get("image")
                if i in by_id and by_id[i].get("local_path"):
                    cands[i] = by_id[i]

        # 2. keyword top-3 (already in matches)
        m = matches.get(key)
        if m:
            for mm in m.get("matches", []):
                i = mm.get("image")
                if i in by_id and by_id[i].get("local_path"):
                    cands.setdefault(i, by_id[i])

        # 3. fill with next keyword candidates (local only)
        if len(cands) < FILL:
            scored = []
            for c in local:
                if c["id"] in cands:
                    continue
                s = score(kws, c["text"]) * SOURCE_BOOST.get(c["source"], 1.0)
                if s > 0:
                    scored.append((s, c))
            scored.sort(key=lambda x: -x[0])
            for s, c in scored[: FILL - len(cands)]:
                cands[c["id"]] = c

        # copy images
        for c in cands.values():
            src = c["local_path"]
            base = os.path.basename(src)
            dst = IMG_DIR / base
            if not dst.exists():
                try:
                    shutil.copy(src, dst)
                    copied.add(base)
                except Exception as ex:
                    print(f"  copy fail {src}: {ex}")

        bundle[key] = {
            "title": e.get("title") or e["name"],
            "collection": e["collection"],
            "keywords": sorted(kws)[:16],
            "candidates": [
                {
                    "image": c["id"],
                    "source": c["source"],
                    "title": (c.get("title") or "")[:80],
                    "file": os.path.basename(c["local_path"]),
                    "kw": round(score(kws, c["text"]) * SOURCE_BOOST.get(c["source"], 1.0), 2),
                }
                for c in cands.values()
            ],
        }

    BUNDLE.write_text(json.dumps(bundle, indent=2))
    print(f"wrote {BUNDLE} | {len(bundle)} essays | {len(copied)} images copied")


if __name__ == "__main__":
    main()
