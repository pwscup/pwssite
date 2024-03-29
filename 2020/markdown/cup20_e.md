# PWS Cup 2020

<div style="text-align: center;">
 <font size="2">
  <a href="./cup20.html">[Japanese]</a>
 </font>
</div>

<div align="center">
 <img src="./Images/pwscup2020_poster_host.jpg" width=50%>
</div>

## What' new

- 2020/02/18 (Tue): This page was created
- 2020/07/29 (Wed): Contest overview was added
- 2020/08/07 (Fri): Contest entry started. 
    - Please read the [Participation Rules](./entry_e.html) and fill out the entry form.
- 2020/08/19 (Wed): We will hold PWS Cup 2020 rule briefing session (2020/08/26 (Wed) 17:00-19:00 JST @WebEX) )
    - Please check the "PWS Cup 2020 Schedule" below
- 2020/08/26 (Wed): PWS Cup 2020 rule briefing session was held. 
    - Details of the rules is [here(English version)](./Images/PWSCUP2020_rule_20200826_e.pdf)
- 2020/08/27 (Thu): Preliminary-anonymization Phase starts. (~2020/09/07(Mon) 23:59:59 JST).
    - Please check an email from committee (Subject: "[PWSCUP2020] Your team accout").
- 2020/09/04 (Fri): [Details of the rules Ver.2](./Images/PWSCUP2020_rule_20200904_e.pdf) is released.
    - Change log is [here](./Images/PWSCUP2020_Rule_Changelog.xlsx).
- 2020/09/09 (Wed): Preliminary-attack Phase starts. (~2020/09/18(Fri) 23:59:59 JST).
    - Please check an email from committee.
- 2020/09/23 (Wed): Preliminary phase Meetup@WebEX
    - Documents (Englinsh version) will be released on 2020/09/24(Thu).
- 2020/09/24 (Thu): Main (anonymize) phase starts (~ 2020/10/05 (Mon) 23:59:59 JST)
    - Please check an email from committee.
- 2020/09/25 (Fri): Sampling(C) and inference(E) data of the preliminary phase were released.
    - Please check an email from committee.
- 2020/10/07 (Wed): Main-attack phase starts. (~2020/10/20(Tue) 23:59:59 JST)
    - Please check an email from committee.
- 2020/10/19 (Mon): [Information for PWS Cup 2020 Session](./session_e.html) is released
- 2020/10/20 (Tue): main-attack phase has ended. Please wait for [PWS Cup2020 Session](./session_e.html).





## PWS Cup 2020 "AMIC" rule (overview) 
We will hold the AMIC ("Anonymity against Membership Inference" Contest). 

Details of the rules is [here](./Images/PWSCUP2020_rule_20200826_e.pdf). 
<img src="./Images/overview_eng.png" width=100%>

[Sample data/script: here](./Images/PubInfo_20200826.zip).


- Contest Flow
    - The **Committee** generates **Synthetic Data** for each participating team. The Committee then generates **Sampled Data** by extracting records from the Synthetic Data with the sampling ratio of 10%. The Synthetic Data is distributed to the participating teams.
    - Each team (as an **Anonymizer**) processes their Sampled Data and generates **Anonymized Data**. The Anonymizer then submits their Anonymized Data to the Committee. The submitted Anonymized data must fulfill the data utility requirements designated by the Committee, or the team will be disqualified.
    - Each team (as an **Attacker**) receives pairs of (Synthetic Data, Anonymized Data) of all Anonymizers other than themselves. From the Anonymized Data, the Attacker estimates the Sampled Data.

- Evaluation
    - Anonymizer Phase: the total number of records successfully estimated by Attackers is deducted from the Anonymizer's point. The Anonymizer with the highest points will be a winner of the anonymization phase.
    - Attacker Phase: the Attacker who successfully estimated the most records in Sampled Data submitted by the Anonymize phase winner will be a winner of the attack phase.

- Determination of Final Ranking
    - There will be two rounds in this contest: the preliminary and final round. Each round has distribution, anonymization, and attack phases.
    - The results of the scoring in both rounds will be used to determine the final rankings.

## Organizer
PWS Committee in the Computer Security Special Interest Group of the Information Processing Society of Japan  
(PWS Cup 2020 is a co-located workshop with the Computer Security Symposium 2020.)

## PWS Cup 2020 Schedule

The schedule is subject to change without notice.

- 2020/08/07 (Fri) - 2020/08/26 (Wed): Entries accepted
- 2020/08/26 (Wed): Rules published
- 2020/08/27 (Thu) - 2020/09/18 (Fri): Preliminary Round
- 2020/09/24 (Thu) - 2020/10/20 (Tue): Final Round
- 2020/10/27 (Tue): Final results announced at CSS2020 
- 2020/10/27 (Tue): Spotlight/Poster session 

## 参加チーム

<table border="1">
<tr><td>Team </td><td>Comment</td><td>Leader</td><td>Affiliation</td></tr>
<tr><td>Brown DP</td><td></td><td>-</td><td>-</td></tr>
<tr><td>鋼鉄の錬金術師</td><td>今年も錬金します。</td><td>中川拓麻</td><td>日鉄ソリューションズ株式会社</td></tr>
<tr><td>Yichi</td><td></td><td>Ruska</td><td>-</td></tr>
<tr><td>小熊軟糖🧸</td><td></td><td>-</td><td>-</td></tr>
<tr><td>たけのこ半島</td><td>頑張ります</td><td>-</td><td>-</td></tr>
<tr><td>JOSE2</td><td>がんばります</td><td>-</td><td>三菱電機株式会社</td></tr>
<tr><td>サイコロ</td><td></td><td>-</td><td>-</td></tr>
<tr><td>SynIPA</td><td></td><td>Alexandre Roy-Gaumond</td><td>UQAM</td></tr>
<tr><td>ホンワカインコ</td><td>ほんわか楽しみたいと思います</td><td>-</td><td>-</td></tr>
<tr><td>🍎🍎🍎</td><td>がんばります</td><td>北島祥伍</td><td>株式会社ミクシィ</td></tr>
<tr><td>ステテコ大木</td><td>🥺</td><td>菅沼弥生</td><td>静岡大学大木研究室</td></tr>
<tr><td>ステテコ西垣</td><td>明治大には負けません！</td><td>北川沢水</td><td>静岡大学西垣研究室</td></tr>
<tr><td>ステテコ菊池</td><td>静岡大には負けません</td><td>伊藤聡志</td><td>明治大学大学院</td></tr>
<tr><td>匿工野郎Aチーム </td><td></td><td>-</td><td>-</td></tr>
<tr><td>天然水</td><td>精一杯がんばります！</td><td>石原詢大</td><td>筑波大学</td></tr>
<tr><td>docomo freshers</td><td>楽しみます</td><td>片山源太郎</td><td>株式会社NTTドコモ</td></tr>
<tr><td>wakanalie</td><td></td><td>-</td><td>-</td></tr>
<tr><td>初ぼっち</td><td>ぼっちなので何もできないかもしれません。</td><td>-</td><td>-</td></tr>
<tr><td>テレぼっち</td><td>テレワークなので、例年よりぼっち度をアゲてがんばります！</td><td>井口誠</td><td>Kii株式会社</td></tr>
<tr><td>Mostly.AI</td><td>-</td><td>-</td><td>-</td></tr>

</table>

## Result
### Final 
- 1st 333 point 03 鋼鉄の錬金術師（Anonymize 1st、Attack 2nd）
- 2nd 143 point 08 サイコロ　　　（Anonymize 3rd、Attack 4th）
- 3rd 083 point 06 たけのこ半島　（Anonymize 5th、Attack 7th）

### Anonymize
- 1st 877 point 03 鋼鉄の錬金術師
- 2nd 840 point 18 天然水第
- 3rd 813 point 08 サイコロ

### Attack
- 1st 122 point 14 ステテコ大木
- 2nd 121 point 03 鋼鉄の錬金術師
- 3rd 108 point 21 wakanalie

[Detail Result (GoogleSpreadSheet)](https://drive.google.com/file/d/1ezGV1ip6F9PgHhMkZxA82SnSLlqhkv9O/view?usp=sharing).

## How to register
- Check the [Entry](./entry_e.html) page

## PWS Cup 2020 session
- Check the [Information for PWS Cup 2020 session](./session_e.html) page.

## Privacy Policy
- Check [PWS Cup 2020 Privacy Policy](./privacy_policy_e.html).

## Twitter
- [PWS Cup Official Twitter](https://twitter.com/pwscup_admin)



## Contact

- PWS Cup 2020 Working Group in the PWS Committee

    - pwscup2020-info(at)iwsec.org

