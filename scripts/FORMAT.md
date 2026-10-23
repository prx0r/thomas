# Directing the free model (house guide — researched 2026-10-14)

Free model = S2 family (`s2.1-pro-free`). Brackets are NOT control tokens — the
model learned implicit mappings from massive data, so placement is meaning and
plain language wins. Sources: Fish emotion docs, S2 inline-tag guides, fish-speech
open-weights repo (self-host path later).

## Core rules

1. **Tag immediately before what it affects.** It applies from that point until the
   next tag or end of sentence. `[whispering] I didn't want to go inside.` whispers
   all of it; `I didn't want to go [whispering] inside.` whispers only "inside".
2. **Pair physical + emotion.** `[whispering]` alone can feel flat; add feeling:
   `[whispering] [scared] Don't move.` / `[sigh] [sad] I miss you.`
3. **Always follow a tag with text.** A tag with nothing after it does nothing.
4. **One primary emotion per sentence, max 3 tags.** Space changes out; never stack
   conflicts.
5. **Sentence-level cues at sentence start; sounds anywhere** (`[sigh]`, `[gasp]`,
   `[pause]` mid-line are the most useful tags in the building).
6. **Intensity modifiers work**: `[slightly sad]`, `[very excited]`, `[slowly]`,
   `[soft voice]`, `[low voice]`, `[warm and happy]`. Free-form generalizes.

## Well-tested tags (use these first)

Breath: `[pause] [short pause] [long pause] [shaky breath] [sigh] [gasp] [inhale] [exhale]`
Voice: `[whispering] [soft voice] [low voice] [slowly] [calm] [relaxed] [warm and happy]`
Feeling: `[sad] [moved] [empathetic] [nostalgic] [lonely] [grateful] [curious] [hopeful]`
Banned for sleep: shouting, screaming, hysterical (blows the bed mix).

## House example (free-native — no paired tags, those are Drama-only)

```
<|speaker:0|>[calm, measured storyteller voice, slow and gentle for sleep] In a village of Musashi Province, there lived two woodcutters.
<|speaker:1|>[bending lower, breath like faint smoke] [whispering] You are a pretty boy, Minokichi... [voice drops to whisper] Remember what I say!
```

## Knobs

- `temperature`/`top_p` 0.7 defaults are fine; lower (0.3–0.5) = steadier narrator, higher = more varied takes. Take 2-3, keep one.
- Multi-speaker: `reference_id` array + `<|speaker:N|>` turns, one request per scene (S2-native, works free).
- `normalize: true`, `latency: normal`, speed 0.8–0.85, ≤15k bytes/call.
- Header `model: s2.1-pro-free` — the ONLY model (free-only law).

## Later (not now)

fish-speech open weights = self-host S2 free-forever fallback. Drama paired tags stay forbidden in-house until/unless the free tier gains them.
