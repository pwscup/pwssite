#!/usr/bin/env python3
"""Build HTML for a single target directory."""

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


def build_target(target_dir: Path) -> int:
    """Build all markdown files in target_dir."""
    md_dir = target_dir / "markdown"
    html_dir = target_dir / "html"
    public_dir = target_dir

    html_dir.mkdir(parents=True, exist_ok=True)

    rel_md_list = collect_markdown(md_dir)

    targets: list[tuple[str, Path]] = []
    for rel in rel_md_list:
        base = rel.stem
        md = md_dir / rel
        html = html_dir / f"{base}.html"
        if (not html.exists()) or (md.stat().st_mtime > html.stat().st_mtime):
            targets.append((base, md))

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
    if len(sys.argv) != 2:
        print("Usage: make.py <target_dir>")
        return 1

    target_dir = Path(sys.argv[1]).resolve()
    return build_target(target_dir)


if __name__ == "__main__":
    sys.exit(main())
