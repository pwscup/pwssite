# CMS Python移行タスク (2026 / ppsd)

## 現状と目標

### Before

```
make.bash (ルート)
  ├── bash 2025/scripts/make.bash      # bash
  ├── python3 2026/scripts/make.py     # Python (移行済み)
  └── bash ppsd/scripts/make.bash      # bash (壊れている)
```

### After

```
make.py (ルート) ← 新規作成
  ├── python3 2026/scripts/make.py     # Python (移行済み)
  └── python3 ppsd/scripts/make.py     # Python (新規作成)

make.bash (ルート) ← 2025専用に縮退
  └── bash 2025/scripts/make.bash      # bash (変更なし)
```

---

## タスク一覧

| ID | タスク | Worktree | 優先度 | 依存 | 状態 |
|---|---|---|---|---|---|
| [001](task/task-001-ppsd-python-migration.md) | ppsd の Python移行 | `feature-001-ppsd-python-migration` | 高 | なし | 未着手 |
| [002](task/task-002-root-makepy.md) | ルート make.py 作成 / make.bash 縮退 | `feature-002-root-makepy` | 高 | 001 | 未着手 |
| [003](task/task-003-cicd-update.md) | CI/CD ワークフロー更新 | `feature-003-cicd-update` | 高 | 002 | 未着手 |
| [004](task/task-004-tests.md) | テストスイート作成 | `feature-004-tests` | 中 | 001 | 未着手 |
| [005](task/task-005-copypy-update.md) | copy.py の改修 | `feature-005-copypy-update` | 中 | 001 | 未着手 |
| [006](task/task-006-future-improvements.md) | 将来の改善検討 | (個別) | 低 | 003 | 未着手 |

## 依存関係

```
001 ppsd Python移行
 ├─→ 002 ルート make.py 作成
 │    └─→ 003 CI/CD 更新
 │          └─→ 006 将来改善 (任意)
 ├─→ 004 テスト作成 (並行可能)
 └─→ 005 copy.py 改修
```

## Worktree 運用ルール

各タスクは git worktree を使って独立したディレクトリで作業する。

### 作成コマンド

```bash
# リポジトリルートで実行
git worktree add gitworktree/feature-NNN-keyword gh-pages -b feature-NNN-keyword
```

### 命名規則

```
gitworktree/feature-{タスクID}-{キーワード}
```

- 例: `gitworktree/feature-001-ppsd-python-migration`
- 例: `gitworktree/feature-002-root-makepy`

### Worktree 一覧確認

```bash
git worktree list
```

### 作業完了後

```bash
# マージ後に worktree を削除
git worktree remove gitworktree/feature-NNN-keyword
# ブランチも不要なら削除
git branch -d feature-NNN-keyword
```

### 注意事項

- `gitworktree/` は `.gitignore` に追加済みであること（コミットしない）
- 各 worktree で作業後は gh-pages ブランチへマージする

## 技術的前提

- Python 3.7+ (`pathlib`, `subprocess`, type hints)
- `requirements.txt`: `Markdown>=3.5`
- 2025 以前のディレクトリは変更しない
