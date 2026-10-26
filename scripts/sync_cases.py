"""Regenerate about/cases.json from the case-list spreadsheet.

The spreadsheet "[随時更新] PWSCUP関連の記事・ブログ・プレスリリース一覧" is the
single source of truth. Columns are looked up by header name:

  項番 公開年 記事分類 区分 記事タイトル 掲載元 URL 受賞 タイプ 年度テーマ テーマ補足

- Rows whose 項番 is blank are drafts and are skipped.
- 記事分類 must look like "PWS Cup 2026"; the year becomes cup_year.
- タイプ is one of 公式 / 企業 / 大学 / 論文 / ブログ / コード / その他.
- A row with 年度テーマ provides that cup_year's theme (at most one per year).
  The theme links to the row's URL.

On any error nothing is written and the exit code is 1.

Usage:
  uv run python3 scripts/sync_cases.py                 # fetch the sheet
  uv run python3 scripts/sync_cases.py --csv sheet.csv # use a local CSV
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import re
import sys
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "about" / "cases.json"

SHEET_ID = "1xfBD17rjLFy9ZPg381ghcHnvk1cu1tw_k1Y6EK3krOk"
DEFAULT_CSV_URL = (
    f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid=0"
)

COLUMNS = {
    "no": "項番",
    "year": "公開年",
    "cup": "記事分類",
    "category": "区分",
    "title": "記事タイトル",
    "source": "掲載元",
    "url": "URL",
    "award": "受賞",
    "type": "タイプ",
    "theme": "年度テーマ",
    "theme_desc": "テーマ補足",
}

TYPES = {
    "公式": "official",
    "企業": "company",
    "大学": "university",
    "論文": "paper",
    "ブログ": "blog",
    "コード": "code",
    "コード・リポジトリ": "code",
    "その他": "other",
}

CASE_KEYS = ["no", "year", "cup_year", "category", "title", "source", "type"]
CASE_KEYS += ["award", "url"]


def clean(value: str | None) -> str:
    """Collapse in-cell line breaks and surrounding whitespace."""
    return re.sub(r"\s*\n\s*", "", value or "").strip()


def parse_int(text: str) -> int | None:
    return int(text) if re.fullmatch(r"\d+", text) else None


def parse_rows(
    rows: list[list[str]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str], int]:
    """Convert sheet rows to (cases, themes, errors, skipped_drafts)."""
    errors: list[str] = []
    if not rows:
        return [], [], ["シートが空です"], 0

    header = [clean(h) for h in rows[0]]
    missing = [name for name in COLUMNS.values() if name not in header]
    if missing:
        return [], [], [f"列が見つかりません → {', '.join(missing)}"], 0
    idx = {key: header.index(name) for key, name in COLUMNS.items()}

    cases: list[dict[str, Any]] = []
    themes: dict[int, dict[str, Any]] = {}
    theme_rows: dict[int, int] = {}
    seen_nos: dict[int, int] = {}
    skipped = 0

    for line, raw in enumerate(rows[1:], start=2):
        cell = {key: clean(raw[i]) if i < len(raw) else "" for key, i in idx.items()}
        if not any(cell.values()):
            continue
        if not cell["no"]:
            skipped += 1
            continue

        where = f"{line}行目（項番 {cell['no']}）"
        row_errors: list[str] = []

        no = parse_int(cell["no"])
        if no is None:
            row_errors.append("項番が整数ではありません")
        elif no in seen_nos:
            row_errors.append(f"項番が {seen_nos[no]}行目と重複しています")

        year = parse_int(cell["year"])
        if year is None:
            row_errors.append("公開年が整数ではありません")

        m = re.fullmatch(r"PWS\s*Cup\s*(\d{4})", cell["cup"], re.IGNORECASE)
        cup_year = int(m.group(1)) if m else None
        if cup_year is None:
            row_errors.append("記事分類は「PWS Cup 2026」の形で書いてください")

        for key in ("category", "title", "source"):
            if not cell[key]:
                row_errors.append(f"{COLUMNS[key]}が空です")

        type_ = TYPES.get(cell["type"])
        if type_ is None:
            choices = " / ".join(k for k in TYPES if k != "コード・リポジトリ")
            row_errors.append(f"タイプは {choices} のいずれかにしてください")

        if cell["url"] and not re.match(r"https?://", cell["url"]):
            row_errors.append("URL は http(s):// で始めてください")

        if cell["theme_desc"] and not cell["theme"]:
            row_errors.append("テーマ補足だけがあり、年度テーマが空です")
        if cell["theme"] and cup_year is not None and cup_year in theme_rows:
            row_errors.append(
                f"{cup_year}年の年度テーマが {theme_rows[cup_year]}行目にもあります"
            )

        if row_errors:
            errors.extend(f"{where}: {msg}" for msg in row_errors)
            continue

        assert no is not None and year is not None and cup_year is not None
        seen_nos[no] = line
        case = {
            "no": no,
            "year": year,
            "cup_year": cup_year,
            "category": cell["category"],
            "title": cell["title"],
            "source": cell["source"],
            "type": type_,
            "award": cell["award"],
            "url": cell["url"],
        }
        cases.append({k: case[k] for k in CASE_KEYS if case[k] != ""})

        if cell["theme"]:
            theme_rows[cup_year] = line
            theme = {
                "year": cup_year,
                "title": cell["theme"],
                "description": cell["theme_desc"],
                "url": cell["url"],
            }
            themes[cup_year] = {k: v for k, v in theme.items() if v != ""}

    cases.sort(key=lambda c: c["no"])
    return cases, [themes[y] for y in sorted(themes)], errors, skipped


def render(themes: list[dict[str, Any]], cases: list[dict[str, Any]]) -> str:
    """Match the hand-written layout: indented themes, one case per line."""
    theme_json = json.dumps(themes, ensure_ascii=False, indent=2)
    theme_json = theme_json.replace("\n", "\n  ")
    case_lines = ",\n".join(
        "    " + json.dumps(c, ensure_ascii=False, separators=(",", ":")) for c in cases
    )
    return f'{{\n  "themes": {theme_json},\n  "cases": [\n{case_lines}\n  ]\n}}\n'


def fetch_csv(url: str) -> str:
    with urllib.request.urlopen(url, timeout=30) as res:
        return res.read().decode("utf-8-sig")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--csv", type=Path, help="シートを取得せずにこの CSV を使う")
    parser.add_argument("--out", type=Path, default=DATA_PATH)
    args = parser.parse_args()

    if args.csv:
        text = args.csv.read_text(encoding="utf-8-sig")
    else:
        url = os.environ.get("CASES_SHEET_CSV_URL", DEFAULT_CSV_URL)
        try:
            text = fetch_csv(url)
        except OSError as e:
            print(f"❌ シートを取得できませんでした — {e}", file=sys.stderr)
            return 1

    cases, themes, errors, skipped = parse_rows(list(csv.reader(io.StringIO(text))))
    if errors:
        summary = f"{len(errors)} 件のエラー（cases.json は更新していません）"
        print(f"\n{summary}:\n", file=sys.stderr)
        for msg in errors:
            print(f"  ❌ {msg}", file=sys.stderr)
        print("", file=sys.stderr)
        return 1
    if not cases:
        print("❌ 公開対象の行が1件もありません", file=sys.stderr)
        return 1

    args.out.write_text(render(themes, cases), encoding="utf-8")
    print(
        f"✅ {args.out.name}: 事例 {len(cases)} 件・"
        f"年度テーマ {len(themes)} 件を書き出しました"
        f"（項番が空の下書き {skipped} 行はスキップ）"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
