#!/usr/bin/env python3
"""Build HTML for a single target directory."""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def collect_markdown(md_dir: Path) -> list[Path]:
    rels: list[Path] = []
    for path in sorted(md_dir.rglob("*.md")):
        if path.is_file():
            rels.append(path.relative_to(md_dir))
    return rels


def select_targets(
    md_dir: Path,
    html_dir: Path,
    rel_md_list: list[Path],
    force: bool = False,
) -> list[tuple[str, Path]]:
    """Pick the markdown files that need building.

    With force=True every markdown file is selected. Otherwise a file is
    selected only when its HTML is missing or older, which relies on mtime.
    git does not record mtime, so the order after a fresh checkout is not
    deterministic and the comparison may silently skip everything. CI must
    therefore pass force=True.
    """
    targets: list[tuple[str, Path]] = []
    for rel in rel_md_list:
        base = rel.stem
        md = md_dir / rel
        html = html_dir / f"{base}.html"
        if force or (not html.exists()) or (md.stat().st_mtime > html.stat().st_mtime):
            targets.append((base, md))
    return targets


def build_target(target_dir: Path, force: bool = False) -> int:
    """Build all markdown files in target_dir."""
    md_dir = target_dir / "markdown"
    html_dir = target_dir / "html"
    public_dir = target_dir

    html_dir.mkdir(parents=True, exist_ok=True)

    rel_md_list = collect_markdown(md_dir)
    targets = select_targets(md_dir, html_dir, rel_md_list, force=force)

    if not targets:
        print("No markdown newer than existing HTML.")
        return 0

    print("Build targets:")
    for base, _ in targets:
        print(f"  {base}.md")
    print("----------------------------------------")

    scripts_dir = Path(__file__).resolve().parent

    for base, _ in targets:
        html = html_dir / f"{base}.html"

        print(f"[BUILD] {base}.md -> {base}.html")
        subprocess.run(
            [sys.executable, str(scripts_dir / "build.py"), str(target_dir), base],
            check=True,
        )

        html.chmod(0o660)

        dest = public_dir / f"{base}.html"
        print(f"[COPY] {html} -> {dest}")
        shutil.copy2(html, dest)

    images_dir = md_dir / "Images"
    if images_dir.is_dir():
        for dest_images in [html_dir / "Images", public_dir / "Images"]:
            subprocess.run(
                [
                    "rsync",
                    "-rt",
                    "--delete",
                    "--chmod=Du=rwx,Dg=rwx,Fu=rw,Fg=rw",
                    f"{images_dir}/",
                    f"{dest_images}/",
                ],
                check=True,
            )

    print("Done.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build HTML for a single target directory."
    )
    parser.add_argument("target_dir", help="target directory (e.g. 2026)")
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="rebuild every markdown file, ignoring mtime comparison",
    )
    args = parser.parse_args()

    return build_target(Path(args.target_dir).resolve(), force=args.force)


if __name__ == "__main__":
    sys.exit(main())
