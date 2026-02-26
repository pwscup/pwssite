# Task 005: copy.py の Python前提への改修

## 概要

新年度ディレクトリ生成スクリプト `copy.py` を、Python ベースのビルドスクリプトを前提とした構成に更新する。

## ブランチ / Worktree

```
git worktree add gitworktree/feature-005-copypy-update gh-pages -b feature-005-copypy-update
```

## 背景

- `copy.py` は `python copy.py 2025 2026` のように使い、テンプレートから新年度ディレクトリを作成する
- 現状の問題点:
  - `run_build_test()` (L81-94) が `make.bash` を実行している
  - コピー元に bash スクリプトが含まれる場合、それもコピーされる
- 2026 をテンプレートとして使えば scripts/ に `.py` ファイルがコピーされるが、
  ビルドテストのコマンドが `bash make.bash` のままで失敗する

## 作業内容

### Step 1: ビルドテスト関数の修正

**対象**: `copy.py` の `run_build_test()` (L81-94)

```python
# Before
make_script = script_dir / target / "scripts" / "make.bash"
result = subprocess.run(["bash", str(make_script)], ...)

# After
make_script = script_dir / target / "scripts" / "make.py"
result = subprocess.run([sys.executable, str(make_script)], ...)
```

### Step 2: 表示メッセージの更新

- L140: `make.bash` → `make.py` の表示修正

### Step 3: 動作確認

```bash
# テスト用ディレクトリで実行
python copy.py 2026 test_year
# 確認後削除
rm -rf test_year
```

- 確認項目:
  - `test_year/scripts/` に `make.py` と `pandoc.py` が存在すること
  - `test_year/scripts/` に bash スクリプトが存在しないこと
  - ビルドテストが `python3 make.py` で実行されること
  - ビルドテストが成功すること

## 対象ファイル

| 操作 | ファイル |
|---|---|
| 編集 | `copy.py` |

## 依存関係

- 前提: Task 001 (ppsd に Python スクリプトが存在すること)
- 備考: copy.py のテンプレート元に 2026 を使えば scripts/ の中身は自然と .py になる

## 完了条件

- [ ] `run_build_test()` が `make.py` を実行する
- [ ] 2026 をテンプレートに新規ディレクトリを作成し、ビルドテストが成功する
