# Task 001: ppsd の Python移行

## 概要

ppsd ディレクトリのビルドスクリプトを bash から Python に移行する。
2026 ディレクトリで実績のある `make.py` / `pandoc.py` をベースにする。

## ブランチ / Worktree

```
git worktree add gitworktree/feature-001-ppsd-python-migration gh-pages -b feature-001-ppsd-python-migration
```

## 背景

- ppsd/scripts/make.bash のインクリメンタルビルドが壊れている
  - コメント:「なぜかファイル更新が検知されないので、一旦全ファイルを更新するようにする」
  - `if true; then` で常に全ファイルをリビルドしている
- 2026 では Python 移行済みで安定稼働している
- ppsd と 2026 のテンプレート構造（header/footer）は同一

## 作業内容

### Step 1: ppsd/scripts/pandoc.py 作成

- `2026/scripts/pandoc.py` をコピーして `ppsd/scripts/pandoc.py` として配置
- 変更不要の見込み（テンプレート相対パスが同じため）
- **判断事項**: TOC 生成機能について
  - 2026 版は `What's new` セクション後に目次を自動挿入する
  - ppsd は現在単一ページ (`index.md` のみ) で、セクション数も少ない
  - → TOC 機能はそのまま残す（セクション少数なら TOC は生成されない設計になっている）

### Step 2: ppsd/scripts/make.py 作成

- `2026/scripts/make.py` をコピーして `ppsd/scripts/make.py` として配置
- 変更不要の見込み（パスは全て `__file__` 起点の相対パス）

### Step 3: 動作確認

```bash
cd ppsd
python3 scripts/make.py
```

- 確認項目:
  - `ppsd/html/index.html` が生成されること
  - `ppsd/index.html` にコピーされること
  - 生成 HTML に `<!-- contents start -->` / `<!-- contents end -->` が含まれること
  - タイトルが正しく抽出されること
  - 2回目の実行で "No markdown newer than existing HTML." と表示されること（インクリメンタルビルド）

### Step 4: bash スクリプト削除

- `ppsd/scripts/make.bash` を削除
- `ppsd/scripts/pandoc.bash` を削除

## 対象ファイル

| 操作 | ファイル |
|---|---|
| 新規作成 | `ppsd/scripts/pandoc.py` |
| 新規作成 | `ppsd/scripts/make.py` |
| 削除 | `ppsd/scripts/make.bash` |
| 削除 | `ppsd/scripts/pandoc.bash` |

## 依存関係

- 前提: なし（最初に着手可能）
- 後続: Task 002, Task 003, Task 005

## 完了条件

- [ ] `python3 ppsd/scripts/make.py` で ppsd/index.html が正しく生成される
- [ ] インクリメンタルビルドが正常に動作する
- [ ] bash スクリプト (`make.bash`, `pandoc.bash`) が削除されている
- [ ] 生成される HTML の内容が bash 版と同等である
