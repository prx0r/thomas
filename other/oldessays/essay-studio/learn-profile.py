#!/usr/bin/env python3
"""Learn a taste profile from user feedback.

Reads thumbnail-feedback.json (per essay: {image: rank, ...}, rejected: [...])
and writes taste-profile.json with:
  - image_pref:   per-image cumulative delta from approved rank / rejection
  - source_affinity: per-source (+ per-collection) delta
  - concept_weights: essay-keyword x image-concept deltas (concepts from
    image text tokens; semantic affinity grows as you rank)
  - collections:   source affinity bucketed per essay collection

Run after any review session:  python3 learn-profile.py
"""
import json, os, sys
from pathlib import Path

ESSAYS = Path("/root/projects/ochema2/essays")
FEEDBACK = ESSAYS / "thumbnail-feedback.json"
PROFILE = ESSAYS / "taste-profile.json"
BUNDLE = ESSAYS / "review-bundle.json"

sys.path.insert(0, str(ESSAYS))
from match_thumbnails import norm


def load(p, d):
    if p.exists():
        try:
            return json.loads(p.read_text())
        except Exception:
            pass
    return d


def main():
    feedback = load(FEEDBACK, {})
    bundle = load(BUNDLE, {})
    if not feedback:
        print("no feedback yet — do some review first")
        return

    prof = {
        "image_pref": {},
        "source_affinity": {"all": {}},
        "concept_weights": {},
        "collections": {},
        "meta": {"feedback_essays": len(feedback), "updated": ""},
    }
    import time
    prof["meta"]["updated"] = time.strftime("%Y-%m-%d %H:%M")

    # bootstrap weights (match same spirit as matcher WEIGHTS)
    from match_thumbnails import WEIGHTS
    for w, v in WEIGHTS.items():
        prof["concept_weights"][w] = {"base": v, "delta": 0.0}

    for key, f in feedback.items():
        coll = key.split("/", 1)[0]
        e = bundle.get(key, {})
        kws = set(e.get("keywords", [])) | set(prof["concept_weights"].keys()) & set(e.get("keywords", []))
        ranking = f.get("ranking", {})
        rejected = f.get("rejected", {})
        ccount = max(len(ranking), 1)
        for img, r in ranking.items():
            # rank 1 (best) gets biggest positive delta
            delta = 0.4 + 0.5 * (ccount - r) / max(ccount, 1)
            ip = prof["image_pref"].setdefault(img, {"approved": 0, "rejected": 0, "delta": 0.0})
            ip["approved"] += 1
            ip["delta"] = ip["delta"] * 0.7 + delta * 0.3
            # source affinity
            c = find_candidate(bundle, key, img)
            if c:
                src = c["source"]
                sa = prof["source_affinity"]["all"].setdefault(src, {"approved": 0, "rejected": 0, "delta": 0.0})
                sa["approved"] += 1
                sa["delta"] = min(1.0, sa.get("delta", 0) + 0.08)
                ca = prof["collections"].setdefault(coll, {}).setdefault(src, {"approved": 0, "rejected": 0, "delta": 0.0})
                ca["approved"] += 1
                ca["delta"] = min(1.0, ca.get("delta", 0) + 0.1)
            # concept affinity: essay keywords that appear in image text
            if c:
                ik = norm(c.get("title", ""))
                for w in kws:
                    if w in ik or (w and c.get("title") and w in c["title"].lower()):
                        cw = prof["concept_weights"].setdefault(w, {"base": 1, "delta": 0.0})
                        cw["delta"] = min(2.0, cw.get("delta", 0) + 0.15)
        for img in rejected:
            ip = prof["image_pref"].setdefault(img, {"approved": 0, "rejected": 0, "delta": 0.0})
            ip["rejected"] += 1
            ip["delta"] = max(-1.0, ip.get("delta", 0) - 0.2)
            c = find_candidate(bundle, key, img)
            if c:
                src = c["source"]
                sa = prof["source_affinity"]["all"].setdefault(src, {"approved": 0, "rejected": 0, "delta": 0.0})
                sa["rejected"] += 1
                sa["delta"] = max(-1.0, sa.get("delta", 0) - 0.05)
                ca = prof["collections"].setdefault(coll, {}).setdefault(src, {"approved": 0, "rejected": 0, "delta": 0.0})
                ca["rejected"] += 1
                ca["delta"] = max(-1.0, ca.get("delta", 0) - 0.06)

    PROFILE.write_text(json.dumps(prof, indent=2))
    n_images = len(prof["image_pref"])
    top_src = sorted(prof["source_affinity"]["all"].items(), key=lambda x: -x[1]["delta"])[:5]
    print(f"wrote {PROFILE} | {len(feedback)} essays | {n_images} images")
    print("top sources:", ", ".join(f"{s}({v['delta']:+.2f})" for s, v in top_src))


def find_candidate(bundle, key, img):
    for c in bundle.get(key, {}).get("candidates", []):
        if c["image"] == img:
            return c
    return None


if __name__ == "__main__":
    main()
