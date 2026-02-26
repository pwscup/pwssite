"""Tests for pandoc.py (shared logic used by 2026 and ppsd)."""

import sys
from pathlib import Path

import pytest

# Add 2026/scripts to path so we can import pandoc module
SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "2026" / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import pandoc as pandoc_mod  # noqa: E402


class TestExtractTitle:
    def test_extracts_h1(self, tmp_path: Path):
        md = tmp_path / "test.md"
        md.write_text("# My Title\nsome content\n", encoding="utf-8")
        assert pandoc_mod.extract_title(md) == "My Title"

    def test_extracts_first_h1(self, tmp_path: Path):
        md = tmp_path / "test.md"
        md.write_text("# First\n# Second\n", encoding="utf-8")
        assert pandoc_mod.extract_title(md) == "First"

    def test_default_when_no_h1(self, tmp_path: Path):
        md = tmp_path / "test.md"
        md.write_text("## Not H1\nsome content\n", encoding="utf-8")
        assert pandoc_mod.extract_title(md) == "PWS"

    def test_default_when_empty_h1(self, tmp_path: Path):
        md = tmp_path / "test.md"
        md.write_text("# \nsome content\n", encoding="utf-8")
        assert pandoc_mod.extract_title(md) == "PWS"

    def test_default_when_file_not_found(self, tmp_path: Path):
        md = tmp_path / "nonexistent.md"
        assert pandoc_mod.extract_title(md) == "PWS"


class TestBuildBody:
    def test_basic_conversion(self):
        toc, html = pandoc_mod.build_body("# Hello\n\nParagraph\n")
        assert "<p>Paragraph</p>" in html

    def test_table_conversion(self):
        md = "| A | B |\n|---|---|\n| 1 | 2 |\n"
        _, html = pandoc_mod.build_body(md)
        assert "<table>" in html
        assert "<td>1</td>" in html

    def test_fenced_code(self):
        md = "```python\nprint('hello')\n```\n"
        _, html = pandoc_mod.build_body(md)
        assert "<code" in html
        assert "print" in html

    def test_footnote(self):
        md = "Text[^1]\n\n[^1]: Footnote content\n"
        _, html = pandoc_mod.build_body(md)
        assert "Footnote content" in html

    def test_toc_generated_with_sections(self):
        md = "# Title\n## Sec1\ntext\n## Sec2\ntext\n"
        toc, _ = pandoc_mod.build_body(md)
        assert "<li>" in toc

    def test_toc_empty_without_sections(self):
        md = "# Title only\nsome text\n"
        toc, _ = pandoc_mod.build_body(md)
        assert toc == ""


class TestInsertTocAfterWhatsNew:
    def test_no_toc(self):
        html = "<h1>Title</h1><p>content</p>"
        result = pandoc_mod.insert_toc_after_whats_new(html, "")
        assert result == html

    def test_inserts_after_whats_new(self):
        html = "<h1>Title</h1><h2>What's new</h2><p>news</p><h2>Next</h2>"
        toc = '<div class="toc"><ul><li>item</li></ul></div>'
        result = pandoc_mod.insert_toc_after_whats_new(html, toc)
        # TOC should be between "news" paragraph and "Next" h2
        assert result.index("目次") < result.index("Next")
        assert result.index("news") < result.index("目次")

    def test_fallback_after_h1(self):
        html = "<h1>Title</h1><p>intro</p><h2>Section</h2>"
        toc = '<div class="toc"><ul><li>item</li></ul></div>'
        result = pandoc_mod.insert_toc_after_whats_new(html, toc)
        # TOC should be after intro paragraph
        assert result.index("intro") < result.index("目次")


class TestBuildHeader:
    def test_japanese_template(self, template_dir_2026: Path):
        script_dir = template_dir_2026.parent / "scripts"
        header = pandoc_mod.build_header(script_dir, "index", "Test Title")
        assert "<title>Test Title</title>" in header
        assert 'lang="ja"' in header

    def test_english_template(self, template_dir_2026: Path):
        script_dir = template_dir_2026.parent / "scripts"
        header = pandoc_mod.build_header(script_dir, "index_e", "Test Title")
        assert "<title>Test Title</title>" in header
        assert 'lang="en"' in header
