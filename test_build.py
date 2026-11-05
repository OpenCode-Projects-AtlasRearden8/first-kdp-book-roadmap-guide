"""Tests for build.py — run with `pytest`."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build as build_mod  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parent

# A minimal markdown fixture used for build() unit tests. Custom pages are
# keyed by real slugs; the rest of the required slugs get generic content.
SECOND_SLUG = build_mod.PAGE_ORDER[1]
MINIMAL_DOCS = {
    "index": "# Home Page\n\nWelcome to the manual.\n",
    SECOND_SLUG: "# Second Page\n\nSome body text with `code`.\n",
    "glossary": "# Glossary\n\n- **ASIN** — Amazon's identifier.\n",
}

STYLE = "/* minimal css */ body { color: #111; }\n"


def _make_docs(tmp_path: Path, pages: dict[str, str] | None = None) -> Path:
    docs = tmp_path / "docs"
    docs.mkdir()
    content = pages or MINIMAL_DOCS
    for slug in build_mod.PAGE_ORDER:
        # Provided pages win; required slugs get a generic body otherwise.
        title = content.get(slug, build_mod.slugify(Path(f"{slug}.md")).replace("-", " ").title())
        text = content.get(slug, f"# {title}\n\nBody content for {slug}.\n")
        (docs / f"{slug}.md").write_text(text, encoding="utf-8")
    return docs


@pytest.fixture()
def style_file(tmp_path: Path) -> Path:
    style = tmp_path / "style.css"
    style.write_text(STYLE, encoding="utf-8")
    return style


class TestPageTitle:
    def test_extract_h1(self):
        assert build_mod.page_title("<h1>My Title</h1>", Path("x.md")) == "My Title"

    def test_strips_inner_tags(self):
        assert (
            build_mod.page_title("<h1>Preface &amp; Notes <a href='#x'>a</a></h1>", Path("x.md"))
            == "Preface &amp;amp; Notes a"
        )

    def test_fallback_when_no_h1(self):
        assert (
            build_mod.page_title("<p>no heading</p>", Path("my-chapter.md"))
            == "My Chapter"
        )

    def test_parallel_h1_removal(self):
        body = build_mod.page_body("<h1>T</h1>\n<p>rest</p>")
        assert "<h1>" not in body
        assert "<p>rest</p>" in body


class TestHtmlEscape:
    @pytest.mark.parametrize(
        "raw,expected",
        [
            ("plain text", "plain text"),
            ("a & b", "a &amp; b"),
            ("<b>x</b>", "&lt;b&gt;x&lt;/b&gt;"),
            ('quote " here', "quote &quot; here"),
        ],
    )
    def test_escape(self, raw, expected):
        assert build_mod.html_escape(raw) == expected


class TestDiscoverPages:
    def test_canonical_order(self, tmp_path: Path):
        docs = _make_docs(tmp_path)
        sources = build_mod.discover_pages(docs)
        stems = [p.stem for p in sources]
        # index first, glossary last; chapters between in canonical order.
        assert stems[0] == "index"
        assert stems[-1] == "glossary"
        assert stems[1].startswith("01-")

    def test_missing_doc_fails(self, tmp_path: Path):
        docs = tmp_path / "docs"
        docs.mkdir()
        (docs / "index.md").write_text(MINIMAL_DOCS["index"], encoding="utf-8")
        with pytest.raises(SystemExit):
            build_mod.discover_pages(docs)


class TestBuild:
    def test_builds_all_pages_and_assets(self, tmp_path: Path, style_file: Path):
        docs = _make_docs(tmp_path)
        out = tmp_path / "site"
        stats = build_mod.build(docs, out, style_file)

        assert stats["pages"] == len(build_mod.PAGE_ORDER)
        for slug in build_mod.PAGE_ORDER:
            page = out / f"{slug}.html"
            assert page.exists(), f"missing {page}"
            html = page.read_text(encoding="utf-8")
            assert "<!DOCTYPE html>" in html
            assert "<article>" in html
            assert 'href="assets/style.css"' in html
        copied = out / "assets" / style_file.name
        assert copied.exists()
        assert copied.read_text(encoding="utf-8") == STYLE

    def test_footer_and_disclaimer_present(self, tmp_path: Path, style_file: Path):
        docs = _make_docs(tmp_path)
        out = tmp_path / "site"
        build_mod.build(docs, out, style_file)
        html = (out / "index.html").read_text(encoding="utf-8")
        assert build_mod.COPYRIGHT_LINE in html
        assert build_mod.PUBLISHER in html
        assert "Education only" in html

    def test_titles_extracted_into_head(self, tmp_path: Path, style_file: Path):
        docs = _make_docs(tmp_path)
        out = tmp_path / "site"
        build_mod.build(docs, out, style_file)
        html = (out / f"{SECOND_SLUG}.html").read_text(encoding="utf-8")
        assert "<title>Second Page" in html
        assert "<h1>Second Page</h1>" in html

    def test_nav_links_prev_next(self, tmp_path: Path, style_file: Path):
        docs = _make_docs(tmp_path)
        out = tmp_path / "site"
        build_mod.build(docs, out, style_file)
        middle = (out / f"{SECOND_SLUG}.html").read_text(encoding="utf-8")
        assert "Prev" in middle and "Next" in middle and "index.html" in middle
        # aria-current only on the matching sidebar entry
        assert middle.count('aria-current="page"') == 1

    def test_stale_html_removed(self, tmp_path: Path, style_file: Path):
        docs = _make_docs(tmp_path)
        out = tmp_path / "site"
        out.mkdir()
        stale = out / "old-page.html"
        stale.write_text("stale", encoding="utf-8")
        build_mod.build(docs, out, style_file)
        assert not stale.exists()

    def test_build_is_deterministic(self, tmp_path: Path, style_file: Path):
        docs = _make_docs(tmp_path)
        out1 = tmp_path / "a"
        out2 = tmp_path / "b"
        build_mod.build(docs, out1, style_file)
        build_mod.build(docs, out2, style_file)
        for slug in MINIMAL_DOCS:
            a = sorted((out1 / f"{slug}.html").read_text(encoding="utf-8").splitlines())
            b = sorted((out2 / f"{slug}.html").read_text(encoding="utf-8").splitlines())
            assert a == b


class TestMain:
    def test_cli_builds_real_repo_site(self, tmp_path: Path):
        out = tmp_path / "site"
        rc = build_mod.main(
            [
                "--docs",
                str(PROJECT_ROOT / "docs"),
                "--out",
                str(out),
                "--style",
                str(PROJECT_ROOT / "assets" / "style.css"),
            ]
        )
        assert rc == 0
        for slug in build_mod.PAGE_ORDER:
            assert (out / f"{slug}.html").exists()

    def test_cli_reports_missing_docs(self, tmp_path: Path):
        rc = build_mod.main(
            [
                "--docs",
                str(tmp_path / "nosuchdir"),
                "--out",
                str(tmp_path / "site"),
                "--style",
                str(PROJECT_ROOT / "assets" / "style.css"),
            ]
        )
        assert rc == 2

    def test_no_secrets_in_output(self, tmp_path: Path, style_file: Path):
        """Site output must not contain API-key-shaped strings or personal data."""
        docs = _make_docs(tmp_path)
        out = tmp_path / "site"
        build_mod.build(docs, out, style_file)
        for page in out.glob("*.html"):
            text = page.read_text(encoding="utf-8")
            assert not re.search(r"sk-[A-Za-z0-9]{20,}", text), "secret-like token"
            assert "@" not in text, "unexpected email address"
