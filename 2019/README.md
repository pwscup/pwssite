pws2019, pwscup2019ウェブサイト用
==

## 構成
- index.html
    - PWS用ページ
- cup19.html
    - PWSCUP用ページ
- data
    - 配布データ(軽いもの)
- .circleci
    - 自動デプロイ用設定 (基本的には触らない)
## 注意
- developにpushすると、[テストサーバ](http://35.230.41.225/pws2019site/)に自動デプロイされます
    - これで確認するといいと思います
- masterにpushすると、[iwsecサーバ](https://www.iwsec.org/pws/)に自動デプロイされます
    - テストサーバで確認してからmasterにpushしましょう
- 重たいデータは、[pwscup-googledrive](https://drive.google.com/drive/folders/1izfvky5Uq0hb16HiDYvratQveA_XD32x?usp=sharing)において、共有リンクを使うなどしましょう
- .circleci/config.yml　は、分かっている人以外触らない
    - 自動デプロイの設定ファイルです
 
