from pathlib import Path

import pytest


@pytest.fixture
def repo_root() -> Path:
    """Repository root directory."""
    return Path(__file__).resolve().parent.parent


@pytest.fixture
def template_dir_2026(repo_root: Path) -> Path:
    return repo_root / "2026" / "template"


@pytest.fixture
def template_dir_ppsd(repo_root: Path) -> Path:
    return repo_root / "ppsd" / "template"


@pytest.fixture
def tmp_markdown(tmp_path: Path) -> Path:
    """Create a temporary markdown directory with a sample file."""
    md_dir = tmp_path / "markdown"
    md_dir.mkdir()
    sample = md_dir / "sample.md"
    sample.write_text("# Sample Title\n\n## Section 1\nHello world\n", encoding="utf-8")
    return md_dir
