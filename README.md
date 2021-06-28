# pwssite
- Privacy Workshop Webサイト管理用です。
- 誰でも触れるように、github上でページを作成・編集できるようにしています。
- ↓の運用方法をよく読みましょう　難しくありません

- 運用方法
  - gh-pagesブランチの2020/markdown にある.mdファイルを、マークダウン形式で編集しましょう。 [このスライド](https://docs.google.com/presentation/d/1VPrXKw8AN9LVo-EXei2zOkcJoQwn1LSfwvPKT-2-5lA/edit)を参考に、github上でやるといいと思います。
  - commitして少し待つと、[github-pages](https://pwscup.github.io/pwssite)に反映されます。ここで見た目を確認します。
  - 表示が問題なければ、内容をmaster branchにマージしましょう。自分で承認して構いません。少し待つと、[IWSECサーバ](https://www.iwsec.org/pws/)にデプロイされます。
  - 詳細が気になる場合は [このスライド](https://docs.google.com/presentation/d/1VPrXKw8AN9LVo-EXei2zOkcJoQwn1LSfwvPKT-2-5lA/edit)を見ましょう
  
# フォルダ構成
- 2018以前
  - PWS2018以前のサイト gitで管理していませんでした 
- 2019
  - PWS2019のサイト htmlファイルを直接編集しています
- 2020
  - PWS2020のサイト mdファイルをビルドして作っています
- 2021
  - PWS2021のサイト PWS2020と同様です
- .circleci
  - circleciの設定 (詳しくないなら触らない)

# ブランチ
- master
  - 本番の[IWSECサーバ](https://www.iwsec.org/pws/)用
  - masterにcommitされた内容は、circleci で自動的に本番にデプロイされるので注意です
- gh-pages
  - テスト用
  - 本番にデプロイする前に、gh-pagesにpushしましょう
  - [github-pages](https://pwscup.github.io/pwssite)で確認できます
- その他
  - 自由

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
  - Masterへの直接commit禁止
    - iwsecサーバで↑の設定をしています   
  - サイズの大きなデータは、githubには置けないので注意です
    - 2019 は 2019/data/ をgitignoreしています data以下はローカルから直接iwsecサーバにscpしています
  - はたのむけ: ビルド用GCPインスタンスを再起動したら
    - ケチって静的IPアドレスの確保をしていないので、再起動したらIPアドレスが変わる。circleciで設定変更が必要
    - circleci > pwscup の環境変数 TEST_HOST_NAMEに、GCPインスタンスのIPアドレスを指定する

# 詳細は
- [PWS Slack](https://pwscup.slack.com)で質問してください
