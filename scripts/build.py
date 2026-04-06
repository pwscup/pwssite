#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys
import unicodedata

from markdown_it import MarkdownIt
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.tasklists import tasklists_plugin


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


def build_header(target_dir: Path, base: str, title: str) -> str:
    if base.endswith("_e"):
        header1 = read_text(target_dir / "template/header_e.html")
        header2 = read_text(target_dir / "template/header_afterTitle_e.html")
    else:
        header1 = read_text(target_dir / "template/header.html")
        header2 = read_text(target_dir / "template/header_afterTitle.html")
    return f"{header1}    <title>{title}</title>\n{header2}"


def _slugify(text: str) -> str:
    """Generate a slug suitable for use as an HTML id attribute."""
    text = unicodedata.normalize("NFC", text)
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s]+", "-", text).strip("-")
    return text


def _collect_headings(tokens: list) -> list[tuple[int, str, str]]:
    """Walk markdown-it tokens and return (level, id, text) for h2-h6."""
    headings: list[tuple[int, str, str]] = []
    slug_counts: dict[str, int] = {}
    counter = 0
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if tok.type == "heading_open":
            level = int(tok.tag[1])  # e.g. "h2" -> 2
            # Collect inline text from the next token
            inline_tok = tokens[i + 1] if i + 1 < len(tokens) else None
            text = ""
            if inline_tok and inline_tok.children:
                text = "".join(
                    child.content for child in inline_tok.children
                    if child.type in ("text", "code_inline")
                )
            if level >= 2:
                slug = _slugify(text)
                if not slug:
                    counter += 1
                    slug = f"_{counter}"
                else:
                    count = slug_counts.get(slug, 0)
                    if count:
                        slug = f"{slug}-{count}"
                    slug_counts[slug.split("-")[0] if "-" in slug else slug] = count + 1
                headings.append((level, slug, text))
                # Inject id into the heading_open token
                tok.attrSet("id", slug)
        i += 1
    return headings


def _build_toc_html(headings: list[tuple[int, str, str]]) -> str:
    """Build a nested TOC HTML string matching the old Markdown TOC format."""
    if not headings:
        return ""
    lines: list[str] = ['<div class="toc">', "<ul>"]
    base_level = headings[0][0]
    prev_level = base_level

    for level, slug, text in headings:
        if level > prev_level:
            # Open nested lists
            for _ in range(level - prev_level):
                lines.append("<ul>")
        elif level < prev_level:
            # Close nested lists and their parent items
            for _ in range(prev_level - level):
                lines.append("</li>")
                lines.append("</ul>")
            # Close the sibling item at the current level
            lines.append("</li>")
        else:
            # Same level — close previous item
            if lines[-1] != "<ul>":
                lines.append("</li>")
        lines.append(f'<li><a href="#{slug}">{text}</a>')
        prev_level = level

    # Close all remaining open tags
    for _ in range(prev_level - base_level):
        lines.append("</li>")
        lines.append("</ul>")
    lines.append("</li>")
    lines.append("</ul>")
    lines.append("</div>")
    return "\n".join(lines)


def build_body(md_text: str) -> tuple[str, str]:
    md = MarkdownIt("commonmark", {"html": True}).enable(["table", "strikethrough"])
    footnote_plugin(md)
    tasklists_plugin(md)

    tokens = md.parse(md_text)
    headings = _collect_headings(tokens)
    toc_html = _build_toc_html(headings)

    html_body = md.render(md_text)
    for level, slug, text in headings:
        pattern = f"<h{level}>"
        replacement = f'<h{level} id="{slug}">'
        html_body = html_body.replace(pattern, replacement, 1)

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


def build_page(target_dir: Path, base: str) -> None:
    """Build a single page: markdown -> HTML."""
    md_path = target_dir / "markdown" / f"{base}.md"
    html_dir = target_dir / "html"
    html_dir.mkdir(parents=True, exist_ok=True)
    output_path = html_dir / f"{base}.html"
    footer_path = target_dir / "template" / "footer.html"

    if not md_path.exists():
        raise FileNotFoundError(f"markdown not found: {md_path}")

    title = extract_title(md_path)
    header = build_header(target_dir, base, title)
    md_text = read_text(md_path)
    toc_html, html_body = build_body(md_text)
    footer = read_text(footer_path)

    parts: list[str] = [header, "<!-- contents start -->"]
    parts.append(insert_toc_after_whats_new(html_body, toc_html))
    parts.append("<!-- contents end -->")
    parts.append(footer)

    output_path.write_text("\n".join(parts) + "\n", encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: pandoc.py <target_dir> <base_filename>")
        return 1

    target_dir = Path(sys.argv[1]).resolve()
    base = sys.argv[2]

    try:
        build_page(target_dir, base)
    except FileNotFoundError as e:
        print(f"[ERROR] {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
