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
    - Please check an email (Subject: "[PWSCUP2020] Your team accout").

## PWS Cup 2020 "AMIC" rule (overview) (WIP)
We will hold the AMIC ("Anonymity against Membership Inference" Contest). Details of the rules will be published at a later date.

Details of the rules is [here](./Images/PWSCUP2020_rule_20200826_e.pdf). 
<img src="./Images/overview_eng.png" width=100%>


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
PWS Committee (in the Computer Security Special Interest Group of the Information Processing Society of Japan)

## PWS Cup 2020 Schedule

The schedule is subject to change without notice.

- 2020/08/07 (Fri) - 2020/08/26 (Wed): Entries accepted
- 2020/08/26 (Wed): Rules published
    - 2020/08/26 (Wed) 17:00-19:00 JST: PWSCUP 2020 rule briefing session(@WebEx)
    - If you would like to attend the briefing session, please contact pwscup2020-info(at)iwsec.org with an email address (list) to which we send  the web-meeting URL
    - The contents will be posted this website immediately after the session
- 2020/08/27 (Thu) - 2020/09/18 (Fri): Preliminary Round
- 2020/09/24 (Thu) - 2020/10/20 (Tue): Final Round
- 2020/10/27 (Tue): Final results announced at CSS2020 
- 2020/10/27 (Tue): Poster session 


## How to register
- Check the [Entry](./entry_e.html) page

## Privacy Policy
- Check [PWS Cup 2020 Privacy Policy](./privacy_policy_e.html).

## Twitter
- [PWS Cup Official Twitter](https://twitter.com/pwscup_admin)



## Contact

- PWS2020 Committee, PWS Cup Working Group
    - pwscup2020-info(at)iwsec.org

