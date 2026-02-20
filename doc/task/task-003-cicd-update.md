# Task 003: CI/CD ワークフロー更新

## 概要

GitHub Actions ワークフローを更新し、Python ビルドパイプラインに対応させる。
現状 `pip install` が欠落しており、Python `markdown` ライブラリが CI 上で利用できていない。

## ブランチ / Worktree

```
git worktree add gitworktree/feature-003-cicd-update gh-pages -b feature-003-cicd-update
```

## 背景

- `.github/workflows/convert_markdown.yml` の build-pages ジョブが対象
- 現状:
  - `sudo apt-get install -y tidy pandoc` で外部ツールのみインストール
  - `bash make.bash` でビルド実行
  - `pip install -r requirements.txt` が**存在しない**
- `requirements.txt` に `Markdown>=3.5` があるが CI でインストールされていない
- 2026 のビルド (`make.py` → `pandoc.py`) は Python `markdown` ライブラリを使用するため、
  現状の CI では 2026 のビルドが失敗する可能性がある

## 作業内容

### Step 1: ワークフロー更新

**対象**: `.github/workflows/convert_markdown.yml`

変更箇所 (build-pages ジョブ):

1. **Python 依存のインストール追加**:
   ```yaml
   - name: Install Python dependencies
     run: pip install -r requirements.txt
   ```

2. **ビルドコマンドの変更**:
   ```yaml
   - name: Build HTML
     run: |
       bash make.bash
       python3 make.py
   ```
   - `bash make.bash` → 2025 のビルド
   - `python3 make.py` → 2026 + ppsd のビルド

3. **pandoc / tidy の扱い**:
   - `pandoc`: 2025 が依存しているため引き続きインストール
   - `tidy`: Python 版の make.py でも使用しているため維持

### Step 2: requirements.txt の確認

- 現状 `Markdown>=3.5` のみ
- テスト用ライブラリ (pytest 等) は `requirements-dev.txt` として分離するか検討
  - CI のビルドジョブには不要
  - テスト実行を CI に追加する場合は別途対応

### Step 3: 動作確認

- ワークフローの YAML 構文チェック
- 可能であればローカルで同等の手順を実行:
  ```bash
  pip install -r requirements.txt
  bash make.bash
  python3 make.py
  ```

## 対象ファイル

| 操作 | ファイル |
|---|---|
| 編集 | `.github/workflows/convert_markdown.yml` |
| 確認 | `requirements.txt` |

## 依存関係

- 前提: Task 002 (ルート make.py が存在すること)
- 後続: なし（ただし Task 004 でテスト CI を追加する場合は関連）

## 完了条件

- [ ] `pip install -r requirements.txt` ステップが追加されている
- [ ] ビルドコマンドが `bash make.bash && python3 make.py` になっている
- [ ] gh-pages ブランチへの push で CI が正常に完了する
