# .DS_Storeファイルクリーンアップ手順

## 現在の状況
- ルートディレクトリに`.DS_Store`ファイルが存在
- `2025/.DS_Store`ファイルが存在
- `.gitignore`を更新済み（macOSシステムファイルを包括的に除外）

## 実行すべき手順

### ターミナルで以下のコマンドを実行してください：

```bash
cd /Users/thatano/works/pwssite

# 1. 既存の.DS_Storeファイルを削除
find . -name ".DS_Store" -type f -delete

# 2. Gitキャッシュからも削除（既にトラッキングされている場合）
git rm --cached .DS_Store 2>/dev/null || true
git rm --cached 2025/.DS_Store 2>/dev/null || true

# 3. 変更をステージング
git add .gitignore

# 4. 不要なクリーンアップスクリプトを削除
rm cleanup_ds_store.bash

# 5. 変更をコミット
git commit -m "Remove .DS_Store files and improve gitignore for macOS system files"

# 6. 確認
git status
```

## 説明

- `.gitignore`に以下を追加しました：
  - `.DS_Store?` - バリエーション対応
  - `._*` - リソースフォーク
  - `.Spotlight-V100` - Spotlight検索インデックス
  - `.Trashes` - ゴミ箱
  - `ehthumbs.db`, `Thumbs.db` - Windows用サムネイルファイル

これにより、今後macOSやWindowsのシステムファイルがGitに含まれることを防げます。
