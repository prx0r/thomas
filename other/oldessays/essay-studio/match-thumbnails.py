#!/usr/bin/env python3
"""Match top-N candidate thumbnail images to each essay.

Catalogs every available image (local curated art, alchemy emblems, seed-images,
R2 wikiart metadata, R2 thangka captions) with semantic text, then scores each
essay (title + concepts + filename) against each image via keyword overlap.

Output: essays/thumbnail-matches.json  (per-essay top 3)
"""
import json, os, re, sys
from pathlib import Path

BLOG = Path("/root/projects/blog")
ESSAYS = Path("/root/projects/ochema2/essays")
OUT = ESSAYS / "thumbnail-matches.json"

# ---------------------------------------------------------------------------
# 1. Build image catalog
# ---------------------------------------------------------------------------
def norm(s):
    s = s.lower()
    s = re.sub(r"[\'\"\u2019\u2018]", "", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return set(w for w in s.split() if len(w) > 2)

def load_wikiart():
    imgs = []
    path = "/tmp/opencode/wikiart.jsonl"
    if not os.path.exists(path):
        return imgs
    with open(path) as f:
        for line in f:
            try:
                d = json.loads(line)
            except Exception:
                continue
            imgs.append({
                "id": d.get("id", ""),
                "text": f"{d.get('title','')} {d.get('artist','')} {d.get('movement','')}",
                "movement": d.get("movement", ""),
                "title": d.get("title", ""),
                "artist": d.get("artist", ""),
                "r2_path": d.get("local_path", ""),
                "source": "wikiart",
            })
    return imgs

def load_cirthan():
    """Thangka captions (level1-3 descriptions) from R2."""
    imgs = []
    path = "/tmp/opencode/cirthan_train.json"
    if not os.path.exists(path):
        return imgs
    try:
        with open(path) as f:
            data = json.load(f)
    except Exception:
        return imgs
    for d in data:
        text = " ".join(str(d.get(k, "")) for k in ("level1", "level2", "level3"))
        imgs.append({
            "id": f"thangka_{d.get('thangka_id','')}",
            "text": text,
            "movement": "thangka",
            "title": d.get("level1", ""),
            "artist": "",
            "r2_path": f"images/cytkv1/cytkv1_{d.get('thangka_id','')}.jpg",
            "source": "thangka",
        })
    return imgs

def load_local_curated():
    """public/art — semantic filenames."""
    imgs = []
    d = BLOG / "public" / "art"
    if d.exists():
        for f in sorted(d.glob("*")):
            if f.suffix.lower() not in (".jpg", ".jpeg", ".png"):
                continue
            name = f.stem.replace("art_", "").replace("_", " ")
            imgs.append({
                "id": f.name,
                "text": name,
                "movement": "curated",
                "title": name,
                "artist": "",
                "r2_path": "",
                "local_path": str(f),
                "source": "local-curated",
            })
    return imgs

def load_alchemy_emblems():
    imgs = []
    d = BLOG / "content" / "sources" / "occult" / "alchemy" / "emblems"
    if d.exists():
        for gallery in sorted(d.iterdir()):
            if not gallery.is_dir():
                continue
            for j in sorted(gallery.glob("*.json")):
                imgfile = j.with_suffix(".jpg")
                if not imgfile.exists():
                    continue
                try:
                    meta = json.loads(j.read_text())
                except Exception:
                    meta = {}
                cap = re.sub(r"<[^>]+>", "", meta.get("caption", ""))
                imgs.append({
                    "id": imgfile.stem,
                    "text": f"alchemy {cap} {meta.get('source','')}",
                    "movement": "alchemy-emblem",
                    "title": cap[:80],
                    "artist": meta.get("source", ""),
                    "r2_path": "",
                    "local_path": str(imgfile),
                    "source": "alchemy-emblem",
                })
    return imgs

def load_seed_images():
    imgs = []
    d = BLOG / "content" / "video-objects" / "seed-images"
    if d.exists():
        for world in sorted(d.iterdir()):
            originals = world / "originals"
            if not originals.exists():
                continue
            for f in sorted(originals.iterdir()):
                if f.suffix.lower() not in (".jpg", ".jpeg", ".png"):
                    continue
                name = f.stem.replace("art_commons_file_", "").replace("_", " ")
                imgs.append({
                    "id": f.name,
                    "text": f"{world.name} {name}",
                    "movement": world.name,
                    "title": name,
                    "artist": "",
                    "r2_path": "",
                    "local_path": str(f),
                    "source": f"seed-{world.name}",
                })
    return imgs

def build_catalog():
    catalog = []
    catalog += load_local_curated()
    catalog += load_alchemy_emblems()
    catalog += load_seed_images()
    catalog += load_wikiart()
    catalog += load_cirthan()
    return catalog

# ---------------------------------------------------------------------------
# 2. Essay index
# ---------------------------------------------------------------------------
def essay_keywords(essay):
    """Combine filename, title, body text, and JSON concepts into a keyword set."""
    kws = set()
    text = essay["name"] + " " + essay.get("title", "") + " " + essay.get("body", "")
    for k in essay.get("concepts", []) or []:
        text += " " + str(k)
    kws |= norm(text)
    return kws

def index_essays():
    essays = []
    for d in sorted(ESSAYS.iterdir()):
        if not d.is_dir() or d.name.startswith("."):
            continue
        for f in sorted(d.iterdir()):
            if f.suffix == ".md":
                title = ""
                text = f.read_text(errors="ignore")
                first = text.splitlines()
                for line in first[:4]:
                    if line.startswith("# "):
                        title = line[2:]
                        break
                body = " ".join(first[:40])
                essays.append({
                    "collection": d.name,
                    "file": f.name,
                    "name": f.stem.replace("-", " ").replace("_", " "),
                    "title": title,
                    "concepts": [],
                    "body": body[:2000],
                    "source": "md",
                })
            elif f.suffix == ".json":
                try:
                    d_ = json.loads(f.read_text())
                except Exception:
                    continue
                essays.append({
                    "collection": d.name,
                    "file": f.name,
                    "name": f.stem.replace("-", " ").replace("_", " "),
                    "title": str(d_.get("title", "")),
                    "concepts": d_.get("concepts", []),
                    "body": str(d_.get("title", "")),
                    "source": "json",
                })
    return essays

# ---------------------------------------------------------------------------
# 3. Scoring
# ---------------------------------------------------------------------------
WEIGHTS = {
    "soul": 2, "spirit": 2, "divine": 2, "god": 2, "light": 2,
    "consciousness": 2, "awareness": 2, "self": 1.5, "mind": 1.5,
    "universe": 2, "cosmos": 2, "matter": 2, "fire": 2, "alchemy": 3,
    "imagination": 2, "dream": 2, "angel": 3, "daimon": 3, "death": 2,
    "beauty": 2, "love": 2, "soul": 2, "sun": 2, "moon": 2, "mirror": 2,
    "body": 1.5, "stone": 2, "jewel": 2, "serpent": 3, "dragon": 3,
    "snake": 2, "lotus": 2, "rose": 2, "mountain": 2, "sea": 1.5,
}

def score(essay_kws, img_text):
    ik = norm(img_text)
    if not ik:
        return 0
    overlap = essay_kws & ik
    s = 0
    for w in overlap:
        s += WEIGHTS.get(w, 1)
    # normalize by image description length (long captions shouldn't dominate)
    s = s / (len(ik) ** 0.35)
    return s

# boost curated/local art over raw wikiart noise
SOURCE_BOOST = {
    "local-curated": 2.0,
    "alchemy-emblem": 1.5,
    "seed-neoplatonic": 3.0,
    "seed-sufi": 2.5,
    "seed-kashmir": 2.5,
    "seed-hermetic": 2.5,
    "seed-buddhist_philosophy": 2.0,
    "seed-yoga_philosophy": 2.0,
    "wikiart": 0.6,
    "thangka": 1.2,
}

def match(catalog, essays, topn=3):
    out = {}
    for e in essays:
        kws = essay_keywords(e)
        scored = []
        for img in catalog:
            s = score(kws, img["text"])
            if s > 0:
                s = s * SOURCE_BOOST.get(img["source"], 1.0)
                scored.append((s, img))
        scored.sort(key=lambda x: -x[0])
        picks = scored[:topn]
        out[f"{e['collection']}/{e['file']}"] = {
            "title": e["title"] or e["name"],
            "keywords": sorted(kws),
            "matches": [
                {
                    "rank": i + 1,
                    "score": round(s, 2),
                    "image": img["id"],
                    "source": img["source"],
                    "title": img.get("title", ""),
                    "artist": img.get("artist", ""),
                    "local_path": img.get("local_path", ""),
                    "r2_path": img.get("r2_path", ""),
                }
                for i, (s, img) in enumerate(picks)
            ],
        }
    return out

def main():
    catalog = build_catalog()
    essays = index_essays()
    print(f"catalog: {len(catalog)} images | essays: {len(essays)}", file=sys.stderr)
    out = match(catalog, essays)
    OUT.write_text(json.dumps(out, indent=2))
    # summary
    matched = sum(1 for v in out.values() if v["matches"])
    no = sum(1 for v in out.values() if not v["matches"])
    print(f"written {OUT} | {matched} essays matched, {no} with no candidate", file=sys.stderr)

if __name__ == "__main__":
    main()
