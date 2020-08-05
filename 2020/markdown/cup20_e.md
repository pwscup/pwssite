# PWS Cup 2020


<div style="text-align: center;">
 <font size="2">
  <a href="./cup20.html">[Japanese]</a>
 </font>
</div>

<div align="center">
 <img src="./Images/pwscup2020_poster.png" width=50%>
</div>

## What' new

- 2020/02/18 (Tue): This page was created
- 2020/07/29 (Wed): Contest overview was added
- 2020/08/06 (Thu): Contest registratin started 


## PWS Cup 2020 "AMIC" rule (overview) (WIP)
The Anonymous Membership Inference Contest "AMIC" ("Anonymity against Membership Inference" Contest) will be held. Details of the rules will be published at a later date.

<img src="./Images/overview_eng.png" width=100%>


- Contest Flow
    - The Committee generates "synthetic-data" for each participating team. The "sampled data" is extracted from the "synthetic-data" and distributed to the participating teams.
    - The anonymizer (each team) processes the "sampled-data" and submits the "anonymized-data". If the "anonymized-data" does not meet the specified criteria for utility, it will be disqualified.
    - The attacker (each team) receives a pair of (synthetic-data, anonymized-data) of all anonymizers other than themselves. From the "anonymized-data", the attacker estimated the "sampled-data".

- Evaluation
    - Anonymization phase: the total number of successful estimates made by each attacker is deducted from the anonymizer's points, and the anonymizer with the highest score wins
    - Attack phase: the attacker with more success in estimating the sampled data of the winner of the anonymization phase wins.


- Determination of Final Ranking
    - There will be two rounds in this contest, the preliminary and final round, and each round has distribute, anonymize, and attack phase.
    - The results of the scoring in each round will be used to determine the final rankings.

## PWS Cup 2020 schedle (WIP)

- 2020/08/06(Thu) - 2020/08/26(Wed) Entries accepted
- 2020/08/?? (?) Rules published
- 2020/08/27 (Thu) - 2020/09/??(?) Preliminary round Anonymization Phase
- (The schedule after is under consideration.)
- 2020/10/26(Tue) Final results announced at CSS2020 
- 2020/10/26(Tue) Poster session 


## How to register
- Check the [Entry](./entry_e.html) page

## Twitter

[PWS Cup Official Twitter](https://twitter.com/pwscup_admin)



## Contact

- PWS2020 Committee
    - pwscup2020-info(at)iwsec.org

