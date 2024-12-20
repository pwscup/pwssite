# PWS Cup 2024

![](./Images/poster2024.jpg){.center}

## PWS Cup 2024 は終了しました。ご参加頂いたみなさま、ありがとうございました。

## What's New
- 2024/11/04(月) PWS Cup 2024 [発表会資料](./Images/20241024_PWSCUP2024.pdf)を公開
- 2024/11/04(月) [本戦＆総合の結果](./Images/result_main_and_overall.xlsx)と[本戦結果詳細](./Images/result_main_detail.xlsx)を公開
- 2024/11/04(月) ポスターを一部公開
- 2024/10/21(月) 審査員を公開
- 2024/10/15(火) 10/24(木)のPWS Cup 2024タイムテーブルを公開
- 2024/10/01(火) [本戦攻撃フェーズの攻撃用データ(19.3MB)](./Images/mainAttackData.zip)を公開
- 2024/09/09(月) 予備戦の結果と各チームのデータを公開
- 2024/09/09(月) PWSCup2024中間説明会の動画と資料をアップ
- 2024/08/16(金) [予備戦攻撃フェーズの攻撃用データ](./Images/preAttackData2.zip)を公開
- 2024/08/16(金) [予備戦加工フェーズの結果](./Images/preAnonymizationPhaseScore.csv)を公開
- 2024/07/31(水) PWSCup2024＆iPWSCup2024 ルール説明資料Ver1.2を公開（P.17に記載の得点ルールを一部変更）
- 2024/07/26(金) 参加チームを公開
- 2024/07/23(火) PWSCup2024＆iPWSCup2024 ルール説明資料Ver1.1を公開
- 2024/07/16(火) PWS Cup 2024用の[GitHubリポジトリ](https://github.com/pwscup/pwscup2024-scripts)にて、加工・評価・チェックスクリプトの開発版を配置(順次更新予定) 
- 2024/07/14(日) PWSCup2024＆iPWSCup2024説明会の動画と資料をアップ
- 2024/07/12(金) [エントリー方法](./entry.html)を公開
- 2024/06/22(土) [PWSCup2024＆iPWSCup2024説明会の参加登録URL](https://docs.google.com/forms/d/e/1FAIpQLScY3xI5OZ3x-ry0f8vFMXfPg_MtxvCpgMyljJrbd1lpjFK6Cw/viewform)を公開
- 2024/06/14(金) 本ページを作成

## PWS Cup 2024 概要
### コンテストストーリー
企業Aは顧客データを利用して映画の推薦システムを作りたいと思い、推薦システム開発のコンペのために顧客データを匿名化してコンペ参加者に提供することとした。しかし匿名化したつもりでも、外部のデータと突き合わせるなどして個人特定されたりプライバシーが侵害されたりした事例がある。さらに最近では、安全とおもわれる匿名化データや統計データでも複数組み合わせると元のデータが復元されてしまう「データベース再構築攻撃」も問題となっている。企業Aは、個人特定攻撃やデータベース再構築攻撃を防ぎつつ、有用性の高い匿名化データを作成できるだろうか？

### コンテスト概要
コンテスト参加者は、加工者と攻撃者の双方の立場となって、データの加工と、加工されたデータへの攻撃技術を競います。データの加工では、参加者は顧客データを公開したい企業を想定した加工者となり、与えられたデータを加工してデータに含まれる人のプライバシーを保護することを目指します。加工されたデータへの攻撃では、参加者はデータの中身を暴こうとする人を想定した攻撃者となり、他の参加者が加工したデータに含まれる人の秘密の情報をより多く暴くことを目指します。

### コンテストの流れ
コンテストは、以下の2つのフェーズからなります。

1. 加工フェーズ:
   - 各チームは、映画の評価に関する架空のデータから、複数の匿名化データを作成する（各匿名化データは、多属性の元データから、分析用途に応じて必要な属性のみ抽出したデータを加工したものとする）。
   - 匿名化データは、有用性をなるべく損ねることなく、他人が元の情報を特定しづらいように加工すること。
2. 攻撃フェーズ:
   - 各チームは、出題者によっていくつか黒塗りされた元データの値を、匿名化データを用いて推定する（データベース再構築攻撃）。
   - また、氏名等が切り離された元データを、匿名化データを用いて氏名等とつなぎ合わせて個人特定を試みる。

これらを順に実施した後、出題者により各チームの加工と攻撃の結果が評価されます。加工の評価は加工データと元データからそれぞれ得られる分析結果の近さ（近いほどよい）と秘密データの他のチームからの正しい推測の困難さ（困難であるほどよい）の観点から、攻撃の評価は他のチームの加工データに対する推測の正確さ（正確であるほどよい）の観点から、それぞれ行います。コンテスト期間中に加工フェーズ、攻撃フェーズ、評価の一連の流れを2回実施します。1回目を予備戦、2回目を本戦と呼び、予備戦と本戦での評価結果を総合して本コンテストの勝者を決定します。

### 加工フェーズの手順
1. 事務局から配布データ3セットを受け取る
2. 匿名化するデータを配布データ3セットから1セット選ぶ
3. 選んだ配布データセットのID（例：00）を[Forumタブのスレッド](https://www.codabench.org/forums/3180/)で申告する
4. 選んだ配布データセットのファイル名（例：Bi00.csv, Bi00_0.csv, ... , Bi00_9.csv）をチームIDを含めたIDにリネームする
	* 例：チームIDが99の場合、B99.csv, B99_0.csv, ... , B99_9.csvとする（iは含まないことに注意）
5. 選んだ配布データセットを匿名化する
	* 例：チームIDが99の場合、B99_0.csv, ... , B99_9.csvをそれぞれ匿名化した10個のファイルC99_0.csv, ... , C99_9.csvを作成する
6. checkCi.pyを用いて、匿名化した10個のファイルの形式に問題がないことを確認する
	* 例：python checkCi.py B99_0.csv C99_0.csv
7. チームID（例：99）を記載したファイルid.txtを作成する
8. 匿名化した10個のファイル（例：C99_0.csv, C99_1.csv, ... , C99_9.csv）とid.txtをzipファイルにする
	* ファイル名は任意。例えばsubmission.zipとする。zipファイルの直下に匿名化した10個のファイルとid.txtが配置されるようにする。フォルダを含めるとエラーになるので注意
9. My Submissionsタブを押し、少し下にあるクリップのアイコンを押すと提出ファイル選択のウィンドウが出るので、前で作成したzipファイルを選択して提出する
	* ファイル選択前に、クリップのアイコンの少し上にあるコメント欄にコメントを書くと、（Resultsタブを押すと出てくる）リーダーボードに結果と共にコメントが表示される
10. 画面下に、提出したzipファイルの処理状況が表示される。Status欄がFinishedになれば処理完了
	* 5分以上かかる場合もあるので気長に待つ。不備があると、Failedになったり、SubmittingやRunningのままになったりする。原因不明でFinishedにならない場合は事務局（pwscup2024-info(at)csec.ipsj.or.jp（“(at)”をアットマーク“@”に置換ください））までご連絡ください
11. Status欄がFinishedになるとActions欄に現れる二つのアイコンのうち、左側のアイコン（カーソルを合わせるとAdd to Leaderboradと表示される）を押す
12. チェックマークのアイコンに変われば完了。リーダーボードに反映される
* 匿名化したファイルを変更したい場合は、変更した10個のファイルとid.txtを再度zipファイルにしてして再提出する
* 以前に提出した結果をリーダーボードに反映したい場合は、以前に提出した結果のActions欄の左側アイコンをクリックしてチェックマークアイコンにする

### 攻撃フェーズの手順
1. 攻撃用データ（予備選、本選）をダウンロードする
   * コードの修正や提出失敗データの取り込みにより、リーダーボードの結果と多少異なる場合があるので注意 
2. 各チームに対する攻撃結果データを作成する（50行2列のcsv形式とし、1列目は個人特定攻撃結果、2列目はDB再構築攻撃結果とする）
3. 各チームの攻撃結果データをまとめた単一のcsvファイル（50行44列のデータ）を作成する
   * 2i-1列目にチームiに対する個人特定攻撃結果、2i列目にチームiに対するDB再構築攻撃結果を記入する
   * 自チームおよび加工データ提出無しチーム（予備選ではチーム08, 13, 19）に対応する列は、空欄とするかアスタリスク（'*'）で埋める
   * ファイル名はExx.csv（xxは自チームID）とする
4. Exx.csvとid.txtをzipファイルにする（ファイル名は任意）
5. 加工フェーズ同様、My Submissionsからzipファイルを提出し、結果をリーダーボードに反映させる

<a id="manuals"></a>

## 参加者向け資料
- [本戦＆総合の結果](./Images/result_main_and_overall.xlsx)
- [本戦結果詳細](./Images/result_main_detail.xlsx)（2行目の"XXi"はTeamXXの個人特定攻撃の成功数、"XXd"はTeamXXのDB再構築攻撃の成功数）
- [10/24発表会資料](./Images/20241024_PWSCUP2024.pdf)
- [予備戦の結果と各チームのデータ(zip(7.3MB))](./Images/pre.zip)
- [PWSCup2024中間説明会の動画](https://youtu.be/bvbgCIdS5Js)
- [PWSCup2024中間説明会の資料(PDF)](./Images/20240909_PWSCUP2024_middle.pdf)
- [予備選加工フェーズの結果(csv)](./Images/preAnonymizationPhaseScore.csv)
- [PWSCup2024＆iPWSCup2024 ルール説明資料Ver1.2(PDF)](./Images/20240731_PWSCUP2024_iPWSCUP2024.pdf)
- [PWSCup2024＆iPWSCup2024 ルール説明資料Ver1.1(PDF)](./Images/20240723_PWSCUP2024_iPWSCUP2024.pdf)
- [PWSCup2024＆iPWSCup2024説明会の動画](https://youtu.be/uEHFeoOJ4Hg)
- [PWSCup2024＆iPWSCup2024説明会の資料(PDF)](./Images/20240712_PWSCUP2024_iPWSCUP2024.pdf)

## 主催
情報処理学会 コンピュータセキュリティ研究会 PWS組織委員会  
（コンピュータセキュリティシンポジウム2024に併催）

<a id="schedule"></a>

## PWS Cup 2024 スケジュール
スケジュールは予告なく変更することがあります。あらかじめご了承ください。
本ページに記載の日時は特に断りのない限り日本標準時(JST)です。システムに記載の日時は協定世界時(UTC)ですので、ご注意ください。

<table border="0">
<tr><td> <strong>日付</strong> </td><td> <strong>イベント</strong> </td></tr>
<tr><td> 2024/07/12(金) 16:00~17:00 </td> <td> PWS Cup 2024＆<a href="https://www.iwsec.org/pws/ipws2024/index.html"> iPWS Cup 2024</a>説明会 （参加登録は<a href="https://docs.google.com/forms/d/e/1FAIpQLScY3xI5OZ3x-ry0f8vFMXfPg_MtxvCpgMyljJrbd1lpjFK6Cw/viewform">こちら</a>)</td></tr>
<tr><td> 2024/07/12(金) ~ 2024/07/24(水) </td> <td> エントリー受付期間 </td></tr>
<tr><td> 2024/07/26(金) ~ 2024/09/02(月) </td> <td> 予備戦 </td></tr>
<tr><td> 2024/09/10(火) ~ 2024/10/15(火) </td> <td> 本戦 </td></tr>
<tr><td> 2024/10/24(木) </td> <td> 発表・表彰式 </td></tr>
</table>

## PWS Cup 2024 発表・表彰式

日時：2024/10/24(木)

場所：神戸国際会議場 B会場（国際会議室301）

タイムテーブル：

9:10-9:30 開会式、競技説明、結果発表

9:30-10:20 チーム01～07 プレゼン（各チーム7分）

10:20-10:40 休憩　※CSSの休憩時間と同じ時間帯

10:40-11:25 チーム01～07 ポスター発表

11:30-12:20 チーム08～14 プレゼン（各チーム7分）

12:20-13:40 昼休み　※CSSの昼休みと同じ時間帯

13:40-14:25 チーム08～14 ポスター発表

14:30-15:20 チーム15～21 プレゼン（各チーム７分）

15:20-15:40 休憩　※CSSの休憩時間と同じ時間帯

15:40-16:25 チーム15～21 ポスター発表

16:25-16:50 休憩（授賞審査）

	審査員：井口誠（Kii）、小野元（NICT）、菊池浩明（明治大）、千田浩司（群馬大）、中村優一（ソフトバンク）、濱田浩気（NTT）、東貴範（TOPPANデジタル）、藤田真浩（三菱電機）、古川諒（NEC）、前田若菜（LINEヤフー）

16:50-17:10 表彰式、閉会式

## 参加方法
- [エントリー方法のページ](./entry.html)をご参照ください。

## 参加チーム
<table border="1">
<tr><th>チームID</th><th>チーム名</th><th>意気込み</th><th>チーム代表者</th><th>所属</th><th>ポスター</th></tr>
<tr><td>01</td><td>宮地研.exe</td><td>頑張ります！</td><td>柳下 智史</td><td>大阪大学　宮地研究室</td><td>-</td></tr>
<tr><td>02</td><td>私達日本語本当下手</td><td>張り切って行こう！！</td><td>陳 柏瑄</td><td>陽明交通大学</td><td>-</td></tr>
<tr><td>03</td><td>ポップコーン</td><td>がんばります。</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>04</td><td>Hots</td><td>-</td><td>郭 亚楠</td><td>Inner Mongolia University of Technology</td><td>[Team04](./Images/pwscup2024_poster_team04.pdf)</td></tr>
<tr><td>05</td><td>SHA-NES</td><td>今年は総合優勝！</td><td>-</td><td>NECソリューションイノベータ</td><td>-</td></tr>
<tr><td>06</td><td>神ぼ大νττ</td><td>馬が逃げ，ぼっちがきた</td><td>小林 雅弥</td><td>神奈川大学</td><td>-</td></tr>
<tr><td>07</td><td>たけのこ映画守り隊</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>08</td><td>0xA</td><td>面白そうだとなと思い、参加しました。</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>09</td><td>ステテコ泥棒</td><td>神戸リベンジャーズ・雪辱・ステテコ実力不足</td><td>-</td><td>明治大学 / 三菱電機</td><td>[Team09](./Images/pwscup2024_poster_team09.pdf)</td></tr>
<tr><td>10</td><td>動的計画法</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>11</td><td>Gunmataro117</td><td>PWS CUP 2024に参加することになり、<br>大変光栄です。この大会を通じて、<br>最高のパフォーマンスを発揮し、<br>自分自身の限界に挑戦することを<br>楽しみにしています。努力と準備を<br>重ねてきましたので、<br>自信を持って競技に臨み、<br>素晴らしい成果を収めたいと思います。<br>皆さんの応援に感謝し、全力で頑張ります</td><td>岡嶋 佳歩</td><td>群馬大学</td><td>[Team11](./Images/pwscup2024_poster_team11.pdf)</td></tr>
<tr><td>12</td><td>HAL</td><td>頑張ります</td><td>松本 知優</td><td>大阪大学</td><td>-</td></tr>
<tr><td>13</td><td>（出場取消）~~無量匿名処~~</td><td>~~『勝つさ』~~</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>14</td><td>privocy</td><td>推して参る</td><td>-</td><td>静岡大学</td><td>-</td></tr>
<tr><td>15</td><td>ES5</td><td>頑張ります</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>16</td><td>佐古研究室</td><td>-</td><td>渡邉 健</td><td>早稲田大学</td><td>-</td></tr>
<tr><td>17</td><td>こそっとアタック、しれっとブロック</td><td>プライバシーを守るのは簡単さ、攻撃かわしてデータを探査</td><td>岡野 真空</td><td>静岡大学</td><td>-</td></tr>
<tr><td>18</td><td>匿名アノニマス</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>19</td><td>RITCHEY</td><td>はじめての参加です！</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>20</td><td>KAT-TUNE</td><td>共同チームで力を合わせます！</td><td>-</td><td>KDDI総合研究所 / ARISE analytics / トヨタ自動車</td><td>[Team20](./Images/pwscup2024_poster_team20.pdf)</td></tr>
<tr><td>21</td><td>PR.AVATECT</td><td>-</td><td>-</td><td>TOPPANデジタル</td><td>[Team21](./Images/pwscup2024_poster_team21.pdf)</td></tr>
<tr><td>22</td><td>春日部防衛隊（かすかべ防衛隊）</td><td>-</td><td>CHEN, YI-HSUAN</td><td>National Yang Ming Chiao Tung University</td><td>-</td></tr>
</table>

<table border="1">
<tr><th>チームID</th><th>アカウント</th><th>予備戦配布データ</th><th>予備戦採用データ</th><th>本戦配布データ</th><th>本戦採用データ</th></tr>
<tr><td>01</td><td>myjlabexe</td><td>10, 20, 30</td><td>30</td><td>10, 20, 30</td><td>20</td></tr>
<tr><td>02</td><td>zelret</td><td>24, 40, 87</td><td>40</td><td>51, 55, 56</td><td>55</td></tr>
<tr><td>03</td><td>jbstkf</td><td>55, 66, 77</td><td>77</td><td>05, 06, 07</td><td>06</td></tr>
<tr><td>04</td><td>rq1543179</td><td>08, 09, 12</td><td>08</td><td>12, 15, 16</td><td>16</td></tr>
<tr><td>05</td><td>shioriabe</td><td>02, 14, 28</td><td>14</td><td>04, 14, 28</td><td>14</td></tr>
<tr><td>06</td><td>masaya</td><td>58, 15, 05</td><td>58</td><td>09, 34, 49</td><td>34</td></tr>
<tr><td>07</td><td>takenoko</td><td>51, 52, 53</td><td>51</td><td>01, 02, 03</td><td>03</td></tr>
<tr><td>08</td><td>yanomichi</td><td>07, 42, 88</td><td></td><td>18, 22, 23</td><td>22</td></tr>
<tr><td>09</td><td>autefu</td><td>21, 86, 91</td><td>21</td><td>00, 13, 53</td><td>13</td></tr>
<tr><td>10</td><td>pwscup2024</td><td>13, 16, 17</td><td>16</td><td>24, 25, 26</td><td>24</td></tr>
<tr><td>11</td><td>kabutookajima</td><td>18, 19, 25</td><td>25</td><td>27, 29, 31</td><td>29</td></tr>
<tr><td>12</td><td>grape1977</td><td>03, 50, 54</td><td>54</td><td>11, 41, 58</td><td>58</td></tr>
<tr><td>13</td><td>harada</td><td>（出場取消）~~11, 23, 69~~</td><td></td><td></td><td></td></tr>
<tr><td>14</td><td>shibata</td><td>22, 33, 44</td><td>33</td><td>32, 33, 35</td><td>35</td></tr>
<tr><td>15</td><td>pwscup2024kobe</td><td>90, 80, 70</td><td>80</td><td>64, 65, 66</td><td>64</td></tr>
<tr><td>16</td><td>mgoto</td><td>26, 27, 29</td><td>26</td><td>36, 37, 38</td><td>36</td></tr>
<tr><td>17</td><td>okano</td><td>43, 57, 99</td><td>43</td><td>39, 40, 42</td><td>39</td></tr>
<tr><td>18</td><td>hajime</td><td>31, 32, 34</td><td>31</td><td>17, 19, 54</td><td>17</td></tr>
<tr><td>19</td><td>ritz2024</td><td>01, 04, 06</td><td></td><td>67, 68, 69</td><td>68</td></tr>
<tr><td>20</td><td>kattune</td><td>35, 36, 37</td><td>35</td><td>43, 44, 45</td><td>45</td></tr>
<tr><td>21</td><td>takanori</td><td>00, 79, 89</td><td>00</td><td>08, 21, 59</td><td>59</td></tr>
<tr><td>22</td><td>crbfwd</td><td>38, 39, 41</td><td>38</td><td>46, 47, 48</td><td>46</td></tr>
</table>

## 最終結果
### 総合
- 優勝　Team04 : Hots
- 第2位　Team21 : PR.AVATECT 
- 第3位　Team10 : 動的計画法 
- 第4位　Team11 : Gunmataro117
- 第5位　Team09 : ステテコ泥棒

### ベストアタック賞
- Team20 : KAT-TUNE

### ベストプレゼン賞
- Team16 : 佐古研究室

### ベストデータサイエンティスト賞
- Team12 : HAL

## プライバシーポリシー
- [プライバシーポリシーのページ](./privacy_policy.html)をご参照ください。

## 公式X(旧Twitter)
[PWSCUP公式X](https://twitter.com/pwscup_admin)で最新情報をお知らせしています。

<a id="contact"></a>

## お問い合わせ先
PWS組織委員会 PWS Cup 2024 ワーキンググループ  
- pwscup2024-info(at)csec.ipsj.or.jp（"(at)"をアットマーク"@"に置換ください）
