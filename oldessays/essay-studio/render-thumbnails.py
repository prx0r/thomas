#!/usr/bin/env python3
"""Auto-render thumbnails for essays using best available pick.

Pick selection: gemma rank-1 (if thumbnail-ranks.json has it), else keyword
rank-1 from thumbnail-matches.json. Caption = shortened essay title (≤6 words,
per thumbnail-analysis findings). Uses thumbnail_render.build_spec + render.

Output: essays/thumbnails/<collection>/<essay>.jpg
"""
import json, os, re, sys
from pathlib import Path

ESSAYS = Path("/root/projects/ochema2/essays")
OUT = ESSAYS / "thumbnails"
sys.path.insert(0, "/root/projects/blog/scripts")
sys.path.insert(0, str(ESSAYS))
import thumbnail_render as TR
from match_thumbnails import build_catalog


def short_caption(title, max_words=6):
    t = re.sub(r"[\u2014\-:.]", " ", title)
    t = re.sub(r"\s+", " ", t).strip()
    words = t.split()
    return " ".join(words[:max_words])


def main():
    matches = json.loads((ESSAYS / "thumbnail-matches.json").read_text())
    ranks = {}
    rp = ESSAYS / "thumbnail-ranks.json"
    if rp.exists():
        ranks = json.loads(rp.read_text())

    catalog = build_catalog()
    by_id = {c["id"]: c for c in catalog}

    # decide treatment/font by source
    STYLE = {
        "alchemy-emblem": ("engraving_crisp", "im_fell_english"),
        "seed-neoplatonic": ("historical_gentle", "cinzel"),
        "seed-sufi": ("historical_gentle", "cormorant_garamond"),
        "seed-kashmir": ("historical_gentle", "cormorant_garamond"),
        "seed-hermetic": ("sepia_classic", "eb_garamond"),
        "seed-buddhist_philosophy": ("sepia_classic", "eb_garamond"),
        "local-curated": ("historical_gentle", "eb_garamond"),
        "thangka": ("sepia_classic", "eb_garamond"),
    }

    rendered = skipped = 0
    for key, m in matches.items():
        coll, fname = key.split("/", 1)
        title = m.get("title") or fname
        pick = None
        r = ranks.get(key)
        if r and r.get("rankings"):
            img_id = r["rankings"][0]["image"]
            if img_id in by_id and by_id[img_id].get("local_path"):
                pick = by_id[img_id]
        if pick is None:
            for mm in m.get("matches", []):
                img_id = mm.get("image")
                if img_id in by_id and by_id[img_id].get("local_path"):
                    pick = by_id[img_id]
                    break
        if pick is None:
            # fallback: any local candidate in the whole catalog (keyword score)
            from match_thumbnails import essay_keywords, score, SOURCE_BOOST, index_essays
            e = next((x for x in index_essays() if x["collection"] == coll and x["file"] == fname), None)
            if e:
                kws = essay_keywords(e)
                local = [c for c in catalog if c.get("local_path")]
                best = max(local, key=lambda c: score(kws, c["text"]) * SOURCE_BOOST.get(c["source"], 1.0))
                if best:
                    pick = best
        if pick is None:
            skipped += 1
            continue

        preset, font = STYLE.get(pick["source"], ("historical_gentle", "eb_garamond"))
        caption = short_caption(title)
        spec = TR.build_spec(title, pick["id"], caption, font, "landscape_below", preset)
        out = OUT / coll / (fname.replace(".md", "").replace(".json", "") + ".jpg")
        lookup = {pick["id"]: pick["local_path"]}
        if TR.render_thumbnail(spec, lookup, str(out)):
            rendered += 1

    print(f"rendered {rendered} thumbnails, skipped {skipped}")


if __name__ == "__main__":
    main()
