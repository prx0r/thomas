# Becoming an Angel — the version lineage

The one essay in this archive with a recoverable history. **No file is named
`v1` / `v2` / `v3`** — those labels below are ours, assigned by artefact.
Only the last two carry `_v6` in the name, in the file itself.

Source: Angela Voss, *Becoming an Angel: the mundus imaginalis*. All four are
`type: condensed_source`, `author: Angela Voss`.

---

## The four stages

| Stage | File | Bytes | Blocks | Words | Title | New at this stage |
|---|---|---:|---:|---:|---|---|
| **1** | `workengestation/output/essays/general/outputs/becoming_an_angel.json` | 15,378 | **27** | 2,160 | Becoming an Angel: The Mundus Imaginalis and the Platonic Path of Self-Knowledge | base. `body` + `audioUrl`. Strict `ai`/`source` ping-pong. **No `art`, no `phases`.** |
| **2** | `workengestation/output/essays/general/glossary-essays/becoming_an_angel.json` | 18,140 | **33** | 2,397 | *(same as 1)* | **`art` + `phases` arrive.** 5 `art` blocks inserted. **+6 blocks, +237 words** — the expansion. |
| **3** | `workengestation/output/essays/general/glossary-essays/becoming_an_angel_beautiful_edition_v6.json` | 15,779 | 33 | **1,991** | **Becoming an Angel — Beautiful Edition v6** | retitled. **Tightened by 406 words (−17%)** vs stage 2. Keeps `art`, `phases`, `audioUrl`. |
| **6** | `oldessays/essaygen/workshop/v6_final/becoming_an_angel_beautiful_edition_v6.json` | 15,603 | 33 | 2,044 | *(same as 3)* | final workshop copy. `phases` and `audioUrl` **stripped**, `art` kept. +53 words vs stage 3. |

Only stage 6 is inside `oldessays/`. Stages 1–3 live in
`workengestation/output/essays/general/` — paths above are exact.

**Stage 6 is the canonical deploy copy:** md5 `a38afae7…` matches
`workengestation/output/essays/general/workshop-v6/…` byte for byte.

---

## What actually changed

**1 → 2 is the real edit.** Six blocks appended (27 → 33), and five `art`
blocks threaded through the body. The closing section added is Corbin:

> Corbin defines himma as "the act of meditating, conceiving, imagining,
> projecting, ardently desiring. It is the force of an intention so powerful
> as t…"

> "To those who have cultivated the direction of affective force through
> longing and desire, the Angel will reveal itself, often in an intensely
> private…"

> "Voss places Corbin within the lineage of Platonic interpreters that runs
> from Plotinus and Iamblichus through to Jung and Hillman."

> "The importance of Corbin's work cannot be overestimated in a world which
> is blinkered and starved of a sense of the sacred…"

**2 → 3 is the cut.** Same 33 blocks, −406 words, retitle to *Beautiful
Edition*. The compression is the craft step: the essay gets its name and
loses a sixth of its length.

**3 → 6 is packaging.** `phases` and `audioUrl` dropped for the workshop,
`art` retained, ±50 words of reflow. Not a rewrite.

**Block-kind pattern:** stage 1 is pure `ai`/`source` alternation with one
`summary`. Stages 2+ interleave `art` at six positions — the visual layer
arrives with the expansion and stays through every later cut.

---

## The only genuine two-version pair

If you want a real A/B rather than an inferred lineage, this is the one:

| File | Bytes | md5 |
|---|---:|---|
| `oldessays/essaygen/workshop/ficino_world_living_book_v2.json` | 4,736 | `922e9272…` |
| `oldessays/essaygen/workshop/ficino_world_living_book_v6.json` | 5,157 | `f3d71930…` |

Both in `oldessays/essaygen/workshop/`. Different content, different sizes —
the only `*_vN.json` in this archive that is not `_v6`.

---

## Why no v1/v2/v3 survive

`workengestation`, `.meta` and `blog` are **not git repositories**, so there
is no commit history to recover earlier drafts from. The five staging dirs
that would have held them — `essaygen/workshop/{imaginal, theurgy, ficino,
corbin, goethe}_essays/` — exist but are **empty**. Earlier drafts were
overwritten in place; only essays someone thought to `_v6`-rename kept a
trace, and only `ficino_world_living_book` kept a pre-v6 one.

**Lesson for thomas:** the ramble → essay pipeline solves exactly this.
Rambles are append-only and versioned in git from now on, so the lineage
stops being reconstructable and starts being a log.
