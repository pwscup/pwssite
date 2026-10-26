"""Tests for scripts/sync_cases.py."""

import json
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import sync_cases  # noqa: E402

HEADER = list(sync_cases.COLUMNS.values())


def row(no="1", cup="PWS Cup 2025", type_="公式", theme="", theme_desc="", **kw):
    cells = {
        "項番": no,
        "公開年": kw.get("year", "2025"),
        "記事分類": cup,
        "区分": kw.get("category", "公式ページ"),
        "記事タイトル": kw.get("title", "PWS Cup 2025"),
        "掲載元": kw.get("source", "PWS公式"),
        "URL": kw.get("url", "https://www.iwsec.org/pws/2025/cup25.html"),
        "受賞": kw.get("award", ""),
        "タイプ": type_,
        "年度テーマ": theme,
        "テーマ補足": theme_desc,
    }
    return [cells[h] for h in HEADER]


class TestParseRows:
    def test_basic_row(self):
        cases, themes, errors, skipped = sync_cases.parse_rows([HEADER, row()])
        assert errors == []
        assert cases == [
            {
                "no": 1,
                "year": 2025,
                "cup_year": 2025,
                "category": "公式ページ",
                "title": "PWS Cup 2025",
                "source": "PWS公式",
                "type": "official",
                "url": "https://www.iwsec.org/pws/2025/cup25.html",
            }
        ]
        assert themes == []

    def test_blank_no_is_draft(self):
        rows = [HEADER, row(), row(no=""), [""] * 6 + ["https://example.com"]]
        cases, _, errors, skipped = sync_cases.parse_rows(rows)
        assert errors == []
        assert len(cases) == 1
        assert skipped == 2

    def test_empty_rows_ignored(self):
        _, _, errors, skipped = sync_cases.parse_rows([HEADER, row(), [""] * 11, []])
        assert errors == []
        assert skipped == 0

    def test_in_cell_newline_removed(self):
        rows = [HEADER, row(title="参加記〜\n")]
        cases, _, _, _ = sync_cases.parse_rows(rows)
        assert cases[0]["title"] == "参加記〜"

    def test_other_type(self):
        cases, _, errors, _ = sync_cases.parse_rows([HEADER, row(type_="その他")])
        assert errors == []
        assert cases[0]["type"] == "other"

    def test_award_kept(self):
        cases, _, _, _ = sync_cases.parse_rows([HEADER, row(award="総合優勝")])
        assert cases[0]["award"] == "総合優勝"

    def test_theme_from_row(self):
        rows = [HEADER, row(theme="テーマ", theme_desc="補足")]
        _, themes, errors, _ = sync_cases.parse_rows(rows)
        assert errors == []
        assert themes == [
            {
                "year": 2025,
                "title": "テーマ",
                "description": "補足",
                "url": "https://www.iwsec.org/pws/2025/cup25.html",
            }
        ]

    def test_missing_column(self):
        _, _, errors, _ = sync_cases.parse_rows([HEADER[:7], row()[:7]])
        assert len(errors) == 1
        assert "受賞" in errors[0] and "タイプ" in errors[0]

    def test_row_errors_collected(self):
        rows = [
            HEADER,
            row(no="1"),
            row(no="1"),
            row(no="x"),
            row(no="4", cup="2025"),
            row(no="5", type_="企業公式"),
            row(no="6", url="example.com"),
            row(no="7", theme_desc="補足だけ"),
        ]
        _, _, errors, _ = sync_cases.parse_rows(rows)
        assert len(errors) == 6
        assert "3行目" in errors[0] and "重複" in errors[0]

    def test_duplicate_theme_year(self):
        rows = [HEADER, row(no="1", theme="A"), row(no="2", theme="B")]
        _, _, errors, _ = sync_cases.parse_rows(rows)
        assert len(errors) == 1
        assert "2025年の年度テーマ" in errors[0]

    def test_sorted_by_no(self):
        cases, _, _, _ = sync_cases.parse_rows([HEADER, row(no="3"), row(no="2")])
        assert [c["no"] for c in cases] == [2, 3]


class TestRender:
    def test_matches_current_layout(self, repo_root: Path):
        path = repo_root / "about" / "cases.json"
        text = path.read_text(encoding="utf-8")
        data = json.loads(text)
        assert sync_cases.render(data["themes"], data["cases"]) == text
