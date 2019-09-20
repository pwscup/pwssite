# pwssite
Privacy Workshop Webサイト管理用です

# フォルダ構成
- 2019
  - PWS2019のサイト
  - 2018 以前は管理していません
- .circleci
  - circleciの設定

# ブランチ
- master
  - 本番の[IWSECサーバ](https://www.iwsec.org/pws/2019/)用
  - masterにcommitした内容は、circleci で自動的に本番にデプロイされるので注意です
- gh-pages
  - テスト用
  - 本番にデプロイする前に、gh-pagesにpushしましょう
  - [github-pages](https://pwscup.github.io/pws2019site)で確認しましょう
- その他
  - 自由

# ワークフロー
  - gh-pagesからbranchを切る
  - ローカルでcommitする
  - gh-pagesにマージして、pushする
  - [github-pages](https://pwscup.github.io/pws2019site)で確認する
  - masterにマージして、本番の[IWSECサーバ](https://www.iwsec.org/pws/2019/)を確認する

# 備考
  - サイズの大きなデータは、直接iwsecサーバにscpしたりしましょう

# 詳細は
- [PWS Slack](https://pwscup.slack.com)で質問してください
