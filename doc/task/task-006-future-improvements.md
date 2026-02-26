# Task 006: 将来の改善検討 (低優先度)

## 概要

Python 移行完了後に検討する改善案をまとめる。
すぐに着手する必要はなく、必要に応じて個別タスクに分離する。

## ブランチ / Worktree

必要に応じて個別に作成:
```
git worktree add gitworktree/feature-006a-remove-tidy gh-pages -b feature-006a-remove-tidy
git worktree add gitworktree/feature-006b-template-engine gh-pages -b feature-006b-template-engine
```

---

## 006a: tidy 外部コマンド依存の排除

### 現状
- `make.py` が HTML 整形に外部コマンド `tidy` を使用
- CI でも `apt-get install -y tidy` でインストールしている
- tidy は警告を出すことがあり、ログが見づらい

### 検討案
- Python ライブラリ `beautifulsoup4` の `prettify()` で置換
- または `html5-parser` / `lxml` の利用

### リスク
- 出力 HTML のインデントやフォーマットが変わる
- 既存の HTML との差分が大量に発生する可能性
- git 上の差分が見づらくなる

### 判断基準
- tidy が問題を起こしていなければ無理に変更しない

---

## 006b: テンプレートエンジン導入

### 現状
- `pandoc.py` で header/footer を文字列結合で組み立てている
- 日英切り替えは `_e` サフィックスで分岐

### 検討案
- Jinja2 テンプレートエンジンの導入
- 1つのテンプレートファイルで条件分岐（日英、TOC有無）

### リスク
- 現状のテンプレート（5ファイル）を全て書き換える必要がある
- 規模が小さいため、テンプレートエンジンが過剰な可能性
- 学習コストが増える

### 判断基準
- テンプレートの種類が増えた場合（新しい言語、新しいレイアウト）に再検討

---

## 006c: ppsd / 2026 のスクリプト共通化

### 現状
- `ppsd/scripts/make.py` と `2026/scripts/make.py` は同一コード
- `ppsd/scripts/pandoc.py` と `2026/scripts/pandoc.py` も同一コード

### 検討案
- 共通ライブラリとして `lib/` に切り出し、各ディレクトリから import
- または、ルートの `make.py` にビルドロジックを集約し、対象ディレクトリをパラメータ化

### リスク
- import パスの管理が複雑になる
- 各ディレクトリの独立性が下がる（一方を変更すると他方に影響）

### 判断基準
- 同一コードの維持が負担になった場合に検討
- 現状2箇所だけなので急ぐ必要はない
