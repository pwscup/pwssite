# pwssite 概要
- Privacy Workshop Webサイト管理用リポジトリです。
- 誰でも触れるように、**github上でページを作成・編集**できるようにしています。
- ↓の運用方法をよく読みましょう　難しくありません
  - [PWS Slack](https://pwscup.slack.com)で質問してください。

- 運用方法
  - [まずはこのスライド](https://docs.google.com/presentation/d/1VPrXKw8AN9LVo-EXei2zOkcJoQwn1LSfwvPKT-2-5lA/edit)を読みましょう。
  - gh-pagesブランチの/202*/markdown にある.mdファイルを、マークダウン形式で編集してください。
    - 新規ページ作成時は、/202*/markdown/hoge.mdを新規作成してください。
  - commitして少し待つと、[テスト環境：github-pages](https://pwscup.github.io/pwssite)に反映されます。ここで見た目を確認します。
    - 表示に問題があれば、またgithub上でmarkdownを編集してください。
  - 表示が問題なければ、gh-pagesブランチの内容をmaster branchにマージしましょう。
    - 自分で承認して構いません。少し待つと、[本番環境：IWSECサーバ](https://www.iwsec.org/pws/)にデプロイされます。
  - 詳細が気になる場合は [このスライド](https://docs.google.com/presentation/d/1VPrXKw8AN9LVo-EXei2zOkcJoQwn1LSfwvPKT-2-5lA/edit)をよく見つつ、 Slackで質問してください
  
# フォルダ構成
- 2018以前
  - PWS2018以前のサイト gitで管理していませんでした 
- 2019
  - PWS2019 のサイト htmlファイルを直接編集しています
- 2020以降
  - PWS202* のサイト "運用方法"の手順で、mdファイルをgithub上で編集して作っています
- .circleci
  - circleciの設定 (通常、これを触りたい場面はないと思います CirfleCIの設定ファイルです)

# ブランチ
- master
  - 本番の[IWSECサーバ](https://www.iwsec.org/pws/)用
  - **masterにcommitされた内容は、circleci で自動的に本番にデプロイされるので注意です**
- gh-pages
  - テスト用
  - [github-pages](https://pwscup.github.io/pwssite)で確認できます
- その他
  - 自由に作成してください。

# 裏側で何が動いているか
  - 気になる人は[このスライド](https://docs.google.com/presentation/d/1VPrXKw8AN9LVo-EXei2zOkcJoQwn1LSfwvPKT-2-5lA/edit)を見ましょう
  - [CircleCI](https://app.circleci.com/pipelines/github/pwscup/pwssite) + GCPのEC2インスタンスが頑張っています

# markdown作成Tips
- インデントはタブ2つで
  - pandocの設定不足なせいで、タブ１つだと深さが変わりません　いつか調べて直します
- 画像の場所に注意
  - markdown/Imagesに配置して、mdファイル内では./Images/hoge.pngという形で参照すれば大丈夫かと
- masterへのマージのタイミング
  - gh-pagesにcommitして少し待つと、CircleCIによるmarkdown->html変換が走って反映されます
  - 焦ってすぐにmasterにmergeすると、htmlが生成されずにmasterに含まれてしまうので、注意です　gh-pagesで確認してからmasterにマージしましょう

# 備考
  - スタイルシートとヘッダ・フッタは編集しない想定です。
    - 見た目で困ることはない気がするので...
  - Masterへの直接commit禁止です。
    - iwsecサーバで↑の設定をしています。 Githubでは面倒なので設定していません。  
  - サイズの大きなデータは、githubには置けません。
    - 2019 は 2019/data/ をgitignoreしています data以下はローカルから直接iwsecサーバにscpしています
    - google driveの公開ディレクトリのURLを記載する、など
  - はたの向け: ビルド用GCPインスタンスを再起動したら
    - ケチって静的IPアドレスの確保をしていないので、再起動したらIPアドレスが変わる。circleciで設定変更が必要
    - circleci > pwscup の環境変数 TEST_HOST_NAMEに、GCPインスタンスのIPアドレスを指定する
    - /tmp/pwssiteが消えているかも git clone git:// .... する 

# 詳細は
- [PWS Slack](https://pwscup.slack.com)で質問してください
