# pwssite 概要

Privacy Workshop Webサイト管理用リポジトリです。
誰でも触れるように、**GitHub上でもページを作成・編集**できるようにしています（ローカルでの作業も可）。

- ↓の"利用方法"をよく読みましょう　難しくありません
- [PWS Slack](https://pwscup.slack.com)で質問してください

## ページの追加・更新方法（GitHub上）

| 手順 | 内容 |
|---|---|
| 1 | [まずはこのスライド](https://docs.google.com/presentation/d/1VPrXKw8AN9LVo-EXei2zOkcJoQwn1LSfwvPKT-2-5lA/edit)を読む（思いと全体構成） |
| 2 | gh-pagesブランチの `/202*/markdown/` 等にある `.md` ファイルをマークダウン形式で編集（新規ページは `.md` を新規作成） |
| 3 | commitして少し待つと、[テスト環境](https://pwscup.github.io/pwssite)に反映される。見た目を確認 |
| 4 | 表示に問題があれば再度編集してcommit |
| 5 | 問題なければ gh-pages → master にマージ。少し待つと[本番環境](https://www.iwsec.org/pws/)にデプロイされる |

- テスト環境での表示確認は必ず行ってください。ビルド完了前にmasterにマージすると本番に反映されません
- 詳細は [PWS Slack](https://pwscup.slack.com) で質問してください

## 新規フォルダの追加方法

新年度や新規プロジェクト立ち上げ時を想定した手順です。
GitHub上の操作のみで完結できます（ローカルでの作業も可）。

詳しくは [新規フォルダの作成方法](doc/how-to-create-new-folder.md) を参照してください。

## フォルダ・ファイル構成

| フォルダ | 管理 | 説明 |
|---|---|---|
| `2018以前` | 対象外 | PWS2018以前のサイト。gitで管理していませんでした |
| `2019` | 対象外 | PWS2019のサイト。htmlファイルを直接編集 |
| `2020以降` | **管理対象** | PWS202*のサイト。mdファイルをgithub上で編集して作成 |
| `ppsd` | **管理対象** | データ合成技術評価委員会のサイト。2020以降と同じ運用 |
| `scripts/` | **管理対象** | 共通ビルドスクリプト（build.py, make.py, copy.py） |
| `.github/workflows` | **管理対象** | GitHub Actionsの設定（管理者向け） |

## ブランチ

| ブランチ | 用途 |
|---|---|
| `master` | 本番の[IWSECサーバ](https://www.iwsec.org/pws/)用。**commitされた内容は自動的に本番にデプロイされるので注意** |
| `gh-pages` | テスト用。[github-pages](https://pwscup.github.io/pwssite)で確認できる |
| その他 | 自由に作成してください |

## 裏側で何が動いているか

- 気になる人は[このスライド](https://docs.google.com/presentation/d/1VPrXKw8AN9LVo-EXei2zOkcJoQwn1LSfwvPKT-2-5lA/edit)を見ましょう
- GitHub Actionsが頑張っています
- Markdown→HTML変換はPython (`markdown-it-py`) で行っています（GitHub Flavored Markdown互換）
- 依存管理には [uv](https://docs.astral.sh/uv/) を使用しています
- ビルド対象は `pyproject.toml` の `[tool.pwssite] targets` で定義されています
- ローカルでビルドする場合は `uv run python3 make.py` を実行してください

## Markdown作成Tips

- GitHub Flavored Markdown (GFM) に対応しています
  - GitHub上のプレビューと同じ見た目でビルドされます
  - 打ち消し線(`~~text~~`)、タスクリスト(`- [ ]`)、テーブル等が使えます
- 最初に登場した `# ...` の文字列が title タグに採用されます。見つからない場合は "PWS" となります
- 画像は `markdown/Images/` に配置して、mdファイル内では `./Images/hoge.png` の形で参照
- masterへのマージのタイミング
  - gh-pagesにcommitして少し待つと、Actionsによるmarkdown→html変換が走って反映されます
  - 焦ってすぐにmasterにmergeすると、htmlが生成されずにmasterに含まれてしまうので注意
  - 上部のActionsタブから自動ビルドの実行状況が見られます。すべて完了状態になっていることを確認したら、次の作業に移りましょう

## 備考

- スタイルシートとフッタは編集しない想定です
- ヘッダは title タグだけ、mdファイルの文字列の影響を受けます
- Masterへの直接commit禁止です
- サイズの大きなデータはgithubには置けません（google driveの公開URL等を利用）

## 詳細は

[PWS Slack](https://pwscup.slack.com)で質問してください
