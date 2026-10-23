# oldessays — essay-workstation archive

Imported verbatim from `projects/.meta/misc/essay-workstation` on 2026-10-23.
This is the pre-thomas essay estate: the algorithms, the grading system,
the v6 workshop essays, exemplar analyses, blueprints, thumbnails and art.

## Verification

- files: **577** · bytes: **258,276,508**
- md5 of full tree (path+content, sorted): `0189428cb97045e71aa51d49fddfb464`
- compared against source: **0 missing, 0 differing** (per-file md5)
- source and destination file counts identical

## What is here

| dir | files | size | what |
|---|---:|---:|---|
| `review-images/` | 129 | 144.7 MB | art reference plates (Met / Cleveland / Blake / Plotinus…) |
| `thumbnails/` | 277 | 44.6 MB | one JPG per essay across every collection |
| `exemplars/` | 28 | 38.3 MB | analyses of other people's gold-standard essays (Watts, Nisargadatta, Anandamayi Ma, Jesus in the Himalayas, Academy of Ideas, eternalised-shadow) |
| `blueprints-copy/` | 22 | 15.0 MB | source books as .md (Ficino Platonic Theology vols 1–6, Enneads, Fusus al-Hikam, Avicenna) |
| `essaygen/` | 97 | 1.0 MB | the machinery — v6/v7 algorithms, gradingsystem.md, antislop, perfectessay, longform-algorithm + all workshop essay JSONs |
| `blueprints/` | 7 | 0.8 MB | per-collection blueprint/thesis plans |
| `thumbnail-matches.json/` | 1 | 0.8 MB |  |
| `review-bundle.json/` | 1 | 0.7 MB |  |
| `thumbnail-review.html/` | 1 | 0.3 MB |  |
| `audio/` | 2 | 0.1 MB | narrated sample (Plotinus Ennead 01, mp3 + m4a) |
| `essay-studio/` | 8 | 0.1 MB | studio state + scripts |
| `thumbnail-ranks.json/` | 1 | 0.0 MB |  |
| `README.md/` | 1 | 0.0 MB |  |
| `TEMPLATES.md/` | 1 | 0.0 MB |  |
| `essay-studio-state.json/` | 1 | 0.0 MB |  |
| `README.md` | 1 | 8 KB | |
| `TEMPLATES.md` | 1 | 5 KB | |
| `essay-studio-state.json` | 1 | 1 KB | |
| `review-bundle.json` | 1 | 681 KB | |
| `thumbnail-matches.json` | 1 | 794 KB | |
| `thumbnail-ranks.json` | 1 | 22 KB | |
| `thumbnail-review.html` | 1 | 328 KB | |

## Not imported — 4 exemplar videos lost

Four `.mp4` symlinks under `exemplars/*/video/` pointed at
`/root/projects/blog/exemplars/gold-standards/…`. `projects/blog` is emptied
(local path absent, volume copy contains only the directory itself), so the
targets are gone. Dangling links were dropped rather than committed:

```
exemplars/nisargadatta/video/The Unbelievable Life Of Nisargadatta Maharaj [ynjFKMNwZgw].mp4
exemplars/alan-watts/video/The Bizarre Life of Alan Watts [T6lRcGxH-Mc].mp4
exemplars/jesus-himalayas/video/Jesus in the Himalayas： The Greatest Story Never Told [2U63TVKMgow].mp4
exemplars/anandamayi-ma/video/The Bizarre Life Of Sri Anandamayi Ma [fSUI4Sn-hr4].mp4
```

Everything else in those folders (analysis JSON, transcripts, frames) is present.

## Extension-less text files (14) — easy to miss

Fourteen substantive `.md`-equivalent files carry **no extension**, so
extension filters skip them silently. They are not directories.

**Collection dumps** — `essaygen/workshop/{corbin,ficino,goethe,imaginal,theurgy}_essays`
The full essay sets for those five workshops, concatenated into one file each
(e.g. `corbin_essays` 81,919 B opens on ʿAṭṭār's birds; `ficino_essays` likewise).

**Blueprint companions** — `blueprints{,-copy}/{buddhism,imaginal,occult,platonic,tantra} blueprints`
Access-status and coverage blueprints per tradition, e.g. the Ñāṇananda
*Nibbāna: The Mind Stilled* free-distribution blueprint (111,673 B).

Sizes in the full listing below are authoritative; check there for the rest.

## Redacted before commit

Three scripts carried **hardcoded API keys used as environment-variable
fallbacks**. GitHub secret-scanning declined two push attempts on these.

**1. `oldessays/essaygen/generate-long-essay.mjs` and
`oldessays/essaygen/process-source.mjs`** — DeepSeek:

```js
const API_KEY = process.env.DEEPSEEK_API_KEY || "<key>"
```

**2. `oldessays/essay-studio/rank-thumbnails.py` (line 22)** — Google AI
Studio, caught by the second push:

```py
API_KEY = os.environ.get("GOOGLE_API_KEY", "AQ.…")
```

Both literals replaced with `sk-REDACTED-BEFORE-COMMIT` /
`AQ.REDACTED-BEFORE-COMMIT`. The `environ.get(...)` paths are untouched, so
all three scripts work normally when the variables are set.

Full-repo rescan is now broad enough to catch the shape that slipped past
first time — any `environ.get(env, "<literal>")` / `os.getenv` fallback, plus
`AQ.`, `AIza`, `sk-`, `hf_`, `gh[pousr]_`, `github_pat_`, `AKIA`, Slack `xox*`,
`Bearer <lit>`, `api_key=`/`token=`/`client_secret=` assignments and
private-key blocks: **clean**.

The originals still hold live keys at
`projects/.meta/misc/essay-workstation/` — **rotate all three** if that box
is not the only holder.

## Start here

- `essaygen/workshop/v6_final/gradingsystem.md` — the v6 grading rubric
- `essaygen/v6algorithm.md`, `essaygen/v7algorithm.md`, `essaygen/antislop.md`
- `essaygen/workshop/v6_final/` — the 32 v6 essays + rubric
- `BECOMING-ANGEL-VERSIONS.md` — the only essay with a recoverable lineage
- `README.md`, `TEMPLATES.md` — the workstation's own docs

## Full file listing

| bytes | path |
|---:|---|
| 8,320 | `README.md` |
| 4,994 | `TEMPLATES.md` |
| 65,302 | `audio/plotinus-enneads/01-the-self-that-is-not-the-body.m4a` |
| 65,088 | `audio/plotinus-enneads/01-the-self-that-is-not-the-body.mp3` |
| 111,673 | `blueprints-copy/buddhism blueprints` |
| 215,144 | `blueprints-copy/imaginal blueprints` |
| 175,919 | `blueprints-copy/occult blueprints` |
| 1,187,715 | `blueprints-copy/source_texts/Avicenna and the Visionary Recital_ (Mythos Series) -- Corbin, Henry -- Bollingen Series (General); .txt` |
| 1,211,750 | `blueprints-copy/source_texts/Fusus Al-Hikam_ Ismail Hakki Bursevi’s Translation and -- Ibn al-Arabi, Ismail Hakki Bursevi -- 1-4, 1986 -- Muhyiddin Ibn ’Arabi Society -- isbn13 9780950952710 -- a890b2d6a616ca432fd9763897cfd4f4 -- Anna’s Archive.md` |
| 589,821 | `blueprints-copy/source_texts/Ibn al-ʿArabī’s Fuṣūṣ Al-Ḥikam_ An Annotated Translation of -- Ibn al-Ê»ArabiÌ#x84;; Binyamin Abra.txt` |
| 589,821 | `blueprints-copy/source_texts/Ibn al-ʿArabī’s Fuṣūṣ Al-Ḥikam_ An Annotated Translation of -- Ibn al-Ê»ArabiÌ.txt` |
| 667,211 | `blueprints-copy/source_texts/Platonic Theology, Volume 1_ Books I–IV (The I Tatti -- Marsilio Ficino; English translation by Michael J_B_ Allen -- I Tatti Renaissance library, 2, -- isbn13 9780674003453 -- fbe3aa243367b91f3e3d872387c8f4da -- Anna’s Ar.md` |
| 727,928 | `blueprints-copy/source_texts/Platonic Theology, Volume 2_ Books V–VIII (The I Tatti -- Marsilio Ficino; Latin text edited by James Hankins with -- I Tatti Renaissance Library, -- isbn13 9780674003453 -- 3ca6cbc090645c74a074a95e900a68b0 -- Anna’s Archi.md` |
| 684,341 | `blueprints-copy/source_texts/Platonic Theology, Volume 3_ Books IX–XI (The I Tatti -- Marsilio Ficino; Latin text edited by James Hankins with -- 1ST, 2003 -- The I Tatti -- isbn13 9780674003453 -- 497370db1dffdf6a06be564c124ab66a -- Anna’s Archive.md` |
| 697,147 | `blueprints-copy/source_texts/Platonic Theology, Volume 4_ Books XII–XIV (The I Tatti -- Marsilio Ficino; Latin text edited by James Hankins with -- I Tatti Renaissance Library, 4, -- isbn13 9780674003453 -- 0dbe58db67a7a6df2bcedce5a2f4c60b -- Anna’s A.md` |
| 683,013 | `blueprints-copy/source_texts/Platonic Theology, Volume 5, Books XV-XVI (The I Tatti -- Marsilio Ficino; Latin text edited by James Hankins with -- (I Tatti Renaissance Library), -- isbn13 9780674003453 -- f1ddd8ee1b09be00f94021e135b41ee5 -- Anna’s Archi.md` |
| 730,513 | `blueprints-copy/source_texts/Platonic Theology, Volume 6_ Books XVII–XVIII (The I Tatti -- Marsilio Ficino; Latin text edited by James Hankins with -- I Tatti Renaissance Library, -- isbn13 9780674003453 -- 9aa0d3f3f30db8afe9f19f13fa732c74 -- Anna’s A.md` |
| 2,419,886 | `blueprints-copy/source_texts/The Enneads_ Second Edition -- Lloyd P_ Gerson (editor and translator); George Boys-Stones -- 2nd, 2025 -- Cambridge University Press -- isbn13 9781009604970 -- 4643160c84a5bdb030e8da5c67a11668 -- Anna’s Archive.md` |
| 354,899 | `blueprints-copy/source_texts/agrippa-book3.txt` |
| 970,009 | `blueprints-copy/source_texts/agrippa-books1-2.txt` |
| 512,004 | `blueprints-copy/source_texts/agrippa-complete.txt` |
| 1,211,750 | `blueprints-copy/source_texts/avicenna.md` |
| 331,450 | `blueprints-copy/source_texts/holy-daimon.txt` |
| 513,885 | `blueprints-copy/source_texts/man-of-light.txt` |
| 977,111 | `blueprints-copy/source_texts/swedenborg-heaven-and-hell.txt` |
| 129,062 | `blueprints-copy/tantra blueprints` |
| 1,683 | `blueprints/DEPLOY_NOTES.md` |
| 111,673 | `blueprints/buddhism blueprints` |
| 10,261 | `blueprints/handover.md` |
| 215,144 | `blueprints/imaginal blueprints` |
| 175,919 | `blueprints/occult blueprints` |
| 204,379 | `blueprints/platonic blueprints` |
| 129,062 | `blueprints/tantra blueprints` |
| 914 | `essay-studio-state.json` |
| 3,527 | `essay-studio/build-review-bundle.py` |
| 3,465 | `essay-studio/build-review-page.py` |
| 20,101 | `essay-studio/essay-studio.py` |
| 4,658 | `essay-studio/learn-profile.py` |
| 10,041 | `essay-studio/match-thumbnails.py` |
| 4,953 | `essay-studio/rank-thumbnails.py` |
| 3,520 | `essay-studio/render-thumbnails.py` |
| 9,959 | `essay-studio/taste-server.py` |
| 10,434 | `essaygen/algorithm-upgrade.md` |
| 3,167 | `essaygen/antislop.md` |
| 7,582 | `essaygen/antislopguide.md` |
| 24,177 | `essaygen/author.md` |
| 20,463 | `essaygen/claude5.md` |
| 10,351 | `essaygen/companion-writing-guide.md` |
| 17,947 | `essaygen/essaygenaudit.md` |
| 12,103 | `essaygen/essayguide.md` |
| 5,279 | `essaygen/essayprocess.md` |
| 4,163 | `essaygen/essaywriter.md` |
| 3,231 | `essaygen/ficinoextraction.md` |
| 5,622 | `essaygen/generate-long-essay.mjs` |
| 4,832 | `essaygen/issuesessay.md` |
| 13,707 | `essaygen/longform-algorithm.md` |
| 6,833 | `essaygen/newgraph.md` |
| 5,326 | `essaygen/perfectessay.md` |
| 8,132 | `essaygen/process-source.mjs` |
| 76,314 | `essaygen/references/antislop_paper_arxiv_2510.15061.txt` |
| 28,560 | `essaygen/rumiengine.md` |
| 10,236 | `essaygen/sourceextraction.md` |
| 10,701 | `essaygen/sourcematerialextraction.md` |
| 8,363 | `essaygen/thesisaudio.md` |
| 12,704 | `essaygen/thesismaster.md` |
| 36,529 | `essaygen/v6algorithm.md` |
| 24,626 | `essaygen/v7algorithm.md` |
| 3,477 | `essaygen/workshop/corbin_attar_v6.json` |
| 3,298 | `essaygen/workshop/corbin_avicenna_angel_v6.json` |
| 2,856 | `essaygen/workshop/corbin_blake_v6.json` |
| 81,919 | `essaygen/workshop/corbin_essays` |
| 3,114 | `essaygen/workshop/corbin_hillman_v6.json` |
| 3,241 | `essaygen/workshop/corbin_jung_v6.json` |
| 2,836 | `essaygen/workshop/corbin_plotinus_beauty_v6.json` |
| 2,909 | `essaygen/workshop/corbin_steiner_imagination_v6.json` |
| 2,741 | `essaygen/workshop/corbin_swedenborg_v6.json` |
| 3,185 | `essaygen/workshop/ficino_divine_madness_v6.json` |
| 57,601 | `essaygen/workshop/ficino_essays` |
| 3,833 | `essaygen/workshop/ficino_ladder_of_desire_v6.json` |
| 4,074 | `essaygen/workshop/ficino_spiritus_v6.json` |
| 4,363 | `essaygen/workshop/ficino_sunlike_eye_v6.json` |
| 3,267 | `essaygen/workshop/ficino_theurgy_v6.json` |
| 4,736 | `essaygen/workshop/ficino_world_living_book_v2.json` |
| 5,157 | `essaygen/workshop/ficino_world_living_book_v6.json` |
| 3,498 | `essaygen/workshop/goethe_between_light_eye_v6.json` |
| 2,901 | `essaygen/workshop/goethe_colour_edge_v6.json` |
| 72,321 | `essaygen/workshop/goethe_essays` |
| 3,433 | `essaygen/workshop/goethe_exact_sensorial_v6.json` |
| 3,214 | `essaygen/workshop/goethe_eye_restores_thought_v6.json` |
| 3,448 | `essaygen/workshop/goethe_image_without_object_v6.json` |
| 3,669 | `essaygen/workshop/goethe_metamorphosis_phenomena_v6.json` |
| 3,521 | `essaygen/workshop/goethe_organism_whole_v6.json` |
| 3,805 | `essaygen/workshop/goethe_thought_begins_see_v6.json` |
| 20,402 | `essaygen/workshop/imaginal_essays` |
| 3,065 | `essaygen/workshop/theurgy_asclepius_v6.json` |
| 3,391 | `essaygen/workshop/theurgy_chaldean_v6.json` |
| 43,722 | `essaygen/workshop/theurgy_essays` |
| 3,613 | `essaygen/workshop/theurgy_iamblichus_v6.json` |
| 3,223 | `essaygen/workshop/theurgy_plotinus_v6.json` |
| 3,469 | `essaygen/workshop/theurgy_proclus_v6.json` |
| 3,735 | `essaygen/workshop/theurgy_sallustius_v6.json` |
| 15,603 | `essaygen/workshop/v6_final/becoming_an_angel_beautiful_edition_v6.json` |
| 3,477 | `essaygen/workshop/v6_final/corbin_attar_v6.json` |
| 3,298 | `essaygen/workshop/v6_final/corbin_avicenna_angel_v6.json` |
| 2,856 | `essaygen/workshop/v6_final/corbin_blake_v6.json` |
| 12,901 | `essaygen/workshop/v6_final/corbin_creative_imagination_v6.json` |
| 3,114 | `essaygen/workshop/v6_final/corbin_hillman_v6.json` |
| 3,241 | `essaygen/workshop/v6_final/corbin_jung_v6.json` |
| 2,836 | `essaygen/workshop/v6_final/corbin_plotinus_beauty_v6.json` |
| 2,909 | `essaygen/workshop/v6_final/corbin_steiner_imagination_v6.json` |
| 2,741 | `essaygen/workshop/v6_final/corbin_swedenborg_v6.json` |
| 3,185 | `essaygen/workshop/v6_final/ficino_divine_madness_v6.json` |
| 3,833 | `essaygen/workshop/v6_final/ficino_ladder_of_desire_v6.json` |
| 4,074 | `essaygen/workshop/v6_final/ficino_spiritus_v6.json` |
| 4,363 | `essaygen/workshop/v6_final/ficino_sunlike_eye_v6.json` |
| 3,267 | `essaygen/workshop/v6_final/ficino_theurgy_v6.json` |
| 5,157 | `essaygen/workshop/v6_final/ficino_world_living_book_v6.json` |
| 3,498 | `essaygen/workshop/v6_final/goethe_between_light_eye_v6.json` |
| 2,901 | `essaygen/workshop/v6_final/goethe_colour_edge_v6.json` |
| 3,433 | `essaygen/workshop/v6_final/goethe_exact_sensorial_v6.json` |
| 3,214 | `essaygen/workshop/v6_final/goethe_eye_restores_thought_v6.json` |
| 3,448 | `essaygen/workshop/v6_final/goethe_image_without_object_v6.json` |
| 3,669 | `essaygen/workshop/v6_final/goethe_metamorphosis_phenomena_v6.json` |
| 3,521 | `essaygen/workshop/v6_final/goethe_organism_whole_v6.json` |
| 3,805 | `essaygen/workshop/v6_final/goethe_thought_begins_see_v6.json` |
| 15,815 | `essaygen/workshop/v6_final/gradingsystem.md` |
| 14,838 | `essaygen/workshop/v6_final/ibn_arabi_barzakh_v6.json` |
| 11,639 | `essaygen/workshop/v6_final/mundus_handcrafted_v6.json` |
| 3,065 | `essaygen/workshop/v6_final/theurgy_asclepius_v6.json` |
| 3,391 | `essaygen/workshop/v6_final/theurgy_chaldean_v6.json` |
| 3,613 | `essaygen/workshop/v6_final/theurgy_iamblichus_v6.json` |
| 3,223 | `essaygen/workshop/v6_final/theurgy_plotinus_v6.json` |
| 3,469 | `essaygen/workshop/v6_final/theurgy_proclus_v6.json` |
| 3,735 | `essaygen/workshop/v6_final/theurgy_sallustius_v6.json` |
| 9,722 | `essaygen/workshop/v6ficinoanalysis.md` |
| 32,743 | `essaygen/workshop/v6ficinofeedback.md` |
| 6,994 | `essaygen/workshop/workshopalgorithm.md` |
| 15,409 | `essaygen/workshop/workshopguide.md` |
| 25,170 | `essaygen/workshop/workshopprocess.md` |
| 11,376 | `exemplars/academy-of-ideas/transcript/pretend-less-intelligent.txt` |
| 15,494 | `exemplars/academy-of-ideas/transcript/western-worldview.txt` |
| 78,309 | `exemplars/alan-watts/analysis/alan-watts-analysis.json` |
| 76,079 | `exemplars/alan-watts/analysis/full-analysis.json` |
| 71,055 | `exemplars/anandamayi-ma/analysis/anandamayi-analysis.json` |
| 71,055 | `exemplars/anandamayi-ma/analysis/fablecut-analysis.json` |
| 21,675 | `exemplars/anandamayi-ma/transcript/anandamayi_audio.srt` |
| 18,256 | `exemplars/anandamayi-ma/transcript/anandamayi_audio.tsv` |
| 20,091 | `exemplars/anandamayi-ma/transcript/anandamayi_audio.vtt` |
| 91,262 | `exemplars/anandamayi-ma/transcript/transcript.json` |
| 15,833 | `exemplars/anandamayi-ma/transcript/transcript.txt` |
| 741 | `exemplars/eternalised-shadow/download.log` |
| 76,079 | `exemplars/gold-standards/alan-watts-analysis.json` |
| 71,055 | `exemplars/gold-standards/anandamayi-analysis.json` |
| 97,039 | `exemplars/gold-standards/anandamayi-ma-analysis.json` |
| 91,262 | `exemplars/gold-standards/anandamayi_audio.json` |
| 21,675 | `exemplars/gold-standards/anandamayi_audio.srt` |
| 18,256 | `exemplars/gold-standards/anandamayi_audio.tsv` |
| 15,833 | `exemplars/gold-standards/anandamayi_audio.txt` |
| 20,091 | `exemplars/gold-standards/anandamayi_audio.vtt` |
| 38,934,556 | `exemplars/gold-standards/anandamayi_audio.wav` |
| 23,264 | `exemplars/gold-standards/aoi-pretend-less-intelligent-analysis.json` |
| 52,731 | `exemplars/gold-standards/aoi-western-worldview-analysis.json` |
| 80,242 | `exemplars/gold-standards/jesus-himalayas-analysis.json` |
| 57,991 | `exemplars/gold-standards/nisargadatta-analysis.json` |
| 80,242 | `exemplars/jesus-himalayas/analysis/full-analysis.json` |
| 794 | `exemplars/jesus-himalayas/analysis/run.log` |
| 57,991 | `exemplars/nisargadatta/analysis/full-analysis.json` |
| 697,429 | `review-bundle.json` |
| 181,059 | `review-images/A001.jpg` |
| 113,414 | `review-images/A005.jpg` |
| 203,088 | `review-images/A006.jpg` |
| 124,784 | `review-images/A009.jpg` |
| 206,200 | `review-images/A010.jpg` |
| 201,427 | `review-images/A011.jpg` |
| 161,640 | `review-images/A012.jpg` |
| 99,479 | `review-images/A013.jpg` |
| 57,939 | `review-images/A014.jpg` |
| 244,973 | `review-images/A016.jpg` |
| 147,351 | `review-images/A017.jpg` |
| 95,934 | `review-images/A042.jpg` |
| 125,373 | `review-images/A045.jpg` |
| 87,282 | `review-images/A046.jpg` |
| 104,082 | `review-images/A057.jpg` |
| 227,931 | `review-images/A071.jpg` |
| 105,023 | `review-images/A072.jpg` |
| 81,979 | `review-images/A081.jpg` |
| 138,304 | `review-images/A093.jpg` |
| 58,509 | `review-images/A120.jpg` |
| 99,768 | `review-images/A125.jpg` |
| 100,166 | `review-images/A143.jpg` |
| 115,695 | `review-images/A149.jpg` |
| 155,822 | `review-images/A154.jpg` |
| 47,759 | `review-images/A176.jpg` |
| 129,228 | `review-images/A199.jpg` |
| 129,777 | `review-images/A200.jpg` |
| 136,262 | `review-images/A201.jpg` |
| 54,888 | `review-images/A231.jpg` |
| 56,345 | `review-images/A241.jpg` |
| 47,804 | `review-images/A242.jpg` |
| 92,978 | `review-images/A255.jpg` |
| 114,475 | `review-images/A269.jpg` |
| 136,804 | `review-images/A270.jpg` |
| 102,638 | `review-images/A295.jpg` |
| 3,699,435 | `review-images/Baghdad Quran illumination - Suhrawardi.jpg` |
| 143,066 | `review-images/Hermes Siena Cathedral mosaic.jpg` |
| 90,910 | `review-images/Hermes as mage.jpg` |
| 127,447 | `review-images/Ibn Arabi life diagram.jpg` |
| 8,226 | `review-images/Ibn Arabi portrait.jpg` |
| 20,262 | `review-images/Ibn Arabi with students - Persian miniature.jpg` |
| 77,394 | `review-images/Plato in his Academy.png` |
| 69,605 | `review-images/Plotinus Vatican bust.jpg` |
| 66,379 | `review-images/Plotinus marble head.jpg` |
| 39,568 | `review-images/Plotinus with disciples sarcophagus.jpg` |
| 60,324 | `review-images/Proclus commentary on Euclid.jpg` |
| 29,521 | `review-images/angel.jpg` |
| 323,983 | `review-images/art_angel_gabriel.jpg` |
| 3,174,151 | `review-images/art_angel_surush.jpg` |
| 273,888 | `review-images/art_blake_albion_rose.jpg` |
| 215,299 | `review-images/art_cleveland_alhambra_hanging_fragment_with_decorated_bands.jpg` |
| 71,639 | `review-images/art_cleveland_durga_destroying_the_buffalo_demon.jpg` |
| 174,183 | `review-images/art_cleveland_folio_22_from_a_yoga_shastra_of_hemachandra_jain_m.jpg` |
| 163,764 | `review-images/art_cleveland_fragment_with_arcade_and_palmettes.jpg` |
| 601,082 | `review-images/art_cleveland_fragment_with_curving_vine_and_palmette_leaves.jpg` |
| 953,008 | `review-images/art_cleveland_fragmentary_icon_panel_christ_in_glory_and_evangel.jpg` |
| 51,310 | `review-images/art_cleveland_goddess_holding_a_lotus.jpg` |
| 178,225 | `review-images/art_cleveland_kali_on_shiva_from_a_tantric_devi_series.jpg` |
| 135,626 | `review-images/art_cleveland_leaf_from_a_book_of_hours_blank_verso.jpg` |
| 271,398 | `review-images/art_cleveland_leaf_from_a_book_of_hours_the_annunciation.jpg` |
| 228,996 | `review-images/art_cleveland_leaf_from_a_book_of_hours_the_annunciation_recto.jpg` |
| 20,977 | `review-images/art_cleveland_lotus_sutra_with_a_frontispiece.jpg` |
| 167,100 | `review-images/art_cleveland_seated_amitabha_with_attendants.jpg` |
| 211,991 | `review-images/art_cleveland_shamsa_recto_from_right_folio_from_a_double_page_f.jpg` |
| 208,105 | `review-images/art_cleveland_stone_sculptures_in_a_shiva_temple.jpg` |
| 258,696 | `review-images/art_cleveland_text_folio_54_recto_from_a_kalpa_sutra.jpg` |
| 75,575 | `review-images/art_cleveland_the_five_hundred_arhats.jpg` |
| 267,066 | `review-images/art_cleveland_the_white_path_between_two_rivers.jpg` |
| 72,048 | `review-images/art_cleveland_trident_with_shiva_as_half_woman_ardhanarishvara.jpg` |
| 228,156 | `review-images/art_cleveland_zulaykha_in_her_palace_and_as_an_old_woman_with_jo.jpg` |
| 143,066 | `review-images/art_commons_file_hermes_mercurius_trismegistus_siena_cathedral.jpg` |
| 155,009 | `review-images/art_commons_file_ibn_al_arabi_plain_of_assembly_jpg.jpg` |
| 8,226 | `review-images/art_commons_file_ibn_arabi_jpg.jpg` |
| 20,262 | `review-images/art_commons_file_ibn_arabi_with_students_jpg.jpg` |
| 77,394 | `review-images/art_commons_file_plato_i_sin_akademi_av_carl_johan_wahlbom_ur_.png` |
| 66,379 | `review-images/art_commons_file_plotinus_jpg.jpg` |
| 1,294,695 | `review-images/art_commons_file_shiva_s_statue_at_cern_engaging_in_the_natara.jpg` |
| 4,982,785 | `review-images/art_conjunction.jpg` |
| 117,015 | `review-images/art_mandala.jpg` |
| 1,970,156 | `review-images/art_met_battle_scene_from_a_devi_mahatmya.jpg` |
| 14,846,906 | `review-images/art_met_chakrasamvara_and_vajravarahi.jpg` |
| 7,746,597 | `review-images/art_met_chakrasamvara_with_his_consort_vajravarahi.jpg` |
| 2,361,772 | `review-images/art_met_chamunda_the_horrific_destroyer_of_evil.jpg` |
| 3,950,857 | `review-images/art_met_devi_vanquishes_the_demon_nisumbha_and_his_armies_.jpg` |
| 2,340,371 | `review-images/art_met_durga_and_kali_approach_the_gathered_armies_of_cha.jpg` |
| 2,012,405 | `review-images/art_met_durga_kali_and_five_matrikas_battle_the_daitya_arm.jpg` |
| 2,232,648 | `review-images/art_met_durga_kali_and_the_matrikas_battle_the_demon_rakta.jpg` |
| 2,737,503 | `review-images/art_met_goddess_durga_slaying_the_demon_mahisha.jpg` |
| 7,646,818 | `review-images/art_met_hanuman_in_his_tantric_five_headed_pancha_mukha_fo.jpg` |
| 3,171,663 | `review-images/art_met_kali_presenting_the_heads_of_chanda_and_munda_to_d.jpg` |
| 6,466,680 | `review-images/art_met_kamala_and_bhairavi.jpg` |
| 2,160,702 | `review-images/art_met_linga_with_face_of_shiva_ekamukhalinga.jpg` |
| 1,941,400 | `review-images/art_met_mahadevi_the_great_goddess.jpg` |
| 2,427,507 | `review-images/art_met_mandala_of_the_bodhisattva_hannya_prajnaparamita.jpg` |
| 3,484,201 | `review-images/art_met_manuscript_cover_interior_with_mahasiddhas_bodhisa.jpg` |
| 87,253 | `review-images/art_met_plaque_from_a_tantric_ritual_apron.jpg` |
| 874,314 | `review-images/art_met_plaque_from_a_tantric_ritual_apron_chakrasamvara_a.jpg` |
| 1,231,320 | `review-images/art_met_plaque_from_a_tantric_ritual_apron_chitipati_danci.jpg` |
| 148,506 | `review-images/art_met_plaque_from_a_tantric_ritual_apron_kirtimukha.JPG` |
| 89,681 | `review-images/art_met_plaque_from_a_tantric_ritual_apron_representing_ch.jpg` |
| 5,524,772 | `review-images/art_met_plate_with_the_god_chahk.jpg` |
| 150,004 | `review-images/art_met_rondel_with_a_racing_male_deity_cradling_his_conso.jpg` |
| 2,360,977 | `review-images/art_met_sacrificial_knife.jpg` |
| 2,335,291 | `review-images/art_met_section_of_a_diptych_in_linga_form_interior_depict.jpg` |
| 3,748,931 | `review-images/art_met_shiva_and_parvati_playing_chaupar_folio_from_a_ras.jpg` |
| 2,117,725 | `review-images/art_met_shiva_and_parvati_with_their_sons_karttikeya_and_g.jpg` |
| 3,106,862 | `review-images/art_met_shiva_carries_the_corpse_of_sati.jpg` |
| 2,189,516 | `review-images/art_met_shiva_seated_with_parvati.jpg` |
| 1,289,210 | `review-images/art_met_standing_parvati.jpg` |
| 1,712,017 | `review-images/art_met_standing_shiva_or_temple_guardian_dvarapala.jpg` |
| 4,318,977 | `review-images/art_met_tantric_rug_with_two_flayed_male_figures.jpg` |
| 3,111,192 | `review-images/art_met_the_avatar_narasimha.jpg` |
| 3,230,897 | `review-images/art_met_the_goddess_bhairavi_devi_with_shiva.jpg` |
| 2,287,793 | `review-images/art_met_the_half_male_half_female_form_of_shiva_shiva_ardh.jpg` |
| 1,662,105 | `review-images/art_met_the_spiritual_master_padmasambhava.jpg` |
| 4,519,775 | `review-images/art_met_the_wrathful_protector_mahakala_tantric_protective.jpg` |
| 9,053,465 | `review-images/art_met_trowo_tsochog_khagying_the_bon_deity.jpg` |
| 285,060 | `review-images/art_sun_moon.jpg` |
| 2,263 | `review-images/avanteshwara-1868.jpg` |
| 2,263 | `review-images/bakhshali-ms.jpg` |
| 526,639 | `review-images/cropped-william_blake_-_albion_rose_-_from_a_large_book_of_designs_1793-69.jpg` |
| 182,635 | `review-images/iconography-of-the-angels-and-other-bodiless-powers.jpeg` |
| 2,263 | `review-images/martand-1864.jpg` |
| 2,263 | `review-images/martand-sun-temple.jpg` |
| 3,915,917 | `review-images/naranag-temple.jpg` |
| 39,781 | `review-images/nataraja.jpg` |
| 101,503 | `review-images/other-world.jpg` |
| 52,551 | `review-images/self-portrait-with-death.jpg` |
| 61,087 | `review-images/the-angel-1905.jpg` |
| 813,197 | `thumbnail-matches.json` |
| 22,096 | `thumbnail-ranks.json` |
| 335,434 | `thumbnail-review.html` |
| 192,212 | `thumbnails/blog-assembly-essays/01_the_universe_has_two_assembly_lines.jpg` |
| 97,072 | `thumbnails/blog-assembly-essays/02_your_body_may_be_a_pointer_rather_than_a_container.jpg` |
| 198,167 | `thumbnails/blog-assembly-essays/03_your_limits_are_building_the_mind_that_feels_trapped.jpg` |
| 81,517 | `thumbnails/blog-assembly-essays/04_recognition_begins_by_drawing_a_boundary.jpg` |
| 195,827 | `thumbnails/blog-assembly-essays/05_mathematics_gives_life_powers_evolution_never_selected.jpg` |
| 190,918 | `thumbnails/blog-theses/from-matter-to-life-synthesis.jpg` |
| 202,884 | `thumbnails/blog-theses/kirby-urner-synthesis.jpg` |
| 161,002 | `thumbnails/blog-theses/seth-synthesis.jpg` |
| 192,818 | `thumbnails/blog-theses/subtle-body-thesis.jpg` |
| 130,504 | `thumbnails/blog-theses/water-inexternalism-synthesis.jpg` |
| 185,786 | `thumbnails/corbin/01-the-map-the-veil-the-method.jpg` |
| 151,766 | `thumbnails/corbin/02-the-god-who-longs-to-be-known.jpg` |
| 137,947 | `thumbnails/corbin/03-sophia-in-mecca.jpg` |
| 154,009 | `thumbnails/corbin/04-creation-is-not-an-object.jpg` |
| 175,424 | `thumbnails/corbin/05-the-heart-that-makes-worlds-real.jpg` |
| 157,303 | `thumbnails/corbin/06-when-man-prays-god-into-presence.jpg` |
| 154,771 | `thumbnails/corbin/07-the-face-that-cannot-be-seen.jpg` |
| 174,453 | `thumbnails/corbin/_archive-01-angel-who-teaches-soul-to-read.jpg` |
| 154,845 | `thumbnails/expansion-essays-52-56/expansion-essay52.jpg` |
| 169,442 | `thumbnails/expansion-essays-52-56/expansion-essay53.jpg` |
| 243,276 | `thumbnails/expansion-essays-52-56/expansion-essay54.jpg` |
| 84,559 | `thumbnails/expansion-essays-52-56/expansion-essay56.jpg` |
| 149,076 | `thumbnails/expansion-essays/01_a_bit_begins_when_a_difference_can_wound_something.jpg` |
| 187,551 | `thumbnails/expansion-essays/01_desire_is_not_proof_that_you_are_incomplete.jpg` |
| 156,855 | `thumbnails/expansion-essays/01_grace_breaks_the_law_that_brought_you_here.jpg` |
| 84,412 | `thumbnails/expansion-essays/01_knowledge_binds_by_making_the_world_small_enough_to_use.jpg` |
| 191,986 | `thumbnails/expansion-essays/01_life_crosses_barriers_it_cannot_climb.jpg` |
| 191,634 | `thumbnails/expansion-essays/01_look_outward_without_leaving_the_heart.jpg` |
| 132,964 | `thumbnails/expansion-essays/01_pleasure_is_what_happens_when_experience_stops_fighting_itself.jpg` |
| 177,348 | `thumbnails/expansion-essays/01_the_body_can_remember_a_shape_it_is_not_wearing.jpg` |
| 77,993 | `thumbnails/expansion-essays/01_the_goddess_is_not_the_alphabet_but_the_path_through_it.jpg` |
| 102,612 | `thumbnails/expansion-essays/01_the_self_appears_wherever_two_moments_belong_to_one_life.jpg` |
| 190,551 | `thumbnails/expansion-essays/01_the_universe_is_hiding_inside_your_attention.jpg` |
| 158,052 | `thumbnails/expansion-essays/01_the_world_arrives_before_you_name_it.jpg` |
| 124,925 | `thumbnails/expansion-essays/01_your_body_is_the_diagram_your_mind_keeps_redrawing.jpg` |
| 154,390 | `thumbnails/expansion-essays/01_your_voice_existed_before_language.jpg` |
| 186,270 | `thumbnails/expansion-essays/02_a_bird_may_see_the_earths_magnetic_field.jpg` |
| 187,469 | `thumbnails/expansion-essays/02_a_markov_blanket_is_not_the_skin_of_the_self.jpg` |
| 183,837 | `thumbnails/expansion-essays/02_a_tumor_may_be_a_cell_that_forgot_the_body.jpg` |
| 131,599 | `thumbnails/expansion-essays/02_an_organism_survives_by_predicting_itself.jpg` |
| 192,554 | `thumbnails/expansion-essays/02_life_survives_by_never_becoming_fully_stable.jpg` |
| 192,493 | `thumbnails/expansion-essays/02_matter_remembers_by_becoming_easier_to_change_again.jpg` |
| 78,284 | `thumbnails/expansion-essays/02_the_brain_has_an_alphabet_before_it_has_a_thought.jpg` |
| 190,429 | `thumbnails/expansion-essays/02_the_embryo_flashes_before_it_has_a_brain.jpg` |
| 82,083 | `thumbnails/expansion-essays/02_the_place_that_exists_nowhere.jpg` |
| 75,873 | `thumbnails/expansion-essays/02_touch_can_move_the_border_of_the_self.jpg` |
| 190,218 | `thumbnails/expansion-essays/02_you_cannot_manufacture_the_state_the_whole_must_become.jpg` |
| 191,627 | `thumbnails/expansion-essays/02_your_senses_are_already_eating_the_universe.jpg` |
| 77,771 | `thumbnails/expansion-essays/03_a_diagram_becomes_alive_when_it_is_given_a_world.jpg` |
| 189,092 | `thumbnails/expansion-essays/03_awakening_is_not_the_heat_but_what_survives_the_cooling.jpg` |
| 130,897 | `thumbnails/expansion-essays/03_awareness_is_not_inside_the_system_that_predicts_the_world.jpg` |
| 201,583 | `thumbnails/expansion-essays/03_everything_is_trying_to_return.jpg` |
| 117,483 | `thumbnails/expansion-essays/03_matter_remembers_the_gods.jpg` |
| 245,956 | `thumbnails/expansion-essays/03_music_is_medicine_for_the_invisible_body.jpg` |
| 110,041 | `thumbnails/expansion-essays/03_nature_builds_bodies_by_looking_inward.jpg` |
| 174,132 | `thumbnails/expansion-essays/03_part_of_you_never_entered_the_body.jpg` |
| 120,671 | `thumbnails/expansion-essays/03_the_crooked_body_can_reach_forms_the_straight_body_cannot.jpg` |
| 98,281 | `thumbnails/expansion-essays/03_the_soul_needs_a_second_body.jpg` |
| 307,986 | `thumbnails/expansion-essays/03_the_universe_changes_scale_without_changing_its_grammar.jpg` |
| 232,379 | `thumbnails/expansion-essays/03_you_are_what_remains_recognisable_after_the_parts_have_changed.jpg` |
| 156,296 | `thumbnails/expansion-essays/04_a_boundary_can_create_a_person_without_creating_consciousness.jpg` |
| 190,886 | `thumbnails/expansion-essays/04_a_collective_becomes_one_when_its_desires_stop_cancelling_each_other.jpg` |
| 127,033 | `thumbnails/expansion-essays/04_a_mutation_may_begin_when_a_proton_changes_the_alphabet.jpg` |
| 120,815 | `thumbnails/expansion-essays/04_a_symbol_becomes_real_when_several_worlds_compile_to_the_same_form.jpg` |
| 125,994 | `thumbnails/expansion-essays/04_life_is_the_loop_that_makes_the_loop.jpg` |
| 189,233 | `thumbnails/expansion-essays/04_self_and_world_hold_each_other_upright.jpg` |
| 192,175 | `thumbnails/expansion-essays/04_the_dead_were_buried_with_instructions.jpg` |
| 233,180 | `thumbnails/expansion-essays/04_the_fire_is_not_destroying_you.jpg` |
| 302,591 | `thumbnails/expansion-essays/04_the_first_point_becomes_a_body_by_losing_symmetry.jpg` |
| 199,188 | `thumbnails/expansion-essays/04_the_universe_speaks_in_borrowed_voices.jpg` |
| 235,287 | `thumbnails/expansion-essays/04_the_warning_can_become_the_trap.jpg` |
| 189,241 | `thumbnails/expansion-essays/04_you_are_only_one_of_your_possible_selves.jpg` |
| 189,036 | `thumbnails/expansion-essays/05_a_body_may_remember_an_idea.jpg` |
| 185,399 | `thumbnails/expansion-essays/05_a_leaf_uses_noise_to_keep_light_from_getting_lost.jpg` |
| 210,745 | `thumbnails/expansion-essays/05_breath_is_the_clock_the_brain_cannot_ignore.jpg` |
| 129,707 | `thumbnails/expansion-essays/05_fear_is_a_precision_setting_before_it_is_a_story.jpg` |
| 127,047 | `thumbnails/expansion-essays/05_form_needs_a_place_that_has_no_form.jpg` |
| 153,635 | `thumbnails/expansion-essays/05_god_looks_through_your_face.jpg` |
| 188,169 | `thumbnails/expansion-essays/05_sakti_draws_the_line_that_turns_physics_into_information.jpg` |
| 107,294 | `thumbnails/expansion-essays/05_the_future_can_move_you_without_existing_yet.jpg` |
| 187,858 | `thumbnails/expansion-essays/05_the_same_state_can_feel_like_birth_from_one_direction_and_death_from_the_other.jpg` |
| 127,492 | `thumbnails/expansion-essays/05_the_whole_can_act_before_any_part_understands_it.jpg` |
| 130,910 | `thumbnails/expansion-essays/05_time_feels_forward_because_the_present_contains_a_fading_past.jpg` |
| 300,703 | `thumbnails/expansion-essays/05_your_cells_may_be_solving_a_problem_called_you.jpg` |
| 242,499 | `thumbnails/ficino/00-orientation-ficinos-world.jpg` |
| 194,512 | `thumbnails/ficino/01-why-medicine-for-philosophers.jpg` |
| 83,467 | `thumbnails/ficino/02-the-melancholic-scholar.jpg` |
| 190,135 | `thumbnails/ficino/03-medicine-cabinet-of-the-soul.jpg` |
| 192,408 | `thumbnails/ficino/04-why-long-life-matters.jpg` |
| 237,227 | `thumbnails/ficino/05-food-putrefaction-gold-milk-blood.jpg` |
| 267,014 | `thumbnails/ficino/06-planetary-old-age.jpg` |
| 186,932 | `thumbnails/ficino/07-turn-to-the-living-world.jpg` |
| 267,729 | `thumbnails/ficino/08-lunar-medicine.jpg` |
| 185,488 | `thumbnails/ficino/09-the-celestial-catalogue.jpg` |
| 268,401 | `thumbnails/ficino/10-rays-figures-talismanic-image.jpg` |
| 205,083 | `thumbnails/ficino/11-song-words-dance-seven-steps.jpg` |
| 85,809 | `thumbnails/ficino/12-genius-vocation-place.jpg` |
| 250,820 | `thumbnails/ficino/13-the-apology.jpg` |
| 190,225 | `thumbnails/ficino/14-why-three-books.jpg` |
| 171,669 | `thumbnails/ficino/ficino_food_putrefaction_gold_milk_blood.jpg` |
| 193,164 | `thumbnails/ficino/ficino_genius_vocation_place.jpg` |
| 191,671 | `thumbnails/ficino/ficino_lunar_medicine.jpg` |
| 112,859 | `thumbnails/ficino/ficino_medicine_cabinet_of_the_soul.jpg` |
| 146,979 | `thumbnails/ficino/ficino_orientation_ficinos_world.jpg` |
| 190,984 | `thumbnails/ficino/ficino_planetary_old_age.jpg` |
| 192,333 | `thumbnails/ficino/ficino_rays_figures_talismanic_image.jpg` |
| 192,064 | `thumbnails/ficino/ficino_song_words_dance_seven_steps.jpg` |
| 195,950 | `thumbnails/ficino/ficino_the_apology.jpg` |
| 108,212 | `thumbnails/ficino/ficino_the_celestial_catalogue.jpg` |
| 198,748 | `thumbnails/ficino/ficino_the_melancholic_scholar.jpg` |
| 109,656 | `thumbnails/ficino/ficino_turn_to_the_living_world.jpg` |
| 121,848 | `thumbnails/ficino/ficino_why_long_life_matters.jpg` |
| 127,083 | `thumbnails/ficino/ficino_why_medicine_for_philosophers.jpg` |
| 190,561 | `thumbnails/ficino/ficino_why_three_books.jpg` |
| 73,087 | `thumbnails/ficino/you-died-already.jpg` |
| 188,284 | `thumbnails/film-packs/stones-are-watching.jpg` |
| 187,404 | `thumbnails/film-packs/world-between-worlds.jpg` |
| 194,437 | `thumbnails/glossary-essays/corbin-mundus-imaginalis.jpg` |
| 113,511 | `thumbnails/glossary-essays/daimon-threshold-guardian.jpg` |
| 171,669 | `thumbnails/glossary-essays/ficino_food_putrefaction_gold_milk_blood.jpg` |
| 193,164 | `thumbnails/glossary-essays/ficino_genius_vocation_place.jpg` |
| 191,671 | `thumbnails/glossary-essays/ficino_lunar_medicine.jpg` |
| 112,859 | `thumbnails/glossary-essays/ficino_medicine_cabinet_of_the_soul.jpg` |
| 146,979 | `thumbnails/glossary-essays/ficino_orientation_ficinos_world.jpg` |
| 190,984 | `thumbnails/glossary-essays/ficino_planetary_old_age.jpg` |
| 192,333 | `thumbnails/glossary-essays/ficino_rays_figures_talismanic_image.jpg` |
| 192,064 | `thumbnails/glossary-essays/ficino_song_words_dance_seven_steps.jpg` |
| 195,950 | `thumbnails/glossary-essays/ficino_the_apology.jpg` |
| 108,212 | `thumbnails/glossary-essays/ficino_the_celestial_catalogue.jpg` |
| 198,748 | `thumbnails/glossary-essays/ficino_the_melancholic_scholar.jpg` |
| 109,656 | `thumbnails/glossary-essays/ficino_turn_to_the_living_world.jpg` |
| 121,848 | `thumbnails/glossary-essays/ficino_why_long_life_matters.jpg` |
| 127,083 | `thumbnails/glossary-essays/ficino_why_medicine_for_philosophers.jpg` |
| 190,561 | `thumbnails/glossary-essays/ficino_why_three_books.jpg` |
| 175,306 | `thumbnails/glossary-essays/laya-daimon-test.jpg` |
| 73,087 | `thumbnails/glossary-essays/you-died-already.jpg` |
| 127,354 | `thumbnails/gold-standard/you-existed-before-earth.jpg` |
| 178,385 | `thumbnails/iamblichus/01-the-priest-replies.jpg` |
| 188,308 | `thumbnails/iamblichus/02-the-ladder-of-beings.jpg` |
| 170,992 | `thumbnails/iamblichus/03-how-to-read-epiphany.jpg` |
| 158,338 | `thumbnails/iamblichus/04-dreams-possession-divination.jpg` |
| 151,808 | `thumbnails/iamblichus/05-theurgy-is-not-coercion.jpg` |
| 188,566 | `thumbnails/iamblichus/06-why-matter-can-save.jpg` |
| 187,593 | `thumbnails/iamblichus/07-mud-lotus-sacred-names.jpg` |
| 151,547 | `thumbnails/iamblichus/08-fate-daemon-union.jpg` |
| 177,368 | `thumbnails/outputs/becoming_an_angel.jpg` |
| 91,336 | `thumbnails/outputs/corbin_creative_imagination.jpg` |
| 90,856 | `thumbnails/outputs/ibn_arabi_barzakh.jpg` |
| 177,525 | `thumbnails/outputs/mundus_imaginalis.jpg` |
| 171,598 | `thumbnails/plotinus-enneads/01-the-self-that-is-not-the-body.jpg` |
| 191,062 | `thumbnails/plotinus-enneads/02-becoming-like-god.jpg` |
| 120,109 | `thumbnails/plotinus-enneads/02-the-gaze-that-makes-worlds-intellect.jpg` |
| 174,395 | `thumbnails/plotinus-enneads/03-beauty-that-transfigures.jpg` |
| 174,905 | `thumbnails/plotinus-enneads/03-the-ladder-of-ascent.jpg` |
| 177,762 | `thumbnails/plotinus-enneads/04-happiness-does-not-come-and-go.jpg` |
| 171,369 | `thumbnails/plotinus-enneads/05-the-daemon-and-love.jpg` |
| 150,638 | `thumbnails/plotinus-enneads/06-whence-evil.jpg` |
| 155,964 | `thumbnails/plotinus-enneads/07-the-cosmos-is-beautiful.jpg` |
| 192,111 | `thumbnails/plotinus-enneads/08-the-receptacle-of-all-things.jpg` |
| 152,648 | `thumbnails/plotinus-enneads/10-love-as-child-of-poverty-and-plenty.jpg` |
| 175,764 | `thumbnails/plotinus-enneads/11-providence-is-not-fate.jpg` |
| 130,044 | `thumbnails/plotinus-enneads/12-eternity-and-time.jpg` |
| 132,994 | `thumbnails/plotinus-enneads/13-contemplation-makes-the-world.jpg` |
| 174,905 | `thumbnails/plotinus-enneads/14-the-amphibious-soul.jpg` |
| 173,837 | `thumbnails/plotinus-enneads/15-the-powers-of-the-soul.jpg` |
| 171,952 | `thumbnails/plotinus-enneads/16-the-soul-is-one-and-many.jpg` |
| 152,979 | `thumbnails/plotinus-enneads/17-the-soul-does-not-die.jpg` |
| 158,078 | `thumbnails/plotinus-enneads/18-the-three-primary-hypostases.jpg` |
| 176,350 | `thumbnails/plotinus-enneads/19-the-intellect-that-does-not-look-outside.jpg` |
| 178,159 | `thumbnails/plotinus-enneads/20-the-self-knowing-intellect.jpg` |
| 264,832 | `thumbnails/plotinus-enneads/21-the-splendor-of-the-intelligible-world.jpg` |
| 192,585 | `thumbnails/plotinus-enneads/22-intellect-ideas-and-being.jpg` |
| 130,867 | `thumbnails/plotinus-enneads/23-the-one-beyond-being.jpg` |
| 177,803 | `thumbnails/plotinus-enneads/24-numbers-as-the-structure-of-reality.jpg` |
| 157,199 | `thumbnails/plotinus-enneads/25-the-multiplicity-of-ideas.jpg` |
| 206,066 | `thumbnails/plotinus-enneads/26-the-ones-freedom.jpg` |
| 176,511 | `thumbnails/plotinus-enneads/27-being-is-everywhere-whole.jpg` |
| 148,707 | `thumbnails/source-note-essays/corbin-attar-essay.jpg` |
| 224,662 | `thumbnails/source-note-essays/ficino-living-book-essay.jpg` |
| 120,850 | `thumbnails/source-note-essays/imaginal-corbin-ibnarabi-suhrawardi.jpg` |
| 115,961 | `thumbnails/source-note-essays/theurgy-sallustius-essay.jpg` |
| 178,575 | `thumbnails/tantraloka-essays/daimon-contact-complete.jpg` |
| 167,735 | `thumbnails/tantraloka-essays/daimon-contact.jpg` |
| 188,692 | `thumbnails/tantraloka-essays/expansion-essay1.jpg` |
| 181,717 | `thumbnails/tantraloka-essays/expansion-essay10.jpg` |
| 152,354 | `thumbnails/tantraloka-essays/expansion-essay11.jpg` |
| 187,404 | `thumbnails/tantraloka-essays/expansion-essay12.jpg` |
| 262,175 | `thumbnails/tantraloka-essays/expansion-essay13.jpg` |
| 154,845 | `thumbnails/tantraloka-essays/expansion-essay14.jpg` |
| 189,550 | `thumbnails/tantraloka-essays/expansion-essay15.jpg` |
| 130,886 | `thumbnails/tantraloka-essays/expansion-essay16.jpg` |
| 150,403 | `thumbnails/tantraloka-essays/expansion-essay17.jpg` |
| 186,136 | `thumbnails/tantraloka-essays/expansion-essay18.jpg` |
| 152,768 | `thumbnails/tantraloka-essays/expansion-essay19.jpg` |
| 192,692 | `thumbnails/tantraloka-essays/expansion-essay2.jpg` |
| 184,606 | `thumbnails/tantraloka-essays/expansion-essay20.jpg` |
| 241,462 | `thumbnails/tantraloka-essays/expansion-essay21.jpg` |
| 158,043 | `thumbnails/tantraloka-essays/expansion-essay22.jpg` |
| 189,525 | `thumbnails/tantraloka-essays/expansion-essay23.jpg` |
| 99,982 | `thumbnails/tantraloka-essays/expansion-essay24.jpg` |
| 243,321 | `thumbnails/tantraloka-essays/expansion-essay25.jpg` |
| 135,528 | `thumbnails/tantraloka-essays/expansion-essay26.jpg` |
| 240,743 | `thumbnails/tantraloka-essays/expansion-essay27.jpg` |
| 82,064 | `thumbnails/tantraloka-essays/expansion-essay28.jpg` |
| 186,081 | `thumbnails/tantraloka-essays/expansion-essay29.jpg` |
| 187,961 | `thumbnails/tantraloka-essays/expansion-essay3.jpg` |
| 183,776 | `thumbnails/tantraloka-essays/expansion-essay30.jpg` |
| 189,260 | `thumbnails/tantraloka-essays/expansion-essay31.jpg` |
| 171,398 | `thumbnails/tantraloka-essays/expansion-essay32.jpg` |
| 151,779 | `thumbnails/tantraloka-essays/expansion-essay33.jpg` |
| 127,354 | `thumbnails/tantraloka-essays/expansion-essay34.jpg` |
| 157,001 | `thumbnails/tantraloka-essays/expansion-essay35.jpg` |
| 170,046 | `thumbnails/tantraloka-essays/expansion-essay36.jpg` |
| 127,835 | `thumbnails/tantraloka-essays/expansion-essay37.jpg` |
| 42,352 | `thumbnails/tantraloka-essays/expansion-essay38.jpg` |
| 187,424 | `thumbnails/tantraloka-essays/expansion-essay39.jpg` |
| 183,586 | `thumbnails/tantraloka-essays/expansion-essay4.jpg` |
| 187,607 | `thumbnails/tantraloka-essays/expansion-essay40.jpg` |
| 95,626 | `thumbnails/tantraloka-essays/expansion-essay41.jpg` |
| 241,842 | `thumbnails/tantraloka-essays/expansion-essay42.jpg` |
| 248,168 | `thumbnails/tantraloka-essays/expansion-essay43.jpg` |
| 173,815 | `thumbnails/tantraloka-essays/expansion-essay44.jpg` |
| 96,083 | `thumbnails/tantraloka-essays/expansion-essay45.jpg` |
| 188,284 | `thumbnails/tantraloka-essays/expansion-essay46.jpg` |
| 172,182 | `thumbnails/tantraloka-essays/expansion-essay47.jpg` |
| 267,475 | `thumbnails/tantraloka-essays/expansion-essay48.jpg` |
| 148,868 | `thumbnails/tantraloka-essays/expansion-essay49.jpg` |
| 109,401 | `thumbnails/tantraloka-essays/expansion-essay5.jpg` |
| 234,645 | `thumbnails/tantraloka-essays/expansion-essay50.jpg` |
| 173,344 | `thumbnails/tantraloka-essays/expansion-essay51.jpg` |
| 182,296 | `thumbnails/tantraloka-essays/expansion-essay6.jpg` |
| 192,269 | `thumbnails/tantraloka-essays/expansion-essay7.jpg` |
| 192,715 | `thumbnails/tantraloka-essays/expansion-essay8.jpg` |
| 173,677 | `thumbnails/tantraloka-essays/expansion-essay9.jpg` |
| 205,084 | `thumbnails/whattheheckis/what-the-heck-is-tetrahedron.jpg` |
| 112,772 | `thumbnails/whattheheckis/what-the-heck-is-time.jpg` |
| 188,436 | `thumbnails/whattheheckis/whattheheckis-exclusion.jpg` |
| 187,941 | `thumbnails/whattheheckis/whattheheckisagency.jpg` |
| 128,507 | `thumbnails/whattheheckis/whattheheckischanneling.jpg` |
| 187,656 | `thumbnails/whattheheckis/whattheheckisimagination.jpg` |
| 187,836 | `thumbnails/whattheheckis/whattheheckismemory.jpg` |
| 127,719 | `thumbnails/whattheheckis/whattheheckisself.jpg` |
| 188,253 | `thumbnails/whattheheckis/whattheheckissubtlebody.jpg` |
| 124,847 | `thumbnails/whattheheckis/whattheheckistime.jpg` |
| 188,381 | `thumbnails/whattheheckis/whattheheckisvalence.jpg` |
| 175,343 | `thumbnails/workshop-v6/becoming_an_angel_beautiful_edition_v6.jpg` |
| 190,037 | `thumbnails/workshop-v6/corbin_attar_v6.jpg` |
| 171,357 | `thumbnails/workshop-v6/corbin_avicenna_angel_v6.jpg` |
| 191,509 | `thumbnails/workshop-v6/corbin_blake_v6.jpg` |
| 176,996 | `thumbnails/workshop-v6/corbin_creative_imagination_v6.jpg` |
| 184,936 | `thumbnails/workshop-v6/corbin_hillman_v6.jpg` |
| 187,106 | `thumbnails/workshop-v6/corbin_jung_v6.jpg` |
| 132,107 | `thumbnails/workshop-v6/corbin_plotinus_beauty_v6.jpg` |
| 189,706 | `thumbnails/workshop-v6/corbin_steiner_imagination_v6.jpg` |
| 84,942 | `thumbnails/workshop-v6/corbin_swedenborg_v6.jpg` |
| 191,770 | `thumbnails/workshop-v6/ficino_divine_madness_v6.jpg` |
| 190,727 | `thumbnails/workshop-v6/ficino_ladder_of_desire_v6.jpg` |
| 192,127 | `thumbnails/workshop-v6/ficino_spiritus_v6.jpg` |
| 132,107 | `thumbnails/workshop-v6/ficino_sunlike_eye_v6.jpg` |
| 189,105 | `thumbnails/workshop-v6/ficino_theurgy_v6.jpg` |
| 186,643 | `thumbnails/workshop-v6/ficino_world_living_book_v6.jpg` |
| 158,547 | `thumbnails/workshop-v6/goethe_between_light_eye_v6.jpg` |
| 189,579 | `thumbnails/workshop-v6/goethe_colour_edge_v6.jpg` |
| 196,128 | `thumbnails/workshop-v6/goethe_exact_sensorial_v6.jpg` |
| 191,778 | `thumbnails/workshop-v6/goethe_eye_restores_thought_v6.jpg` |
| 191,465 | `thumbnails/workshop-v6/goethe_image_without_object_v6.jpg` |
| 197,599 | `thumbnails/workshop-v6/goethe_metamorphosis_phenomena_v6.jpg` |
| 191,414 | `thumbnails/workshop-v6/goethe_organism_whole_v6.jpg` |
| 113,673 | `thumbnails/workshop-v6/goethe_thought_begins_see_v6.jpg` |
| 90,856 | `thumbnails/workshop-v6/ibn_arabi_barzakh_v6.jpg` |
| 170,900 | `thumbnails/workshop-v6/mundus_handcrafted_v6.jpg` |
| 156,738 | `thumbnails/workshop-v6/theurgy_asclepius_v6.jpg` |
| 189,953 | `thumbnails/workshop-v6/theurgy_chaldean_v6.jpg` |
| 190,582 | `thumbnails/workshop-v6/theurgy_iamblichus_v6.jpg` |
| 129,766 | `thumbnails/workshop-v6/theurgy_plotinus_v6.jpg` |
| 189,553 | `thumbnails/workshop-v6/theurgy_proclus_v6.jpg` |
| 187,334 | `thumbnails/workshop-v6/theurgy_sallustius_v6.jpg` |
