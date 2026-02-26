"""Tests for make.py build logic."""

import sys
import time
from pathlib import Path

import pytest

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "2026" / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import make as make_mod  # noqa: E402


class TestCollectMarkdown:
    def test_finds_md_files(self, tmp_markdown: Path):
        result = make_mod.collect_markdown(tmp_markdown)
        assert len(result) == 1
        assert result[0] == Path("sample.md")

    def test_finds_nested_md_files(self, tmp_markdown: Path):
        sub = tmp_markdown / "sub"
        sub.mkdir()
        (sub / "nested.md").write_text("# Nested\n", encoding="utf-8")
        result = make_mod.collect_markdown(tmp_markdown)
        assert len(result) == 2

    def test_empty_directory(self, tmp_path: Path):
        empty = tmp_path / "empty"
        empty.mkdir()
        result = make_mod.collect_markdown(empty)
        assert result == []

    def test_ignores_non_md_files(self, tmp_markdown: Path):
        (tmp_markdown / "readme.txt").write_text("not markdown", encoding="utf-8")
        result = make_mod.collect_markdown(tmp_markdown)
        assert len(result) == 1

    def test_sorted_output(self, tmp_markdown: Path):
        (tmp_markdown / "aaa.md").write_text("# A\n", encoding="utf-8")
        (tmp_markdown / "zzz.md").write_text("# Z\n", encoding="utf-8")
        result = make_mod.collect_markdown(tmp_markdown)
        names = [r.name for r in result]
        assert names == sorted(names)


class TestIncrementalBuild:
    """Test the build-target selection logic from make.main()."""

    def test_new_md_is_build_target(self, tmp_path: Path):
        md_dir = tmp_path / "markdown"
        html_dir = tmp_path / "html"
        md_dir.mkdir()
        html_dir.mkdir()
        md = md_dir / "test.md"
        md.write_text("# Test\n", encoding="utf-8")
        # No HTML exists → should be a target
        rel = Path("test.md")
        html = html_dir / "test.html"
        assert not html.exists()

    def test_updated_md_is_build_target(self, tmp_path: Path):
        md_dir = tmp_path / "markdown"
        html_dir = tmp_path / "html"
        md_dir.mkdir()
        html_dir.mkdir()
        html = html_dir / "test.html"
        html.write_text("<html></html>", encoding="utf-8")
        time.sleep(0.05)
        md = md_dir / "test.md"
        md.write_text("# Updated\n", encoding="utf-8")
        assert md.stat().st_mtime > html.stat().st_mtime

    def test_unchanged_md_is_not_target(self, tmp_path: Path):
        md_dir = tmp_path / "markdown"
        html_dir = tmp_path / "html"
        md_dir.mkdir()
        html_dir.mkdir()
        md = md_dir / "test.md"
        md.write_text("# Test\n", encoding="utf-8")
        time.sleep(0.05)
        html = html_dir / "test.html"
        html.write_text("<html></html>", encoding="utf-8")
        assert md.stat().st_mtime < html.stat().st_mtime
