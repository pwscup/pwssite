"""Tests for ppsd/scripts/pandoc.py (GFM-compatible engine)."""

import importlib
import sys
from pathlib import Path

import pytest

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "ppsd" / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

# Force reload to avoid using cached 2026/scripts/pandoc
if "pandoc" in sys.modules:
    del sys.modules["pandoc"]
import pandoc as ppsd_pandoc  # noqa: E402


class TestBuildBodyGfm:
    def test_basic_conversion(self):
        toc, html = ppsd_pandoc.build_body("# Hello\n\nParagraph\n")
        assert "<p>Paragraph</p>" in html

    def test_table_conversion(self):
        md = "| A | B |\n|---|---|\n| 1 | 2 |\n"
        _, html = ppsd_pandoc.build_body(md)
        assert "<table>" in html
        assert "<td>1</td>" in html

    def test_fenced_code(self):
        md = "```python\nprint('hello')\n```\n"
        _, html = ppsd_pandoc.build_body(md)
        assert "<code" in html
        assert "print" in html

    def test_footnote(self):
        md = "Text[^1]\n\n[^1]: Footnote content\n"
        _, html = ppsd_pandoc.build_body(md)
        assert "Footnote content" in html

    def test_strikethrough(self):
        md = "~~deleted text~~\n"
        _, html = ppsd_pandoc.build_body(md)
        assert "<s>" in html or "<del>" in html
        assert "deleted text" in html

    def test_raw_html_preserved(self):
        md = "<dl>\n<dt>Key</dt>\n<dd>Value</dd>\n</dl>\n"
        _, html = ppsd_pandoc.build_body(md)
        assert "<dl>" in html
        assert "<dt>Key</dt>" in html
        assert "<dd>Value</dd>" in html

    def test_dash_list(self):
        md = "- item1\n- item2\n"
        _, html = ppsd_pandoc.build_body(md)
        assert "<li>" in html
        assert "item1" in html

    def test_toc_generated_with_sections(self):
        md = "# Title\n## Sec1\ntext\n## Sec2\ntext\n"
        toc, _ = ppsd_pandoc.build_body(md)
        assert "<li>" in toc
        assert "Sec1" in toc
        assert "Sec2" in toc

    def test_toc_empty_without_sections(self):
        md = "# Title only\nsome text\n"
        toc, _ = ppsd_pandoc.build_body(md)
        assert toc == ""

    def test_heading_ids_generated(self):
        md = "# Title\n## Section One\ntext\n"
        _, html = ppsd_pandoc.build_body(md)
        assert 'id="section-one"' in html

    def test_japanese_heading_ids(self):
        md = "# タイトル\n## セクション\ntext\n"
        _, html = ppsd_pandoc.build_body(md)
        assert 'id="セクション"' in html

    def test_toc_structure(self):
        md = "# Title\n## A\ntext\n### B\ntext\n## C\ntext\n"
        toc, _ = ppsd_pandoc.build_body(md)
        assert '<div class="toc">' in toc
        assert "<ul>" in toc
        assert "</ul>" in toc
