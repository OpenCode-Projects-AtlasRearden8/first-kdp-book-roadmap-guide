# STATUS.md — First KDP Book Roadmap Guide

Last updated: 2026-11-05

## What was built

An end-to-end beginner manual for publishing a first low-stress book on KDP, delivered as Markdown sources plus a tested static-site build.

### The manual (`docs/`, 9 pages)

1. **`index.md`** — who it's for, the roadmap at a glance, disclaimers.
2. **`01-wrong-vs-right-first-project.md`** — picking a first book you can finish; wrong shapes (giant handbooks, fast-expiring topics, fiction series, permission traps) vs. right shapes; real lessons from *The Massive AI Manual*.
3. **`02-interior-setup-page-by-page.md`** — Kindle and paperback interiors in reading order: title page, copyright page, disclaimer, TOC, body, back matter; trim size, outside margins, gutter rules, embedded fonts, 300-DPI images, bleed.
4. **`03-pricing-honestly.md`** — 35% vs. 70% royalty tiers, delivery fee, paperback printing cost, a worked illustrative example, five honest pricing principles, a pricing worksheet.
5. **`04-categories-and-keywords.md`** — honest category matching, real-reader keyword phrases, prohibited-keyword pitfalls, writing a truthful description, review integrity.
6. **`05-launch-week.md`** — a calm launch checklist, day-by-day posture, what *not* to do, realistic-expectations table.
7. **`06-royalties-and-paperwork.md`** — payment timeline, the sales-vs-royalty distinction, W-9/W-8 forms, LLC payee consistency, what records to keep, ISBN defaults.
8. **`checklists.md`** — printable phase checklists for every chapter.
9. **`glossary.md`** — plain-English definitions of every acronym and term.

Grounded in the experience of publishing *The Massive AI Manual*, education-only, no hype, no affiliate links. KDP numeric rules are hedged with explicit verify-against-current-documentation notes.

### The site (`site/`, generated)

A static HTML site built by `build.py`: one page per chapter, a sticky sidebar with `aria-current` page marking, prev/home/next pager, footer with `Copyright (c) 2026 Asdale Dynamics, LLC` and an education-not-advice disclaimer, responsive single-column layout under 56em. Fully offline (no external fonts/CDNs).

### The build

- **`build.py`** (Python, stdlib + `markdown`): converts `docs/*.md` in canonical reading order to `site/*.html` + CSS copy. CLI: `python3 build.py [--docs DIR] [--out DIR] [--style FILE]`. Deterministic output; stale HTML files are removed.
- **`test_build.py`** (pytest, 19 tests): title extraction, HTML escaping, canonical page ordering, missing-doc failure, full build contents/assets, footer & disclaimer presence, nav cache, stale-file cleanup, determinism, CLI success/error codes, and a no-secrets/no-personal-data scan of output.

## How to run it

```bash
pip install markdown    # the only non-stdlib dependency
python3 build.py        # build docs/ -> site/
python3 -m pytest       # run the test suite
```

Then open `site/index.html` in a browser (no server needed).

## Verification results

- `python3 -m pytest` → **19 passed**.
- `python3 build.py` → **built 9 pages -> site/**, exit code 0, all expected files present, plus `site/assets/style.css`.
- Spot-checks: rendered pricing chapter contains the royalty table and both links; every page includes DOCTYPE, article, footer, and disclaimer text.

## Known gaps

- **KDP numbers age.** Royalty tiers, delivery fee, printing-cost formula, margin/gutter thresholds, and keyword/category slots reflect values used in real experience; each numeric statement is flagged with a verify note, but no automated check ties them to KDP's help center.
- **No break-even calculator** — this repo is deliberately a manual, distinct from the existing `kdp-*` calculators/checkers tools, which pair naturally with it.
- **No cover-file guidance.** Cover anatomy (spine width, safely margins, templates) is its own topic and is out of scope for this guide; the interior is covered in depth instead.
- **Site is minimal by design.** No search, no dark mode, no print-specific stylesheet; suggestions if the manual grows: add print CSS and maybe full-page search.
- **Glossary cites "at the time of writing" values only in one place (Koll note).** Acceptable, but a future pass could standardize date-of-check stamps per term.
