#!/usr/bin/env python3
"""Rank thumbnail candidates per essay using Gemma vision (Google GenAI).

For each essay, gather up to N keyword-matched candidates (local images only,
so we can send actual pixels), send them all in ONE gemma call, and get a
ranked top-5 with one-line reasons.

Output: essays/thumbnail-ranks.json
"""
import base64, io, json, os, re, sys, time
from pathlib import Path
from PIL import Image

from google import genai
from google.genai import types

from match_thumbnails import build_catalog, index_essays, essay_keywords, score, SOURCE_BOOST

ESSAYS = Path("/root/projects/ochema2/essays")
OUT = ESSAYS / "thumbnail-ranks.json"
MODEL = "gemma-4-31b-it"
API_KEY = os.environ.get("GOOGLE_API_KEY", "AQ.REDACTED-BEFORE-COMMIT")

TOPN_KD = 10       # keyword prefilter: how many candidates to send to gemma
RANK = 5           # how many the model should return
MAX_PX = 480       # downscale before base64


def encode(path):
    img = Image.open(path).convert("RGB")
    if max(img.size) > MAX_PX:
        r = MAX_PX / max(img.size)
        img = img.resize((int(img.width * r), int(img.height * r)))
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=80)
    return buf.getvalue()


def essay_theme(e):
    """A short one-line theme descriptor for the ranking prompt."""
    title = e.get("title") or e["name"]
    # first ~160 chars of body
    body = re.sub(r"[#*_\-|`>\[\]]+", " ", e.get("body", ""))[:200]
    return f"{title}. {body}"


def rank_one(client, e, candidates):
    parts = []
    for i, c in enumerate(candidates):
        parts.append(types.Part(text=f"CANDIDATE {i}:"))
        parts.append(types.Part(inline_data=types.Blob(
            mime_type="image/jpeg", data=encode(c["local_path"]))))
    parts.append(types.Part(text=(
        f"These {len(candidates)} images are candidate thumbnails for an essay. "
        f"ESSAY: {essay_theme(e)}\n"
        f"Pick the {RANK} best-fitting images as thumbnail art. "
        "Return STRICT JSON: {\"rankings\":[{\"index\":<int>,\"reason\":\"<one line>\"}...]} "
        "ordered best-first. Only JSON, nothing else."
    )))
    resp = client.models.generate_content(
        model=MODEL, contents=types.Content(parts=parts))
    text = resp.text
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if not m:
        return None, text
    return json.loads(m.group()), text


def main():
    client = genai.Client(api_key=API_KEY)
    catalog = build_catalog()
    essays = index_essays()

    # only local images can be sent
    local = [c for c in catalog if c.get("local_path")]

    only = None
    if len(sys.argv) > 1:
        only = sys.argv[1]
    if only:
        essays = [e for e in essays if e["collection"] == only]

    # resume support
    done = set()
    if OUT.exists():
        prev = json.loads(OUT.read_text())
        done = set(prev.keys())
    else:
        prev = {}

    for e in essays:
        key = f"{e['collection']}/{e['file']}"
        if key in done:
            print(f"SKIP {key}")
            continue

        kws = essay_keywords(e)
        scored = []
        for c in local:
            s = score(kws, c["text"])
            if s > 0:
                scored.append((s * SOURCE_BOOST.get(c["source"], 1.0), c))
        scored.sort(key=lambda x: -x[0])
        candidates = [c for _, c in scored[:TOPN_KD]]

        print(f"RANK {key} ({len(candidates)} candidates) ...", flush=True)
        if len(candidates) < 3:
            prev[key] = {"title": e["title"] or e["name"], "keywords": sorted(kws),
                         "rankings": [], "note": f"only {len(candidates)} candidates"}
            OUT.write_text(json.dumps(prev, indent=2))
            continue

        result, raw = rank_one(client, e, candidates)
        if result is None:
            print(f"  parse fail: {raw[:120]!r}")
            prev[key] = {"title": e["title"] or e["name"], "keywords": sorted(kws),
                         "rankings": [], "error": raw[:300]}
            OUT.write_text(json.dumps(prev, indent=2))
            continue

        picks = []
        for r in result.get("rankings", [])[:RANK]:
            i = r.get("index")
            if not isinstance(i, int) or not (0 <= i < len(candidates)):
                continue
            c = candidates[i]
            picks.append({
                "rank": len(picks) + 1,
                "index": i,
                "image": c["id"],
                "source": c["source"],
                "title": c.get("title", ""),
                "local_path": c["local_path"],
                "reason": r.get("reason", ""),
            })
        prev[key] = {"title": e["title"] or e["name"], "keywords": sorted(kws),
                     "rankings": picks}
        OUT.write_text(json.dumps(prev, indent=2))
        print(f"  -> {[p['rank'] for p in picks]}")
        time.sleep(1)

    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
