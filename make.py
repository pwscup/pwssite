#!/usr/bin/env python3
"""Build entry point: reads targets from pyproject.toml and builds each."""

from pathlib import Path
import subprocess
import sys

import tomllib


def main() -> int:
    root = Path(__file__).resolve().parent
    pyproject = root / "pyproject.toml"

    with pyproject.open("rb") as f:
        config = tomllib.load(f)

    targets = config.get("tool", {}).get("pwssite", {}).get("targets", [])
    if not targets:
        print("[WARN] No targets defined in pyproject.toml [tool.pwssite].targets")
        return 0

    scripts_make = root / "scripts" / "make.py"

    for target_name in targets:
        target_dir = root / target_name
        print(f"=== {target_name} ===")
        result = subprocess.run(
            [sys.executable, str(scripts_make), str(target_dir)],
        )
        if result.returncode != 0:
            print(f"[ERROR] {target_name} failed (exit {result.returncode})")
            return result.returncode

    return 0


if __name__ == "__main__":
    sys.exit(main())
