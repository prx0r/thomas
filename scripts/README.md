# scripts — the rambles and essays as Fish feed

The dramatic-text layer: the same texts you already wrote, in the format
`fish/client.py` consumes — `//` headers, `[cues]` for pauses and voice,
section breaks, at sleep pace. What gets fed to Fish. Nothing here is new
prose.

Source of the format is the Fish house, `/root/damn`:

| File here | Copied verbatim from | What it is |
|---|---|---|
| `FORMAT.md` | `damn/docs/drama-syntax.md` | The tag rules — placement is meaning, pairing, tag budgets, well-tested tags, knobs |
| `BEATS.md` | `damn/docs/video-structure.md` | Universal beats (cold open → settle → walk → turn → return → goodnight) + lane overlays |
| `examples/*.drama.txt` | three `damn/projects/*/` scripts, byte-identical | Two-speaker tale, mono diary, and a full six-section essay |

`FORMAT.md` and `BEATS.md` are **verbatim copies, not rewrites** — read them
there rather than here. The three examples are untouched reference material,
not thomas output.

## The two laws this folder obeys

1. **Extract, never write** (`damn/AGENTS.md`, owner doctrine 2026-10-21).
   An agent composes no script prose. Body text in every file here is the
   source markdown **verbatim**. Only three things are added: `//` headers,
   `[cues]`, and section breaks. Where a beat would need a sentence nobody
   has written — a cold open, a goodnight — the sentence is not written. See
   *Open slots* below.
2. **Never generate audio.** `client.tts()` refuses in code. Direction is
   proven on paper by `damn/fish/validate.py`, never by rendering. Nothing in
   this repo calls an API.

## What the converter does — and what it will not do

`build.py` (this folder, reproducible) applies exactly this:

**Adds**
- A `//` header: title, lane, model, source path + byte/word counts, the
  verbatim pledge, stand-in voice notice, chunk count, references note, SFX.
- `<|speaker:0|>` and a voice-profile tag, both taken from tags already in
  use in `damn` — no invented tag names.
- `[pause, section change]` on its own line at every `##` heading, with the
  heading text spoken **exactly as written — no punctuation added** (`The exam`,
  not `The exam.`).
- `[soft pause]` at the start of every paragraph after the first in a section.
- `[pause]` at the end of any paragraph that ends on a rhetorical question.
- A lane from `BEATS.md`: **rambles → ramble read**, **essays → lectures**
  (question → walk → one idea → drift-out).

**Never touches**
- A word, comma, typo, capitalisation, or the owner's asides. Rambles keep
  their raw register and their pasted fact-check blocks exactly as written.
- Section order or paragraph order.

**Strips (markdown structure only, never words)**
- `#` heading marks, `**` bold, backticks, link URLs keeping link text,
  footnote refs, bullet and number markers, blockquote `>` marks.
- The **`## References` section and everything after it** — a read does not
  cite. Header line points at the source file instead.
- The H1 title — it lives in the header comment.

## Inventory — 9 scripts, mirroring `rambles/` + `essays/`

| Script | Bytes | Words | Mirrors |
|---|---:|---:|---|
| `rambles/samsara1.drama.txt` | 13,732 | 2,402 | `rambles/samsara1.md` |
| `rambles/nibbana1.drama.txt` | 7,909 | 1,394 | `rambles/nibbana1.md` |
| `rambles/rebirth1.drama.txt` | 9,602 | 1,688 | `rambles/rebirth1.md` |
| `essays/samsara/samsaraessayai1.drama.txt` | 13,376 | 2,327 | `essays/samsara/samsaraessayai1.md` |
| `essays/samsara/samsaraessayai2.drama.txt` | 14,040 | 2,454 | `essays/samsara/samsaraessayai2.md` |
| `essays/nibbana/nibbanaessayai1.drama.txt` | 9,735 | 1,659 | `essays/nibbana/nibbanaessayai1.md` |
| `essays/nibbana/nibbanaessayai2.drama.txt` | 10,812 | 1,841 | `essays/nibbana/nibbanaessayai2.md` |
| `essays/rebirth/rebirthessayai1.drama.txt` | 10,997 | 1,879 | `essays/rebirth/rebirthessayai1.md` |
| `essays/rebirth/rebirthessayai2.drama.txt` | 11,961 | 2,056 | `essays/rebirth/rebirthessayai2.md` |

`ESSAY.md` is not mirrored separately: for samsara and nibbana it is
byte-identical to `ai1`, for rebirth byte-identical to `ai2`. Mirroring it
would be the same script twice.

Every script fits one Fish call: spoken body 7,208–13,324 bytes, all under
the 14,000 working budget, all far under the 16,000 hard cap. So
**`CHUNKS: 1 of 1` on every file** — no `.part1` splitting was needed. (Had
any exceeded, the suffix would have been `.partN.drama.txt`. That suffix is
this repo's invention; `damn` has no full-essay multi-chunk precedent, only
2-minute pilots.)

## Content fidelity — checked, not asserted

Every script is diffed against its source after removing only the `//`
headers, `<|speaker:0|>`, the voice-profile line and every `[cue]`, with both
sides run through the identical markdown strip. **9/9 verbatim.**

Two rounds were needed and the second one is the honest note: the first
version appended a full stop to each spoken heading (`The exam` → `The exam.`).
That was a character nobody wrote. `build.py` no longer does it, and the audit
above is what proves it. Re-run it after any rebuild:

    python3 - <<'EOF'   # compare source body to script body, token for token
    # (full checker: strip headers + cues from the script, markdown-strip both,
    #  normalise quotes/whitespace, assert string equality)
    EOF

No sentence, aside, capital or typo has ever been moved, added or removed.

## Validation status

`python3 damn/fish/validate.py <each file>` — **ALL SHIPPABLE**, 0 blocks,
$0 spent, no API calls. Exit 0.

15 warnings, three classes, all in the source text and all left alone:

| Class | Count | Examples | Why it stays |
|---|---:|---|---|
| `parentheticals` | 8 | `(SN 15.1)`, `(MN 9)`, `(AN 3.86 and parallels)`, `(Magandiya)`, `(is that metal?)`, `(yes this is a confession)` | Verbatim rule. The citation ones are **essay-stage work** — inline source parentheticals should come out of `ESSAY.md`, not be silently cut here. Owner's asides stay by definition. |
| `long-sentences` | 6 | ramble run-ons, the "apply the same logic to every tug…" line | Same reason. This is `C2: Sentence Architecture` in `gradingsystem.md` — an essay-round fix, not a script-round fix. |
| `caps-words` | 2 | `THIS` ×2 in `samsara1` | Owner's caps. Kept. |

## Voice

All nine use `<|speaker:0|>` (mono — matches 48 of the 104 scripts in `damn`)
with a **stand-in** profile:

- essays → `[calm, measured storyteller voice, slow and gentle for sleep]`
- rambles → `[warm companion voice, settling, like a friend on the sofa]`

Both are real tags already in use in `damn`, chosen for register, and they are
**stand-ins, recast at voice lock** per `damn/voices/registry.md`. One
narrator voice per project, never shared across projects.

## Open slots — deliberately not filled

1. **No goodnight.** `BEATS.md` universal beat 6 is a house sign-off ritual,
   same words every episode. Thomas has none. Each script ends on its own
   closing — samsara on *"have you seen nibbana?"*. Write the ritual in your
   own words and it drops in; an agent cannot supply it.
2. **No cold open was invented.** Every script opens on the source text's own
   first line, which is already a question in both essays' case.
3. **`script:` is not an AGENTS.md stage prefix** (`ramble: review: resources:
   essay: video:`). This folder needed one. Flagged, not added — `AGENTS.md`
   is the other session's file.

## Rebuilding

```
python3 scripts/build.py
```

Deterministic: regenerates all nine from `rambles/*.md` and
`essays/*/*.md`. Run it after any essay round, then re-validate:

```
python3 /root/damn/fish/validate.py scripts/rambles/*.drama.txt scripts/essays/*/*.drama.txt
```
