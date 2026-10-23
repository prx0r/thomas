# thomas — working method

## Layout — four folders, nothing else at top level

- `rambles/` — the raw material. Owner's thought stream, typos and all.
- `essays/<topic>/` — one folder per ramble title (`samsara`, `nibbana`,
  `rebirth`). Holds every version plus review, resources and process notes.
- `audio/<topic>/` — same topics. Holds the two renders when they exist:
  `<topic>1.mp3` (the ramble) + `ESSAY.mp3` (the chosen final essay).
- `other/` — everything else: `resources/`, `scripts/`, `skills/`,
  `oldessays/`. Tooling and archive, never the piece itself.

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
      `ESSAY.md` is always the latest working draft. Each finished iteration is
      also frozen as a numbered snapshot beside it — `<topic>essayai1.md`,
      then `ai2`, `ai3` — mirroring the ramble names (`samsara1`,
      `nibbana1`). Snapshots are never edited; new rounds write a new number
      until the owner picks the one they like.
   - Dangerous errors flagged in review must be fixed in the draft, not
     carried over. Live scholarly seams (where sources disagree) stay visible,
     never smoothed over.

3. **Video / audio** (`audio/<topic>/` when a piece gets there).
   Script + storyboard + reads, compiled only from the essay stage, never
   straight from the ramble. Every read-aloud quote traces back to
   `RESOURCES.md`. Owner's original analogies and lines stay in owner's voice.
   `ESSAY.md` is the chosen final by definition — it alone renders as
   `audio/<topic>/ESSAY.mp3`, alongside the ramble as
   `audio/<topic>/<topic>1.mp3`.

## Repo rules

- One topic per folder under `essays/` and `audio/` (e.g. `samsara`, `nibbana`).
  Folder names match the ramble titles: `rambles/samsara1.md` → `essays/samsara/` → `audio/samsara/`.
- Rambles are append-only history. Essays are living documents.
- Quotes: verbatim with source. Owner's own lines stay owner's — never dress
  them as textual, never dress textual claims as owner's.
- Commit messages name the stage: "ramble:", "review:", "resources:", "essay:", "video:".

## Owner's axiom — verbatim, do not paraphrase or tidy

The following is the owner's own wording, saved word for word. It overrides
any conflicting habit above. Never rewrite it, never summarise it:

yeah i think also worth nothing like guidelines for all of iit and what each process is doing. ramble is basically me outputting my own intuitions about the topic, the essay is the formalisation and fact chcking and refercing and sourcing and the video is that same thing mamde consumable and memorable, at all times we try to preserve my original wording , aiming not to rewrite but edit and rearrange supplementing with quotes from masters and direct knowlegde at no point should you be writing words yourself or summarising. the only way to prevent slop is to not write in the first place. this i teh axiom you stick by. instead you find the words of a specialist and arrange it so it makes sense. if you cannot do this well ask me before writing , i would ratehr have a sequence of satemtns that fit oddly together than something written by you..

## Referencing — enforced

- `other/resources/` is the shared library (see `other/resources/README.md`). Essay
  `RESOURCES.md` files draw from these shelves; nothing is cited in an essay
  that is not first shelved with provenance.
- Every essay ends with a references section listing each shelf item it
  actually used (e.g. N4, NN1, A2, S2). A reference not cited in the text is
  removed; a citation without a shelf entry is forbidden.
- Quotes stay short and verbatim with source. Owner's analogies and verdicts
  stay owner's voice and are never presented as textual positions.

## Plain English — the house rule

- Rambles use no Buddhist jargon. That is their great strength and it is
  load-bearing: the piece must stay thinkable by someone with no Pali and no
  background. Jargon never leaks upstream into a ramble to sound learned.
- Every specialist quote used in an essay or video is followed by a plain
  English rendering in the owner's register. Pattern: quote verbatim with
  source, then say what it means as the owner would say it to a friend.
  The quote proves it; the rendering makes it land.
- Pali terms appear only alongside their plain rendering on first use
  (e.g. going round, not bare samsarana), and the rendering carries the
  sentence thereafter. No term is ever left standing unexplained.
- If a quote cannot be rendered plainly without distorting it, do not paraphrase
  it away — keep the quote, mark the difficulty openly, ask the owner.

## The continual loop — how we work

- The owner writes an essay ramble. The agent answers with the actual
  mechanisms: staying on the exact content of that essay, explaining and
  correcting it using the actual explanations the masters give.
- Not verbatim unpacking of the full discourse. The master's words are brought
  in only where the essay's claim needs them — to confirm, correct, or deepen
  that exact point — then rendered plain.
- Then the owner writes another essay and the agent corrects again. Continual
  process: ramble, mechanisms, ramble, mechanisms. Each round leaves the repo
  further along: new REVIEW.md, extended RESOURCES.md and shelves, new ESSAY.md.
- After every essay snapshot, the agent writes PROCESS-ai<N>.md beside it:
  what was kept from the ramble and why, which resources carried which beats,
  what was deliberately NOT done and why, a references-vs-body honesty audit,
  and the sharpening queue for the next round. No essay ships without its
  process record.

## Sculpting loop — essay, process, essay (with pushing)

- The unit of work is a round, not a draft. Each round: write the essay
  snapshot (`<topic>essayai<N>.md`), then document the process
  (`PROCESS-ai<N>.md`), then write the next essay. Repeat until the essay is
  sufficiently sculpted from the raw material of the ramble — the owner calls
  the stop, never the agent.
- Sculpting means removal and arrangement, not addition. Each round should
  leave the piece shorter or denser, never padded. If a round cannot improve
  on the last, say so and stop.
- Every round applies the pushing method, adapted from the gochema pushing
  work (`pushing-tantraloka`, Logicvid sessions) and the excavation skill's
  three passes (extract, verify against source, hunt holes):
  1. Verify against the sources — re-read the cited passages, check quotes
     exact, check what the shelves hold that the essay did not use.
  2. Push each essay claim with "why?" and answer only from the masters'
     texts, never from the agent's own frameworks. Frameworks may supply the
     questioning; the answers must come from the quoted sources.
  3. Store the full passage where the answer came from (more than needed),
     so the next round can re-read and re-push it.
  4. Mark the frontier honestly in PROCESS — what the texts assert but do not
     argue, what remains asserted-not-proven. Never smooth a frontier into a
     conclusion.
  5. Hunt holes — what the ramble or the shelves contain that the essay
     ignored, and either use it next round or record why not.
- The sharpening queue in PROCESS-ai<N>.md is the work order for ai<N+1>.
  A round is done when its queue is written, not when the essay is perfect.

## Pushing — adapted from the gochema pushing work

- Source method: `pushing-tantraloka/` (35 Logicvid sessions hounding the
  Tantraloka), `pushing-ipvv/` (10 sessions on Abhinavagupta's IPVV commentary,
  run even closer to the text's own structure), `pushing/` method layer
  (PUSHING_GUIDE, AUTONOMOUS_PUSHING_AGENT_SPEC). Full machinery lives there;
  this repo takes only the portable habits below. Do not import the formal
  apparatus (truth-packets, proof engine, claim-strength tags).
- The one rule, unchanged: hound the text with "why" and force its OWN
  reasoning out. Frameworks supply only the questioning; answers come from
  the masters' texts. Each essay claim that leans on a source must be
  pushable back to a quoted passage.
- Question DNA for each round (adapt the shape, not the content): start from
  the text's own primitive, not a modern term; interrogate words assumed
  identical; find the quantifier/scope leap; push the load-bearing step's why;
  name the hidden premise; play the strongest opponent head-on (the
  relabelling accusation — poetic description is not mechanism); separate
  what the text licenses from what it does not; end every penetration with
  the next forced question, never a dead end.
- Penetration marking: where a source asserts but does not prove, mark it in
  PROCESS as frontier, not as conclusion. The essay may use the frontier only
  flagged as such.
- Destroy pass: before finishing any ESSAY.md, run one hostile re-read whose
  only job is to break it — unsupported entailments, conflated levels,
  translation dependence, passages that resist, rival readings. Repair only
  what survives. Record the kills in PROCESS.
- The destroy pass follows `other/skills/essay-sharpening/SKILL.md` (adapted from
  the gochema pushing work — Logicvid sessions, PUSHING_GUIDE, agent spec —
  without the formal apparatus). Sharpen metaphors to their logical ends;
  grade claims proven/supported/plausible/asserted in PROCESS, never in prose.
- Licensed-vs-unlicensed is the honesty check on every borrowed claim: state
  what the passage licenses and what it does not, in the same breath.
- Branch footer: end every essay with open branches plus the next forced
  question, never a closed conclusion. A piece that terminates is a piece
  that overclaimed.
- Hypothesis phrasing for cross-tradition or cross-text claims: write
  "hypothesis: X ≡ Y", never "X is Y". Similarity is a probe, not an identity.
- No new primitive (a term like samsara, self, time used as if explained)
  unless two or more independent passes force it. Keep ancestry on reused
  terms: what is X (from Ñāṇavīra) vs (from Ñāṇananda) stays visibly sourced.
- The agent works the queue autonomously once set. Owner interruptions
  redirect; otherwise keep moving piece to piece.
