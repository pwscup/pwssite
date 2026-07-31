"""Tests for scripts/make.py build logic."""

import os
import sys
import time
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
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


def _make_dirs(tmp_path: Path) -> tuple[Path, Path]:
    md_dir = tmp_path / "markdown"
    html_dir = tmp_path / "html"
    md_dir.mkdir()
    html_dir.mkdir()
    return md_dir, html_dir


def _bases(targets: list) -> list:
    return [base for base, _ in targets]


class TestIncrementalBuild:
    """Test the build-target selection logic from make.select_targets()."""

    def test_new_md_is_build_target(self, tmp_path: Path):
        md_dir, html_dir = _make_dirs(tmp_path)
        (md_dir / "test.md").write_text("# Test\n", encoding="utf-8")
        assert not (html_dir / "test.html").exists()

        rels = make_mod.collect_markdown(md_dir)
        assert _bases(make_mod.select_targets(md_dir, html_dir, rels)) == ["test"]

    def test_updated_md_is_build_target(self, tmp_path: Path):
        md_dir, html_dir = _make_dirs(tmp_path)
        html = html_dir / "test.html"
        html.write_text("<html></html>", encoding="utf-8")
        time.sleep(0.05)
        md = md_dir / "test.md"
        md.write_text("# Updated\n", encoding="utf-8")
        assert md.stat().st_mtime > html.stat().st_mtime

        rels = make_mod.collect_markdown(md_dir)
        assert _bases(make_mod.select_targets(md_dir, html_dir, rels)) == ["test"]

    def test_unchanged_md_is_not_target(self, tmp_path: Path):
        md_dir, html_dir = _make_dirs(tmp_path)
        md = md_dir / "test.md"
        md.write_text("# Test\n", encoding="utf-8")
        time.sleep(0.05)
        html = html_dir / "test.html"
        html.write_text("<html></html>", encoding="utf-8")
        assert md.stat().st_mtime < html.stat().st_mtime

        rels = make_mod.collect_markdown(md_dir)
        assert make_mod.select_targets(md_dir, html_dir, rels) == []


class TestForceRebuild:
    """--force must ignore mtime entirely (CI relies on this)."""

    def test_force_selects_unchanged_md(self, tmp_path: Path):
        md_dir, html_dir = _make_dirs(tmp_path)
        (md_dir / "test.md").write_text("# Test\n", encoding="utf-8")
        time.sleep(0.05)
        (html_dir / "test.html").write_text("<html></html>", encoding="utf-8")

        rels = make_mod.collect_markdown(md_dir)
        targets = make_mod.select_targets(md_dir, html_dir, rels, force=True)
        assert _bases(targets) == ["test"]

    def test_force_selects_md_with_identical_mtime(self, tmp_path: Path):
        """A fresh git checkout can leave md and html with the same mtime."""
        md_dir, html_dir = _make_dirs(tmp_path)
        md = md_dir / "test.md"
        md.write_text("# Test\n", encoding="utf-8")
        html = html_dir / "test.html"
        html.write_text("<html></html>", encoding="utf-8")
        stamp = md.stat().st_mtime
        os.utime(html, (stamp, stamp))
        assert md.stat().st_mtime == html.stat().st_mtime

        rels = make_mod.collect_markdown(md_dir)
        # Without --force the equal mtime makes this a silent no-op.
        assert make_mod.select_targets(md_dir, html_dir, rels) == []
        targets = make_mod.select_targets(md_dir, html_dir, rels, force=True)
        assert _bases(targets) == ["test"]

    def test_force_selects_every_md(self, tmp_path: Path):
        md_dir, html_dir = _make_dirs(tmp_path)
        for name in ["a", "b", "c"]:
            (md_dir / f"{name}.md").write_text(f"# {name}\n", encoding="utf-8")
            (html_dir / f"{name}.html").write_text("<html></html>", encoding="utf-8")

        rels = make_mod.collect_markdown(md_dir)
        targets = make_mod.select_targets(md_dir, html_dir, rels, force=True)
        assert _bases(targets) == ["a", "b", "c"]
