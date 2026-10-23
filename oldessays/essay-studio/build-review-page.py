#!/usr/bin/env python3
"""Build a review page: essay + top-3 thumbnail candidates, for vision-model review."""
import json, os, html

MATCHES = "thumbnail-matches.json"
OUT = "thumbnail-review.html"
IMG_DIR = "review-images"


def thumb(m):
    src = m.get("local_path")
    if src:
        return f"review-images/{os.path.basename(src)}"
    return None


def main():
    data = json.load(open(MATCHES))
    # group essays by collection
    collections = {}
    for key, e in data.items():
        coll, fname = key.split("/", 1)
        collections.setdefault(coll, []).append((key, e))

    total_picks = 0
    missing_thumb = 0
    rows = []
    for coll in sorted(collections):
        essays = collections[coll]
        rows.append(f'<h2 class="coll">{html.escape(coll)} <span>({len(essays)})</span></h2>')
        for key, e in essays:
            cells = []
            for m in e["matches"]:
                img = thumb(m)
                total_picks += 1
                if not img:
                    missing_thumb += 1
                src = f'<img src="{img}" loading="lazy">' if img else '<div class="noimg">r2 only</div>'
                cells.append(
                    f'<div class="card">'
                    f'{src}'
                    f'<div class="meta">'
                    f'<div class="score">{m["score"]:.2f}</div>'
                    f'<div class="src">{html.escape(m["source"])}</div>'
                    f'<div class="img">{html.escape(os.path.basename(m["image"]))}</div>'
                    f'<div class="t">{html.escape(m.get("title", "")[:70])}</div>'
                    f'</div></div>'
                )
            kws = " ".join(e["keywords"][:14])
            rows.append(
                f'<div class="essay">'
                f'<div class="header"><h3>{html.escape(e["title"])}</h3>'
                f'<div class="kws">{html.escape(kws)}</div></div>'
                f'<div class="cands">{"".join(cells)}</div>'
                f'</div>'
            )

    body = "\n".join(rows)
    page = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<title>Thumbnail candidates review</title>
<style>
body {{ font-family: system-ui, sans-serif; margin: 24px; background: #141414; color: #e8e8e8; }}
h1 {{ font-size: 22px; }}
.coll {{ margin: 34px 0 6px; border-bottom: 1px solid #444; padding-bottom: 6px; color: #9ecbff; }}
.coll span {{ color: #888; font-weight: normal; }}
.essay {{ margin: 14px 0 22px; }}
.header h3 {{ margin: 0 0 4px; font-size: 15px; }}
.kws {{ color: #9a9a9a; font-size: 11px; }}
.cands {{ display: flex; gap: 10px; margin-top: 8px; }}
.card {{ flex: 1; max-width: 260px; background: #1e1e1e; border: 1px solid #333; border-radius: 8px; overflow: hidden; }}
.card img {{ width: 100%; height: 180px; object-fit: cover; display: block; }}
.noimg {{ width: 100%; height: 180px; display: flex; align-items: center; justify-content: center; background:#2a2a2a; color:#666; }}
.meta {{ padding: 8px; font-size: 11px; }}
.score {{ float: right; color: #ffd166; font-weight: bold; }}
.src {{ color: #7fd6a0; }}
.img {{ color: #bbb; word-break: break-all; }}
.t {{ color: #8a8a8a; margin-top: 3px; }}
</style></head><body>
<h1>Thumbnail candidates — {total_picks} picks ({len(data)} essays)</h1>
{body}
</body></html>
"""
    open(OUT, "w").write(page)
    print(f"wrote {OUT} | {len(data)} essays | {total_picks} picks | {missing_thumb} R2-only (no image shown)")


if __name__ == "__main__":
    main()
