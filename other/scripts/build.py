"""build.py — rambles/essays markdown -> Fish .drama.txt (deterministic).

Adds only: // headers, <|speaker:0|>, a stand-in voice tag, [pause, section change]
at ## headings, [soft pause] between paragraphs, [pause] after rhetorical questions.
Strips markdown structure and the ## References section. Never changes a word.

    python3 other/scripts/build.py      # run from repo root

Voice tags are stand-ins, recast at voice lock (damn/voices/registry.md).
Lanes from other/scripts/BEATS.md: rambles -> ramble read, essays -> lectures.
Rules from other/scripts/FORMAT.md (verbatim from damn/docs/drama-syntax.md).

After building: python3 /root/damn/fish/validate.py other/scripts/rambles/*.drama.txt other/scripts/essays/*/*.drama.txt

Law: extract-never-write (damn/AGENTS.md) + never-generate-audio. No API calls.
"""

import re, os, sys

VO_ESAY = "[calm, measured storyteller voice, slow and gentle for sleep]"
VO_RAMB = "[warm companion voice, settling, like a friend on the sofa]"
CAP = 14000

def strip_md(s):
    s = re.sub(r'!\[.*?\]\(.*?\)', '', s)              # images
    s = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', s)     # links -> text
    s = re.sub(r'\[\^[^\]]*\]', '', s)                 # footnote refs
    s = re.sub(r'`([^`]*)`', r'\1', s)                 # code
    s = re.sub(r'\*\*([^*]*)\*\*', r'\1', s)           # bold
    s = re.sub(r'__([^_]*)__', r'\1', s)
    s = re.sub(r'^\s*#{1,6}\s*', '', s)                # heading marks
    s = re.sub(r'^\s*>\s?', '', s)                     # blockquote
    s = re.sub(r'^\s*[-*+]\s+', '', s)                 # bullet markers
    s = re.sub(r'^\s*\d+\.\s+', '', s)                 # numbered markers
    s = re.sub(r'<[^>]+>', '', s)                      # html
    return re.sub(r'[ \t]+', ' ', s).strip()

def blocks_of(md):
    out, cur = [], []
    def flush():
        if cur:
            out.append(("para", strip_md(" ".join(cur))))
            cur.clear()
    for ln in md.splitlines():
        if ln.startswith("## References"):
            flush(); break
        if re.match(r'^\s*#{1,6}\s+\S', ln):
            flush()
            if re.match(r'^\s*#\s+\S', ln) and not ln.startswith("##"):
                continue                              # H1 title -> dropped, lives in header
            out.append(("head", strip_md(re.sub(r'^\s*#{1,6}\s+', '', ln))))
        elif not ln.strip():
            flush()
        else:
            cur.append(ln.strip())
    flush()
    return [b for b in out if b[1]]

def render(blocks, voice):
    lines, first = [], True
    for kind, text in blocks:
        if kind == "head":
            lines.append("")
            lines.append("[pause, section change]")
            lines.append("")
            lines.append(text)   # heading spoken exactly as written — no punctuation added
            first = True
            continue
        if first:
            lines.append(text)
            first = False
        else:
            lines.append("")
            lines.append("[soft pause] " + text)
        if text.rstrip().endswith("?"):
            lines[-1] = lines[-1] + " [pause]"
    return "\n".join(lines).strip()

def chunk(body, cap=CAP):
    if len(body.encode()) <= cap:
        return [body]
    paras = body.split("\n\n")
    parts, cur = [], ""
    for p in paras:
        if len((cur + "\n\n" + p).encode()) > cap and cur:
            parts.append(cur.strip()); cur = p
        else:
            cur = (cur + "\n\n" + p).strip() if cur else p
    if cur.strip(): parts.append(cur.strip())
    return parts

def build(src, dst, title, lane, voice, src_rel):
    md = open(src, encoding="utf-8").read()
    b = blocks_of(md)
    words = sum(len(t.split()) for k, t in b)
    body = render(b, voice)
    parts = chunk(body)
    n = len(parts)
    for i, part in enumerate(parts, 1):
        suffix = f".part{i}" if n > 1 else ""
        path = os.path.join(dst, os.path.splitext(os.path.basename(src))[0] + suffix + ".drama.txt")
        hdr = [
            f"// THOMAS — {title}",
            f"// lane: {lane} (docs/video-structure.md) | model s2.1-pro-free ($0, free-only law) | speed 0.85 | latency normal",
            f"// source: {src_rel} ({os.path.getsize(src)} B, {words} words)",
            "// body is the source text VERBATIM — only // headers, [cues] and section breaks were added (extract-never-write, damn/AGENTS.md)",
            "// narrator STAND-IN — recast at voice lock (damn/voices/registry.md); never shared outside this project at lock",
            f"// CHUNKS: {n} of {n} (each at most 14000 bytes, split at section breaks)",
            "// REFERENCES: not spoken — see the source file for the references section",
            "// SFX: none in first pass",
        ]
        text = "\n".join(hdr) + "\n\n<|speaker:0|>\n\n" + voice + "\n\n" + part + "\n"
        os.makedirs(dst, exist_ok=True)
        open(path, "w", encoding="utf-8").write(text)
        print(f"  {os.path.relpath(path, T):55s} {len(text.encode()):6d} B  {len(text.split()):5d} w")

T = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
jobs = [
 ("rambles/samsara1.md",  "other/scripts/rambles",      "samsara ramble 1",        "ramble read",  VO_RAMB),
 ("rambles/nibbana1.md",   "other/scripts/rambles",      "nibbana ramble 1",        "ramble read",  VO_RAMB),
 ("rambles/rebirth1.md",   "other/scripts/rambles",      "rebirth ramble 1",        "ramble read",  VO_RAMB),
 ("essays/samsara/samsaraessayai1.md",   "other/scripts/essays/samsara",  "samsara essay ai1", "lectures", VO_ESAY),
 ("essays/samsara/samsaraessayai2.md",   "other/scripts/essays/samsara",  "samsara essay ai2", "lectures", VO_ESAY),
 ("essays/nibbana/nibbanaessayai1.md",   "other/scripts/essays/nibbana",  "nibbana essay ai1",  "lectures", VO_ESAY),
 ("essays/nibbana/nibbanaessayai2.md",   "other/scripts/essays/nibbana",  "nibbana essay ai2",  "lectures", VO_ESAY),
 ("essays/rebirth/rebirthessayai1.md",   "other/scripts/essays/rebirth",  "rebirth essay ai1",  "lectures", VO_ESAY),
 ("essays/rebirth/rebirthessayai2.md",   "other/scripts/essays/rebirth",  "rebirth essay ai2",  "lectures", VO_ESAY),
]
print("building:")
for rel, dst, title, lane, voice in jobs:
    s = os.path.join(T, rel)
    if not os.path.exists(s):
        print(f"  MISSING {rel}"); continue
    build(s, os.path.join(T, dst), title, lane, voice, rel)
