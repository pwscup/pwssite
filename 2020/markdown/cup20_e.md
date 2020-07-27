# PWS Cup 2020

## What' new

- 2020/02/18(火) 本ページを作成
- 2020/07/29(水) ルール概要説明を作成


## PWS Cup 2020 匿名メンバシップ推定コンテスト AMIC ルール概要
匿名メンバシップ推定コンテスト "AMIC" (Anonymous Membership Inference Contest)を開催します。ルール詳細は後日公開します。

<img src="./Images/overview_e.png" width=100%>


- Contest Flow
  - The Committee generates "synthetic-data" for each participating team. The "sampled data" is extracted from the "synthetic-data" and distributed to the participating teams.
  - The anonymizer (each team) processes the "sampled-data" and submits the "anonymized-data". If the "anonymized-data" does not meet the specified criteria for utility, it will be disqualified.
  - The attacker (each team) receives a pair of (synthetic-data, anonymized-data) of all anonymizers other than themselves. From the "anonymized-data", the attacker estimated the "sampling data".

- Evaluation
  - Anonymization phase: the total number of successful estimates made by each attacker is deducted from the anonymizer's points, and the anonymizer with the highest score wins
  - Attack phase: the attacker with more success in estimating the sampled data of the winner of the anonymization phase wins.


- Determination of Final Ranking
  - There will be two rounds in this contest, the preliminary and final round, and each round has distribute, anonymize, and attack phase.
  - The results of the scoring in each round will be used to determine the final rankings.

## PWS Cup 2020 schedle (作成中)

- 2020/07/29(水) - 2020/08/26(水) エントリー受付
- 2020/07/??(?) ルール公開
- 2020/08/03(月) - 2020/08/31(月) 予備戦匿名化フェーズ開始
- (以降のスケジュールは検討中)
- 2020/10/26(火) CSS2020にて、最終結果発表
- 2020/10/26(火) CSS2020にて、各チームの加工・攻撃手法のポスターセッション


## 参加方法
- [参加規定](../entry.html)のページをご確認ください。

## 公式Twitter

[PWSCUP公式Twitter](https://twitter.com/pwscup_admin)で最新情報をお知らせしています。



## お問い合わせ先

- PWS2020実行委員会 Cupワーキングループ
  - (作成中)
