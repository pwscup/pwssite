# pwssite 概要
- Privacy Workshop Webサイト管理用リポジトリです。
- 誰でも触れるように、**GitHub上でもページを作成・編集**できるようにしています。
  - ローカルで作業していただいても構いません
- ↓の"利用方法"をよく読みましょう　難しくありません
  - [PWS Slack](https://pwscup.slack.com)で質問してください。
  
- 利用方法(@GitHub)
  - [まずはこのスライド](https://docs.google.com/presentation/d/1VPrXKw8AN9LVo-EXei2zOkcJoQwn1LSfwvPKT-2-5lA/edit)を読みましょう。
    - 思いと全体構成が書いてあります
  - 既存ページを更新する際は、gh-pagesブランチの/202*/markdown 等にある.mdファイルを、マークダウン形式で編集してください。
    - 新規ページを作成する際は、/202*/markdown/hoge.md等を新規作成してください。
  - commitして少し待つと、[テスト環境：github-pages](https://pwscup.github.io/pwssite)の/202*/hoge.mdに反映されます。ここで見た目を確認します。
    - 表示に問題があれば、再度GitHub上でmarkdownを編集してcommitしてください。
  - 表示が問題なければ、本番環境に反映してください。gh-pagesブランチの内容をmaster branchにマージするだけです。
    - 自分で承認して構いません。少し待つと、[本番環境：IWSECサーバ](https://www.iwsec.org/pws/)にデプロイされます。
    - テスト環境での表示確認は必ず行ってください。早まってビルド完了前にmasterにマージした場合は、本番環境に変更が反映されません。
  - 詳細が気になる場合は [PWS Slack](https://pwscup.slack.com)で質問してください。誰かが答えてくれます。
    - 招待済みでない場合は、他の適当な手段で運営委員のどなたかにコンタクトをとってください。担当者にスローされます。

- 利用方法(@ローカル)
  - いい感じにお願いします

# フォルダ・ファイル構成
- (管理対象外)2018以前
  - PWS2018以前のサイト gitで管理していませんでした 
- (管理対象外)2019
  - PWS2019 のサイト htmlファイルを直接編集しています
- (管理対象)2020以降
  - PWS202* のサイト "運用方法"の手順で、mdファイルをgithub上で編集して作っています
- (管理対象) .github/workflows
  - GitHub Actionsの設定 (通常、これを触りたい場面はないと思います 管理者向けです)
# ブランチ
- master
  - 本番の[IWSECサーバ](https://www.iwsec.org/pws/)用
  - **masterにcommitされた内容は、Actionsで自動的に本番にデプロイされるので注意です**
- gh-pages
  - テスト用
  - [github-pages](https://pwscup.github.io/pwssite)で確認できます
- その他
  - 自由に作成してください。

# 裏側で何が動いているか
  - 気になる人は[このスライド](https://docs.google.com/presentation/d/1VPrXKw8AN9LVo-EXei2zOkcJoQwn1LSfwvPKT-2-5lA/edit)を見ましょう
  - GitHub Actionsが頑張っています


# markdown作成Tips
- インデントはタブ2つで
  - pandocの設定不足なせいで、タブ１つだと深さが変わりません　いつか調べて直します
- 最初に登場した "# ..." の文字列が title タグに採用されます。見つからない場合は "PWS" となります。
- 画像の場所に注意
  - markdown/Imagesに配置して、mdファイル内では./Images/hoge.pngという形で参照すれば大丈夫かと
- masterへのマージのタイミング
  - gh-pagesにcommitして少し待つと、Actionsによるmarkdown->html変換が走って反映されます
  - 焦ってすぐにmasterにmergeすると、htmlが生成されずにmasterに含まれてしまうので、注意です　gh-pagesで確認してからmasterにマージしましょう
  - 上部のActionsタブから、自動ビルド実行様子が見られます。すべて完了状態になっていることを確認したら、次の作業に移りましょう

# 備考
  - スタイルシートとフッタは編集しない想定です。
    - 見た目で困ることはない気がするので...
  - ヘッダは title タグだけ、 mdファイルの文字列の影響を受けます。
  - Masterへの直接commit禁止です。
    - iwsecサーバで↑の設定をしています。 Githubでは、...どうやるんだ？誰か教えてください
  - サイズの大きなデータは、githubには置けません。
    - 2019 は 2019/data/ をgitignoreしています data以下はローカルから直接iwsecサーバにscpしています
    - google driveの公開ディレクトリのURLを記載する、など

# 詳細は
- [PWS Slack](https://pwscup.slack.com)で質問してください
