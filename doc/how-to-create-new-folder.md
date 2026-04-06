# 新規フォルダの作成方法

新年度や新規プロジェクトのフォルダを作成する手順です。
GitHub上での操作のみで完結する方法と、ローカル環境で行う方法があります。

## 方法1: GitHub上で作成する（推奨）

### 手順

1. リポジトリの **Actions** タブを開く
2. 左メニューから **Create New Folder** を選択
3. **Run workflow** をクリック
4. 以下を入力して実行:
   - **参照元フォルダ名**: コピー元のフォルダ（例: `2026`）
   - **新規フォルダ名**: 作成するフォルダ（例: `2027`）
5. ワークフローが完了すると、gh-pages に対するPRが自動作成される

### 自動で行われること

- 参照元からディレクトリ構造をコピー（`scripts/` は除外）
- 共通ファイルのコピー（`style.css`, `template/*`, `markdown/index.md`）
- `index.md` の初期化（見出し構造のみ残してTBDに）
- `html/` にプレースホルダを作成
- `pyproject.toml` の `[tool.pwssite] targets` に新規フォルダ名を追加
- ビルドテストの実行

### PR作成後に手動で行うこと

PRが作成されたら、GitHub上でファイルを編集して追加コミットしてください。

1. **`index.html` にリンクを追加**: トップページのリンク一覧に新規フォルダへのリンクを追加
2. **`<新規名>/markdown/index.md` を編集**: コンテンツの内容を記入

## 方法2: ローカル環境で作成する

### 前提

- Python 3.9以上
- [uv](https://docs.astral.sh/uv/) がインストール済み

### 手順

1. フォルダを作成
   ```bash
   uv run python3 scripts/copy.py <参照元> <新規名>
   ```
   例: `uv run python3 scripts/copy.py 2026 2027`

2. `<新規名>/markdown/index.md` を編集

3. `index.html` に新規フォルダへのリンクを追加

4. 変更をコミットしてPRを作成
