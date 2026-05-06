"""Validate about/cases.json against about/cases.schema.json.

Exit code:
  0 ... valid
  1 ... invalid (prints all errors to stderr)

Usage:
  uv run python3 scripts/validate_cases.py
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "about" / "cases.json"
SCHEMA_PATH = ROOT / "about" / "cases.schema.json"


def main() -> int:
    errors: list[str] = []

    try:
        data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"❌ {DATA_PATH.name}: JSON構文エラー — {e.msg} (line {e.lineno}, col {e.colno})", file=sys.stderr)
        return 1

    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"❌ {SCHEMA_PATH.name}: JSON構文エラー — {e.msg}", file=sys.stderr)
        return 1

    validator = Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
        path = "/".join(str(p) for p in err.absolute_path) or "(root)"
        errors.append(f"❌ {path}: {err.message}")

    cases = data.get("cases", [])
    if isinstance(cases, list):
        nos = [c.get("no") for c in cases if isinstance(c, dict) and "no" in c]
        dupes = [n for n, count in Counter(nos).items() if count > 1]
        if dupes:
            errors.append(f"❌ cases: no が重複しています → {sorted(dupes)}")

    if errors:
        print(f"\n{len(errors)} 件のバリデーションエラー:\n", file=sys.stderr)
        for msg in errors:
            print(f"  {msg}", file=sys.stderr)
        print("", file=sys.stderr)
        return 1

    print(f"✅ {DATA_PATH.name}: {len(cases)} 件の事例、すべて有効です。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
