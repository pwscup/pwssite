#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import sys

from markdown import Markdown


DEFAULT_TITLE = "PWS"


def extract_title(md_path: Path) -> str:
    try:
        with md_path.open("r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("# "):
                    title = line[2:].strip()
                    if title:
                        return title
                    break
    except FileNotFoundError:
        return DEFAULT_TITLE
    return DEFAULT_TITLE


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def build_header(script_dir: Path, base: str, title: str) -> str:
    if base.endswith("_e"):
        header1 = read_text(script_dir / "../template/header_e.html")
        header2 = read_text(script_dir / "../template/header_afterTitle_e.html")
    else:
        header1 = read_text(script_dir / "../template/header.html")
        header2 = read_text(script_dir / "../template/header_afterTitle.html")
    return f"{header1}    <title>{title}</title>\n{header2}"


def build_body(md_text: str) -> tuple[str, str]:
    md = Markdown(
        extensions=["tables", "footnotes", "toc", "fenced_code"],
        extension_configs={
            "toc": {"toc_depth": "2-6"},
        },
    )
    html_body = md.convert(md_text)
    toc_html = md.toc or ""
    if "<li>" not in toc_html:
        toc_html = ""
    return toc_html, html_body


def insert_toc_after_whats_new(html_body: str, toc_html: str) -> str:
    if not toc_html:
        return html_body
    title_marker = "What's new</h2>"
    title_pos = html_body.find(title_marker)
    idx = -1
    if title_pos != -1:
        idx = html_body.rfind("<h2", 0, title_pos)
    toc_block = "\n<h2>目次</h2>\n" + toc_html
    if idx == -1:
        # Fallback: after first paragraph following h1 if possible
        h1_end = html_body.find("</h1>")
        if h1_end == -1:
            return toc_block + "\n" + html_body
        p_end = html_body.find("</p>", h1_end)
        insert_at = p_end + len("</p>") if p_end != -1 else h1_end + len("</h1>")
        return html_body[:insert_at] + toc_block + html_body[insert_at:]
    # Insert after the What's new section content (before next h2)
    next_h2 = html_body.find("<h2", title_pos + len(title_marker))
    insert_at = next_h2 if next_h2 != -1 else len(html_body)
    return html_body[:insert_at] + toc_block + html_body[insert_at:]


def convert_md_to_html(base: str, script_dir: Path) -> int:
    md_path = (script_dir / f"../markdown/{base}.md").resolve()
    html_dir = (script_dir / "../html").resolve()
    html_dir.mkdir(parents=True, exist_ok=True)
    output_path = (script_dir / f"../html/{base}.html").resolve()
    footer_path = (script_dir / "../template/footer.html").resolve()

    if not md_path.exists():
        print(f"[ERROR] markdown not found: {md_path}")
        return 1

    title = extract_title(md_path)
    header = build_header(script_dir, base, title)
    md_text = read_text(md_path)
    toc_html, html_body = build_body(md_text)
    footer = read_text(footer_path)

    parts: list[str] = [header, "<!-- contents start -->"]
    parts.append(insert_toc_after_whats_new(html_body, toc_html))
    parts.append("<!-- contents end -->")
    parts.append(footer)

    output_path.write_text("\n".join(parts) + "\n", encoding="utf-8")
    return 0


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
        result = convert_md_to_html(base, script_dir)
        if result != 0:
            return result

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
