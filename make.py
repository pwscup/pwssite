#!/usr/bin/env python3
"""2026 / ppsd のビルドエントリポイント

2025 以前の bash ベースのビルドは make.bash を使用してください。
"""

from pathlib import Path
import subprocess
import sys


def main() -> int:
    root = Path(__file__).resolve().parent
    targets = [
        root / "2026" / "scripts" / "make.py",
        root / "ppsd" / "scripts" / "make.py",
    ]

    for script in targets:
        print(f"=== {script.relative_to(root)} ===")
        result = subprocess.run([sys.executable, str(script)])
        if result.returncode != 0:
            print(f"[ERROR] {script.relative_to(root)} failed (exit {result.returncode})")
            return result.returncode

    return 0


if __name__ == "__main__":
    sys.exit(main())
