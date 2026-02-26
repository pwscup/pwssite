# Task 004: テストスイート作成

## 概要

`pandoc.py` と `make.py` のユニットテスト、およびビルド全体の結合テストを作成する。

## ブランチ / Worktree

```
git worktree add gitworktree/feature-004-tests gh-pages -b feature-004-tests
```

## 背景

- 現在テストが一切存在しない
- Python 移行で関数が分離されたため、ユニットテストが書きやすい状態
- 今後のリファクタリング（共通化等）に備えて回帰テストを整備する

## 作業内容

### Step 1: テスト基盤セットアップ

- `requirements-dev.txt` を作成（`pytest` を追加）
- テストディレクトリ `tests/` を作成
- `tests/conftest.py` に共通フィクスチャを定義（テンプレートディレクトリの提供等）

### Step 2: pandoc.py のユニットテスト

**対象**: `tests/test_pandoc.py`

| テスト関数 | テスト観点 |
|---|---|
| `extract_title()` | H1 行からタイトル抽出 |
| `extract_title()` | H1 がない場合のデフォルト値 "PWS" |
| `build_body()` | 基本的な Markdown → HTML 変換 |
| `build_body()` | テーブルの変換 |
| `build_body()` | 脚注の変換 |
| `build_body()` | fenced code block の変換 |
| `insert_toc_after_whats_new()` | "What's new" セクション後への TOC 挿入 |
| `insert_toc_after_whats_new()` | "What's new" がない場合のフォールバック |
| `insert_toc_after_whats_new()` | TOC が空の場合（セクションが少ない） |
| `build_header()` | 日本語テンプレートの選択 |
| `build_header()` | `_e` サフィックスで英語テンプレートの選択 |

### Step 3: make.py のユニットテスト

**対象**: `tests/test_make.py`

| テスト関数 | テスト観点 |
|---|---|
| `collect_markdown()` | .md ファイルの収集 |
| `collect_markdown()` | サブディレクトリ内の .md ファイル |
| `collect_markdown()` | 空ディレクトリ |
| ビルド判定 | HTML が存在しない場合 → ビルド対象 |
| ビルド判定 | md が HTML より新しい場合 → ビルド対象 |
| ビルド判定 | md が HTML より古い場合 → スキップ |

### Step 4: 結合テスト

**対象**: `tests/test_build.py`

| テスト | テスト観点 |
|---|---|
| ppsd ビルド | `python3 ppsd/scripts/make.py` の実行と HTML 生成 |
| 2026 ビルド | `python3 2026/scripts/make.py` の実行と HTML 生成 |
| ルート make.py | `python3 make.py` で両ディレクトリがビルドされる |
| HTML 構造検証 | `<!-- contents start -->`, `<!-- contents end -->` の存在 |
| HTML 構造検証 | `<title>` タグの存在 |
| HTML 構造検証 | footer の存在 |

### Step 5 (任意): CI にテスト実行を追加

- `.github/workflows/convert_markdown.yml` にテストステップ追加
- または別ワークフローとして分離

## 対象ファイル

| 操作 | ファイル |
|---|---|
| 新規作成 | `requirements-dev.txt` |
| 新規作成 | `tests/conftest.py` |
| 新規作成 | `tests/test_pandoc.py` |
| 新規作成 | `tests/test_make.py` |
| 新規作成 | `tests/test_build.py` |

## 依存関係

- 前提: Task 001 (ppsd の Python スクリプトが存在すること)
- 前提: Task 002 (ルート make.py が存在すること) ※結合テストのみ
- Phase 1〜2 と並行して着手可能（ユニットテストは 2026 のコードだけで書ける）

## 完了条件

- [ ] `pytest tests/` が全て PASS する
- [ ] pandoc.py の主要関数にテストがある
- [ ] make.py の collect_markdown / ビルド判定にテストがある
- [ ] 結合テストで実際の HTML 生成が検証されている
