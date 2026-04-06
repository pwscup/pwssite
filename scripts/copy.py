#!/usr/bin/env python3
"""新年度ディレクトリ作成用スクリプト"""

import os
import shutil
import subprocess
import sys
from pathlib import Path


def get_repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def copy_directory_structure(src: Path, dst: Path) -> None:
    """ディレクトリ構造のみをコピー (scripts/ は除外)"""
    for dirpath, dirnames, _ in os.walk(src):
        relative = Path(dirpath).relative_to(src)
        # scripts/ は共通化済みなのでコピーしない
        if relative.parts and relative.parts[0] == "scripts":
            continue
        target = dst / relative
        target.mkdir(parents=True, exist_ok=True)


def copy_common_files(src: Path, dst: Path) -> None:
    """共通ファイルのコピー"""
    # style.css
    shutil.copy2(src / "style.css", dst / "style.css")

    # template/*
    for f in (src / "template").iterdir():
        if f.is_file():
            shutil.copy2(f, dst / "template" / f.name)

    # markdown/index.md
    shutil.copy2(src / "markdown" / "index.md", dst / "markdown" / "index.md")


def clean_index_md(dst: Path) -> None:
    """index.md を見出し構造だけ残して内容を TBD にする"""
    md_path = dst / "markdown" / "index.md"
    lines = md_path.read_text(encoding="utf-8").splitlines()

    cleaned: list[str] = []
    for line in lines:
        if line.startswith("# "):
            cleaned.append("# TBD")
            cleaned.append("")
        elif line.startswith("## "):
            cleaned.append(line)
            cleaned.append("TBD")
            cleaned.append("")

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


def run_build_test(repo_root: Path, target: str) -> None:
    """scripts/make.py を実行してビルドテスト"""
    make_script = repo_root / "scripts" / "make.py"
    target_dir = repo_root / target
    result = subprocess.run(
        [sys.executable, str(make_script), str(target_dir)],
        capture_output=True,
        text=True,
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="")
    if result.returncode != 0:
        print(
            f"ビルドテストが失敗しました (終了コード: {result.returncode})",
            file=sys.stderr,
        )
        sys.exit(result.returncode)


def main() -> None:
    if len(sys.argv) != 3:
        print("新規ディレクトリ作成スクリプト", file=sys.stderr)
        print("", file=sys.stderr)
        print(
            f"使い方: python {sys.argv[0]} <参照元フォルダ名> <新規フォルダ名>",
            file=sys.stderr,
        )
        print("", file=sys.stderr)
        print("例:", file=sys.stderr)
        print("  python scripts/copy.py 2026 2027", file=sys.stderr)
        print("    → 2026/ を元に 2027/ を作成", file=sys.stderr)
        sys.exit(1)

    template_name = sys.argv[1]
    target_name = sys.argv[2]
    repo_root = get_repo_root()
    src = repo_root / template_name
    dst = repo_root / target_name

    if not src.is_dir():
        print(f"参照元ディレクトリ {template_name} が見つかりません。", file=sys.stderr)
        sys.exit(1)

    if dst.exists():
        print(f"{target_name} directory already exists.")
        sys.exit(1)

    print(f"{template_name}/ を元に {target_name}/ を作成します")
    print()

    print(f"[1/5] ディレクトリ構造をコピー: {template_name}/ → {target_name}/")
    copy_directory_structure(src, dst)

    print("[2/5] 共通ファイルをコピー (style.css, template/*, markdown/index.md)")
    copy_common_files(src, dst)

    print("[3/5] index.md を初期化 (見出し構造のみ残す)")
    clean_index_md(dst)

    print("[4/5] html/ にプレースホルダを作成")
    create_html_placeholder(dst)

    print()
    print(f"[5/5] ビルドテスト: scripts/make.py {target_name} を実行")
    print("-" * 40)
    run_build_test(repo_root, target_name)
    print("-" * 40)
    print("[5/5] ビルドテスト完了")

    print()
    print(f"完了: {target_name}/ を作成しました")
    print(
        "※ pyproject.toml の [tool.pwssite] targets に"
        f' "{target_name}" を追加してください'
    )


if __name__ == "__main__":
    main()
