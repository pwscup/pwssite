#!/usr/bin/env python3
"""新年度ディレクトリ作成用スクリプト (copy.bash の Python 版)"""

import os
import sys
import shutil
import subprocess
from pathlib import Path



def get_script_dir() -> Path:
    return Path(__file__).resolve().parent


def copy_directory_structure(src: Path, dst: Path) -> None:
    """ディレクトリ構造のみをコピー (rsync --include "*/" --exclude "*" 相当)"""
    for dirpath, dirnames, _ in os.walk(src):
        relative = Path(dirpath).relative_to(src)
        target = dst / relative
        target.mkdir(parents=True, exist_ok=True)


def copy_common_files(script_dir: Path, template: str, target: str) -> None:
    """共通ファイルのコピー"""
    src = script_dir / template
    dst = script_dir / target

    # style.css
    shutil.copy2(src / "style.css", dst / "style.css")

    # template/*
    for f in (src / "template").iterdir():
        if f.is_file():
            shutil.copy2(f, dst / "template" / f.name)

    # scripts/*
    for f in (src / "scripts").iterdir():
        if f.is_file():
            shutil.copy2(f, dst / "scripts" / f.name)

    # markdown/index.md
    shutil.copy2(src / "markdown" / "index.md", dst / "markdown" / "index.md")


def clean_index_md(dst: Path) -> None:
    """index.md を見出し構造だけ残して内容を TBD にする"""
    md_path = dst / "markdown" / "index.md"
    lines = md_path.read_text(encoding="utf-8").splitlines()

    cleaned: list[str] = []
    for line in lines:
        if line.startswith("# "):
            # h1: 見出し自体を TBD に
            cleaned.append("# TBD")
            cleaned.append("")
        elif line.startswith("## "):
            # h2: 見出しテキストは残し、内容を TBD に
            cleaned.append(line)
            cleaned.append("TBD")
            cleaned.append("")
        # h2 以下の本文・h3 等はすべて捨てる

    md_path.write_text("\n".join(cleaned) + "\n", encoding="utf-8")


def create_html_placeholder(dst: Path) -> None:
    """html ディレクトリとプレースホルダの作成"""
    html_dir = dst / "html"
    html_dir.mkdir(exist_ok=True)
    (html_dir / "tmp.txt").touch()


def place_gitkeep(dst: Path) -> None:
    """空ディレクトリに .gitkeep を配置して Git 管理対象にする"""
    for dirpath, dirnames, filenames in os.walk(dst):
        if not dirnames and not filenames:
            (Path(dirpath) / ".gitkeep").touch()


def run_build_test(script_dir: Path, target: str) -> None:
    """make.py を実行してビルドテスト"""
    make_script = script_dir / target / "scripts" / "make.py"
    result = subprocess.run(
        [sys.executable, str(make_script)],
        capture_output=True, text=True,
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="")
    if result.returncode != 0:
        print(f"ビルドテストが失敗しました (終了コード: {result.returncode})", file=sys.stderr)
        sys.exit(result.returncode)


def main() -> None:
    if len(sys.argv) != 3:
        print("新規ディレクトリ作成スクリプト", file=sys.stderr)
        print("", file=sys.stderr)
        print(f"使い方: python {sys.argv[0]} <参照元フォルダ名> <新規フォルダ名>", file=sys.stderr)
        print("", file=sys.stderr)
        print("例:", file=sys.stderr)
        print("  python copy.py 2026 2027", file=sys.stderr)
        print("    → 2026/ を元に 2027/ を作成", file=sys.stderr)
        print("  python copy.py 2026 ipws2027", file=sys.stderr)
        print("    → 2026/ を元に ipws2027/ を作成", file=sys.stderr)
        sys.exit(1)

    template_year = sys.argv[1]
    target_year = sys.argv[2]
    script_dir = get_script_dir()
    src = script_dir / template_year
    dst = script_dir / target_year

    if not src.is_dir():
        print(f"参照元ディレクトリ {template_year} が見つかりません。", file=sys.stderr)
        sys.exit(1)

    if dst.exists():
        print(f"{target_year} directory already exists.")
        sys.exit(1)

    print(f"{template_year}/ を元に {target_year}/ を作成します")
    print()

    print(f"[1/6] ディレクトリ構造をコピー: {template_year}/ → {target_year}/")
    copy_directory_structure(src, dst)

    print(f"[2/6] 共通ファイルをコピー (style.css, template/*, scripts/*, markdown/index.md)")
    copy_common_files(script_dir, template_year, target_year)

    print(f"[3/6] index.md を初期化 (見出し構造のみ残す)")
    clean_index_md(dst)

    print(f"[4/6] html/ にプレースホルダを作成")
    create_html_placeholder(dst)

    print()
    print(f"[5/6] ビルドテスト: {target_year}/scripts/make.py を実行")
    print("-" * 40)
    run_build_test(script_dir, target_year)
    print("-" * 40)
    print(f"[5/6] ビルドテスト完了")

    print(f"[6/6] 空ディレクトリに .gitkeep を配置")
    place_gitkeep(dst)

    print()
    print(f"完了: {target_year}/ を作成しました")


if __name__ == "__main__":
    main()
