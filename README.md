# pwssite — Privacy Workshop Webサイト管理ガイド

Privacy Workshop (PWS) の公式Webサイトを管理するリポジトリです。
GitHub上でMarkdownファイルを編集するだけでページの作成・更新ができます（ローカルでの作業も可）。
不明点は [PWS Slack](https://pwscup.slack.com) で質問してください。

- テスト環境: https://pwscup.github.io/pwssite
- 本番環境: https://www.iwsec.org/pws/

## 目次

| # | セクション | 内容 |
|---|---|---|
| 01 | [ページの追加・更新方法](#01-ページの追加更新方法github上) | GitHub上でのページ編集手順 |
| 02 | [新規フォルダの追加方法](#02-新規フォルダの追加方法ローカル) | 新年度・新規プロジェクト立ち上げ時の手順 |
| 03 | [フォルダ・ファイル構成](#03-フォルダファイル構成) | リポジトリの主要ディレクトリ一覧 |
| 04 | [ブランチ](#04-ブランチ) | ブランチの種類と運用ルール |
| 05 | [技術スタック・アーキテクチャ](#05-技術スタックアーキテクチャ) | ビルド・デプロイを支える技術要素 |
| 06 | [Markdown作成Tips](#06-markdown作成tips) | Markdown記述時に知っておくと便利なポイント |
| 07 | [備考](#07-備考) | その他の注意事項 |
| 08 | [困ったときは](#08-困ったときは) | 問い合わせ先・参考リンク |

---

## 01. ページの追加・更新方法（GitHub上）

GitHub上でMarkdownファイルを編集・commitするだけでページを更新できます。
まずは[全体構成スライド](https://docs.google.com/presentation/d/1VPrXKw8AN9LVo-EXei2zOkcJoQwn1LSfwvPKT-2-5lA/edit)を読んで、サイトの思想と構成を把握してください。

| 手順 | 概要 | 内容 |
|---|---|---|
| 1 | 全体像の把握 | [全体構成スライド](https://docs.google.com/presentation/d/1VPrXKw8AN9LVo-EXei2zOkcJoQwn1LSfwvPKT-2-5lA/edit)を読む（思いと全体構成） |
| 2 | Markdownの編集 | gh-pagesブランチの `/202*/markdown/` 等にある `.md` ファイルをマークダウン形式で編集（新規ページは `.md` を新規作成） |
| 3 | ビルド完了を待つ | commitすると [GitHub Actions](https://github.com/pwscup/pwssite/actions) が自動でHTML変換を実行する。Actionsタブで全ジョブが完了（緑チェック）になるまで待つ |
| 4 | テスト環境で確認 | [テスト環境](https://pwscup.github.io/pwssite)で見た目を確認。問題があれば再度編集してcommit |
| 5 | 本番へデプロイ | 問題なければ gh-pages → master にマージ。少し待つと[本番環境](https://www.iwsec.org/pws/)にデプロイされる |

**注意事項**

| 項目 | 内容 |
|---|---|
| テスト環境の確認 | 必ず[テスト環境](https://pwscup.github.io/pwssite)で表示を確認してからmasterにマージしてください |
| ビルド完了前のマージ禁止 | [Actionsタブ](https://github.com/pwscup/pwssite/actions)で全ジョブが完了する前にmasterにマージすると、HTMLが生成されないまま本番に反映されます |
| ビルド状況の確認方法 | リポジトリ上部の [Actions](https://github.com/pwscup/pwssite/actions) タブから実行状況を確認できます |

---

## 02. 新規フォルダの追加方法

新年度や新規プロジェクト立ち上げ時を想定した手順です。
GitHub上の操作のみで完結できます（ローカルでの作業も可）。

詳しくは [新規フォルダの作成方法](doc/how-to-create-new-folder.md) を参照してください。

---

## 03. フォルダ・ファイル構成

リポジトリの主要なディレクトリとその役割です。
コンテンツの編集対象は `2020` 以降の年度フォルダと [`ppsd/`](ppsd/) です。

| フォルダ | 管理 | 説明 |
|---|---|---|
| `2018以前` | 対象外 | PWS2018以前のサイト。gitで管理していませんでした |
| [`2019/`](2019/) | 対象外 | PWS2019のサイト。htmlファイルを直接編集 |
| `2020/` 以降 | **管理対象** | PWS各年度のサイト。mdファイルをGitHub上で編集して作成 |
| [`ppsd/`](ppsd/) | **管理対象** | データ合成技術評価委員会のサイト。2020以降と同じ運用 |
| [`scripts/`](scripts/) | **管理対象** | 共通ビルドスクリプト（[build.py](scripts/build.py), [make.py](scripts/make.py), [create_folder.py](scripts/create_folder.py)） |
| [`tests/`](tests/) | **管理対象** | テストコード（pytest） |
| [`doc/`](doc/) | **管理対象** | ドキュメント・タスク管理 |
| [`.github/workflows/`](.github/workflows/) | **管理対象** | GitHub Actionsの設定（管理者向け） |

---

## 04. ブランチ

3種類のブランチを使い分けています。
通常の開発は `gh-pages` ブランチ、または `gh-pages` から切り出した `feature-*` ブランチで行います。

| ブランチ | 用途 | 運用ルール |
|---|---|---|
| `master` | [本番環境](https://www.iwsec.org/pws/)へのデプロイ用 | **直接commitしない**。gh-pagesの内容をマージして本番に反映する |
| `gh-pages` | [テスト環境](https://pwscup.github.io/pwssite)での確認・開発用 | メインの開発ブランチ。PRのベースはこちら |
| `feature-*` 等 | 機能開発・修正用 | gh-pagesから切り出して作成し、gh-pagesへPRを出す |

---

## 05. 技術スタック・アーキテクチャ

サイトのビルド・デプロイを支える技術要素です。
全体像は[全体構成スライド](https://docs.google.com/presentation/d/1VPrXKw8AN9LVo-EXei2zOkcJoQwn1LSfwvPKT-2-5lA/edit)を参照してください。

| 技術 | 用途 | 備考 |
|---|---|---|
| [Python 3.9+](https://www.python.org/) | ビルドスクリプト | [`make.py`](make.py) がエントリーポイント。ローカルビルドは `uv run python3 make.py` |
| [markdown-it-py](https://markdown-it-py.readthedocs.io/) | Markdown→HTML変換 | GitHub Flavored Markdown (GFM) 互換 |
| [uv](https://docs.astral.sh/uv/) | 依存管理・実行環境 | `uv run` でスクリプトを実行 |
| [GitHub Actions](https://github.com/pwscup/pwssite/actions) | CI/CD | [`convert_markdown.yml`](.github/workflows/convert_markdown.yml) でビルド・デプロイを自動化 |
| [pytest](https://docs.pytest.org/) | テスト | `uv run pytest` で実行 |
| [ruff](https://docs.astral.sh/ruff/) | リンター/フォーマッター | `uv run ruff check .` / `uv run ruff format .` |
| [`pyproject.toml`](pyproject.toml) | ビルド対象定義 | `[tool.pwssite] targets` でビルド対象フォルダを指定 |

---

## 06. Markdown作成Tips

Markdownを書く際に知っておくと便利なポイントです。
HTML変換には [markdown-it-py](https://markdown-it-py.readthedocs.io/) を使用しており、GitHub Flavored Markdown (GFM) 互換です。

| Tips | 説明 |
|---|---|
| GFM対応 | GitHub上のプレビューと同じ見た目でビルドされます。打ち消し線(`~~text~~`)、タスクリスト(`- [ ]`)、テーブル等が使えます |
| titleタグ | 最初に登場した `# ...` の文字列がHTMLの `<title>` タグに採用されます。見つからない場合は "PWS" になります |
| 画像の配置 | `markdown/Images/` に配置し、mdファイル内では `./Images/hoge.png` の形で参照 |
| マージのタイミング | [Actionsタブ](https://github.com/pwscup/pwssite/actions)で全ジョブの完了（緑チェック）を確認してからmasterにマージしてください |

---

## 07. 備考

上記セクションに該当しない注意事項です。

| 項目 | 内容 |
|---|---|
| スタイルシート・フッタ | 編集しない想定です（`style.css` や template 内のフッタ） |
| 大きなデータ | GitHubにはサイズの大きなデータを置けません。Google Driveの公開URL等を利用してください |

---

## 08. 困ったときは

不明点や問題があれば以下を参照してください。

| リソース | 説明 |
|---|---|
| [PWS Slack](https://pwscup.slack.com) | 質問・相談はこちら |
| [全体構成スライド](https://docs.google.com/presentation/d/1VPrXKw8AN9LVo-EXei2zOkcJoQwn1LSfwvPKT-2-5lA/edit) | サイトの思想と全体構成 |
| [GitHub Actionsタブ](https://github.com/pwscup/pwssite/actions) | ビルド・デプロイの実行状況 |
| [テスト環境](https://pwscup.github.io/pwssite) | gh-pagesブランチの表示確認 |
| [本番環境](https://www.iwsec.org/pws/) | masterブランチのデプロイ先 |
