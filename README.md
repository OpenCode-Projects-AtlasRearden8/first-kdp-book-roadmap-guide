# First KDP Book Roadmap Guide

An end-to-end beginner manual for publishing your first low-stress book on Amazon Kindle Direct Publishing (KDP) — in plain English, with no hype and no tricks.

It covers the whole path: choosing a first project you can actually finish, setting up the interior page by page, pricing with real math instead of folklore, using categories and keywords honestly, running a calm launch week, and keeping royalties paperwork clean. It also includes condensed checklists and a glossary.

Everything here is grounded in the real experience of publishing *The Massive AI Manual* — a book from [Asdale Dynamics, LLC](https://dylanasdale.github.io) that explains AI "like a friend would."

**Important:** this repository contains education, not legal, tax, or accounting advice, and no affiliate links or upsells. KDP's numbers change; the guide's method is durable, but always verify current rates and thresholds against Amazon's help documentation.

## What's in this repo

| Path | What it is |
| --- | --- |
| `docs/` | The manual's source: one Markdown file per chapter, plus `checklists.md` and `glossary.md` |
| `build.py` | Tested build script that renders `docs/` into a static HTML site |
| `assets/style.css` | The site's stylesheet |
| `site/` | Generated static site (includes an `index.html` and one HTML page per chapter) |
| `test_build.py` | Test suite for the build script: `pytest` |
| `STATUS.md` | What was built, how to verify, known gaps |

## Run it

You need Python 3.10+ and the `markdown` package (`pip install markdown`).

```bash
# Build the site (docs/ -> site/)
python3 build.py

# Custom paths
python3 build.py --docs docs --out site --style assets/style.css

# Run the test suite
python3 -m pytest
```

The generated `site/` is fully static — open `site/index.html` in a browser, no server needed.

## Reuse this guide's structure

Copy the structure freely: one Markdown file per chapter, a `PAGE_ORDER` list in `build.py`, checklists, and a glossary. The build script is MIT-licensed (see `LICENSE`), attributed to `Copyright (c) 2026 Asdale Dynamics, LLC`.

## License

MIT — see [LICENSE](LICENSE). Copyright line: `Copyright (c) 2026 Asdale Dynamics, LLC`.
