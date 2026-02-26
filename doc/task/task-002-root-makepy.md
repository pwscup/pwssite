# Task 002: ルート make.py 作成 / make.bash 縮退

## 概要

ルートに `make.py` を新規作成し、2026 と ppsd のビルドを Python から実行する。
既存の `make.bash` は 2025 専用に縮退させる。

## ブランチ / Worktree

```
git worktree add gitworktree/feature-002-root-makepy gh-pages -b feature-002-root-makepy
```

## 背景

- 現在の `make.bash` は 2025 (bash), 2026 (python), ppsd (bash) を順次呼び出している
- Task 001 完了後、ppsd も Python 化されるため、Python 系は `make.py` に集約する
- 2025 は bash のまま維持するため、`make.bash` も残す

## 作業内容

### Step 1: /make.py 新規作成

```python
#!/usr/bin/env python3
"""2026 / ppsd のビルドエントリポイント"""
```

- `2026/scripts/make.py` と `ppsd/scripts/make.py` を順次 subprocess で呼び出す
- いずれかが失敗した場合は非ゼロの終了コードを返す
- 現在の `make.bash` の構造を参考にする（シンプルに呼び出すだけ）

### Step 2: /make.bash の縮退

- 2026 と ppsd の呼び出し行を削除
- 2025 の呼び出しのみ残す
- ファイル先頭にコメントを追加:

```bash
# [LEGACY] 2025以前の bash ベースのビルド用
# 2026 以降は make.py を使用してください
```

### Step 3: 動作確認

```bash
# Python 系ビルド
python3 make.py

# bash 系ビルド (2025のみ)
bash make.bash
```

## 対象ファイル

| 操作 | ファイル |
|---|---|
| 新規作成 | `make.py` |
| 編集 | `make.bash` |

## 依存関係

- 前提: Task 001 (ppsd の Python移行が完了していること)
- 後続: Task 003 (CI/CD でこの make.py を呼ぶ)

## 完了条件

- [ ] `python3 make.py` で 2026 と ppsd の HTML が正しく生成される
- [ ] `bash make.bash` で 2025 の HTML が正しく生成される
- [ ] `make.bash` に 2026 / ppsd の呼び出しが残っていないこと
