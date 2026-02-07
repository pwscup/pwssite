#!/usr/bin/env python3
from pathlib import Path
import shutil
import subprocess
import sys


def collect_markdown(md_dir: Path) -> list[Path]:
    rels: list[Path] = []
    for path in sorted(md_dir.rglob("*.md")):
        if path.is_file():
            rels.append(path.relative_to(md_dir))
    return rels


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    md_dir = (script_dir / "../markdown").resolve()
    html_dir = (script_dir / "../html").resolve()
    public_dir = md_dir.parent.resolve()

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

    for base, _ in targets:
        html = html_dir / f"{base}.html"

        print(f"[BUILD] {base}.md -> {base}.html")
        subprocess.run(
            ["bash", str(script_dir / "pandoc.bash"), base],
            check=True,
        )

        tidy_result = subprocess.run(
            ["tidy", "-quiet", "-indent", "-utf8", "-m", str(html)],
            check=False,
        )
        if tidy_result.returncode != 0:
            print("[WARN] tidy reported issues; continuing")

        html.chmod(0o660)

        dest = public_dir / f"{base}.html"
        print(f"[COPY] {html} -> {dest}")
        shutil.copy2(html, dest)

    images_dir = md_dir / "Images"
    if images_dir.is_dir():
        subprocess.run(
            [
                "rsync",
                "-rt",
                "--delete",
                "--chmod=Du=rwx,Dg=rwx,Fu=rw,Fg=rw",
                f"{images_dir}/",
                f"{(html_dir / 'Images')}/",
            ],
            check=True,
        )

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
