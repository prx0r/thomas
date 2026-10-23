# thomas — working method

Every piece in this repo moves through the same three stages, in order.
Do not skip a stage.

## The pipeline: ramble → essay → video

1. **Ramble** (`rambles/<topic>1.md`, then `<topic>2.md` for follow-ups).
   Raw thought stream, written in order as it comes, typos and all.
   Its job is to expose the author's misunderstanding, not to be correct.
   Never edit a ramble after the essay stage starts — write a new numbered
   ramble instead, so the process stays visible.

2. **Formal essay** (`essays/<topic>/`).
   The ramble formalised into a coherent peer-reviewed essay.
   - `REVIEW.md` — claim-by-claim review of the ramble: keep / cut / fix.
   - `RESOURCES.md` — every primary source the essay needs, keyed to essay
     beats: sutta refs by standard numbering, verbatim quotes with provenance,
     verification status for each (verified local text, verified public
     translation, needs fetching). No uncited doctrinal claims survive this stage.
   - `ESSAY.md` — the draft itself, in the author's voice, with citations.
   - Dangerous errors flagged in review must be fixed in the draft, not
     carried over. Live scholarly seams (where sources disagree) stay visible,
     never smoothed over.

3. **Video** (`videos/<topic>/` when a piece gets there).
   Script + storyboard + reads, compiled only from the essay stage, never
   straight from the ramble. Every read-aloud quote traces back to
   `RESOURCES.md`. Owner's original analogies and lines stay in owner's voice.

## Repo rules

- One topic per folder under `essays/` and `videos/` (e.g. `samsara`, `nibbana`).
- Rambles are append-only history. Essays are living documents.
- Quotes: verbatim with source. Owner's own lines stay owner's — never dress
  them as textual, never dress textual claims as owner's.
- Commit messages name the stage: "ramble:", "review:", "resources:", "essay:", "video:".

## Owner's axiom — verbatim, do not paraphrase or tidy

The following is the owner's own wording, saved word for word. It overrides
any conflicting habit above. Never rewrite it, never summarise it:

yeah i think also worth nothing like guidelines for all of iit and what each process is doing. ramble is basically me outputting my own intuitions about the topic, the essay is the formalisation and fact chcking and refercing and sourcing and the video is that same thing mamde consumable and memorable, at all times we try to preserve my original wording , aiming not to rewrite but edit and rearrange supplementing with quotes from masters and direct knowlegde at no point should you be writing words yourself or summarising. the only way to prevent slop is to not write in the first place. this i teh axiom you stick by. instead you find the words of a specialist and arrange it so it makes sense. if you cannot do this well ask me before writing , i would ratehr have a sequence of satemtns that fit oddly together than something written by you..
