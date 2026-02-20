"""Integration tests: full build pipeline."""

import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


def run_build(script: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(script)],
        capture_output=True,
        text=True,
    )


class TestPpsdBuild:
    def test_build_succeeds(self):
        result = run_build(REPO_ROOT / "ppsd" / "scripts" / "make.py")
        assert result.returncode == 0

    def test_html_generated(self):
        run_build(REPO_ROOT / "ppsd" / "scripts" / "make.py")
        html = REPO_ROOT / "ppsd" / "index.html"
        assert html.exists()
        content = html.read_text(encoding="utf-8")
        assert "<!-- contents start -->" in content
        assert "<!-- contents end -->" in content

    def test_html_has_title(self):
        run_build(REPO_ROOT / "ppsd" / "scripts" / "make.py")
        html = REPO_ROOT / "ppsd" / "index.html"
        content = html.read_text(encoding="utf-8")
        assert "<title>" in content


class Test2026Build:
    def test_build_succeeds(self):
        result = run_build(REPO_ROOT / "2026" / "scripts" / "make.py")
        assert result.returncode == 0

    def test_html_generated(self):
        run_build(REPO_ROOT / "2026" / "scripts" / "make.py")
        html = REPO_ROOT / "2026" / "index.html"
        assert html.exists()
        content = html.read_text(encoding="utf-8")
        assert "<!-- contents start -->" in content
        assert "<!-- contents end -->" in content


class TestRootMakePy:
    def test_build_succeeds(self):
        result = run_build(REPO_ROOT / "make.py")
        assert result.returncode == 0

    def test_both_directories_built(self):
        run_build(REPO_ROOT / "make.py")
        assert (REPO_ROOT / "2026" / "index.html").exists()
        assert (REPO_ROOT / "ppsd" / "index.html").exists()
