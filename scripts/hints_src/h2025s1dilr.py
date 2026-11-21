_inno = ("<p>Asha, Bunty and Chintu start in Elite and are all in Novice by Quarter 4. Only three demotions happen (after Q1, Q2 and Q3), so each of them is demoted once and nobody is ever promoted back. Dolly, Eklavya and Falguni are each promoted once. Nobody moves twice.</p>"
 "<p>Lalu rates Bunty in Q2, so Bunty is demoted after Q1. Lalu rates Asha and Dolly in Q3, so Asha is demoted after Q2, Chintu after Q3, and Dolly is promoted after Q3. Dolly's constant rating is 2.</p>"
 "<p>Q1 Novice: Dolly 2, and Eklavya and Falguni share 1 and 3. Q2 Novice: Bunty 1, Dolly 2, so the third gets 3. That third must be promoted after Q2 (tied with Dolly at 4 and winning on the latest rating). A constant rater can't go 1 then 3, so the third is Eklavya (1, then 3), and Falguni (always 3) was promoted after Q1.</p>"
 "<p>For Asha to be demoted after Q2, she must get 1 in Q2 (Chintu 2); her Q1 rating can be 2 or 3. In Q3, Elite gives Falguni 3, Eklavya 2 and Chintu 1, and Novice gives Bunty 3.</p>")
_ih1 = "Three people must go from Elite to Novice in three swaps. Can anyone move twice? Then use who Lalu rated in Q2 and Q3 to date each demotion."
_ih2 = "Eklavya and Falguni split 1 and 3 in Q1. Which of them can keep the same rating every quarter?"
_rt = ("<p>Davies is in chair 2 after Turn 1 (before moving), so he starts there. Chhavi starts in 7. Aslam sits next to Chhavi, and chair 1 must stay empty beside Davies, so Aslam is in 6. Bashir needs empty chairs on both sides: only chair 4 works.</p>"
 "<p>Start: Davies 2, Bashir 4, Aslam 6, Chhavi 7. Turn 1: Aslam → 1. Turn 2: Bashir → 3, so 7, 1, 2, 3 are all together (the only way to make them adjacent).</p>"
 "<p>Turn 3: Chhavi → 6 (going to 4 would block Davies). Turn 4: Davies → 4. Turn 5: Aslam → 7 (going to 2 makes Turn 6 fail). Turn 6: Bashir → 5, so 4, 5, 6, 7 are together. Turn 7: Chhavi → 1 or 3, which leaves chair 6 empty.</p>")
_rh1 = "Davies hasn't moved by the end of Turn 1, and Chhavi hasn't moved by the end of Turn 2. So where do they start? Then place Aslam and Bashir."
_tap = ("<p>Every question gets four answers that include at least one Yes, No and Maybe (6 taps), plus one more answer. So each question gets 7, 8 or 9 taps. Alia got 9, and Badal, Dilshan and Ehsaan got the same: 9 + Clive + 3k = 40 works only with k = 8 and Clive = 7.</p>"
 "<p>Alia tapped 6: Yes to Clive and Dilshan uses 2, and she can't say Yes again, so she said No to Badal and Ehsaan. Badal and Clive tapped 40 − 6 − 11 − 9 = 14 together, with Clive more.</p>"
 "<p>The \"answers can't match\" rules then fix everything. Full grid (rows answer each column's question):<br>Alia: B No, C Yes, D Yes, E No (6)<br>Badal: A Yes, C No, D No, E Yes (6)<br>Clive: A No, B Yes, D Maybe, E No (8)<br>Dilshan: A Maybe, B No, C Maybe, E Maybe (11)<br>Ehsaan: A Maybe, B Maybe, C Yes, D No (9)</p>")
_th1 = "Each question gets at least one Yes, No and Maybe from its four answers. What range of taps can one question get? Use the 40 total."
_th2 = "Alia's 6 taps include two Yeses. Nobody says Yes more than twice. What were her other two answers?"
H = {
6: dict(ans="4", hints=[_ih1, _ih2], why=_inno + "<p>Eklavya: 1 in Q1 and 3 in Q2, so his score is <b>4</b>.</p>"),
7: dict(ans="0", hints=[_ih1, "Count the demotions available before Quarter 4, and how many people must be demoted."], why=_inno + "<p>So <b>0</b> employees changed groups more than once.</p>"),
8: dict(ans="5", hints=[_ih1, "Bunty was in Novice for Q2 and Q3. Find the Q1 rating that got him demoted, and his Q3 rating from Lalu."], why=_inno + "<p>Bunty: 1 (Q1, lowest in Elite) + 1 (Q2) + 3 (Q3) = <b>5</b>.</p>"),
9: dict(ans="4", hints=[_ih1, "Which ratings stay unfixed? Look at Asha's and Chintu's Q1 ratings."],
 why=_inno + "<p>Fixed at end of Q3: Bunty 5, Dolly 6, Eklavya 6, Falguni 9. Asha (4 or 5) and Chintu (6 or 5) depend on who got 2 and 3 in Q1. So <b>4</b> are certain.</p>"),
10: dict(ans="D", hints=[_ih1, "After Q2, Asha must have the lowest Elite score (ties go to the higher latest rating). Try each split of 2 and 3 in Q1 and of 1 and 2 in Q2."],
 why=_inno + "<p>Asha gets 1 in Q2 in every case that works, but her Q1 rating can be 2 or 3. So <b>only II</b> must be true.</p>"),
11: dict(ans="4", hints=[_rh1, "Bashir needs empty chairs on both sides at the start."], why=_rt + "<p>Bashir started in chair <b>4</b>.</p>"),
12: dict(ans="D", hints=[_rh1, "Davies must reach chair 4 in Turn 4. If Chhavi took chair 4 in Turn 3, where would Davies end up?"], why=_rt + "<p>After Turn 3 the seats are 1, 2, 3 and 6, so chair 4 is empty: <b>no one</b>.</p>"),
13: dict(ans="D", hints=[_rh1, "In Turn 5 Aslam goes to 2 or 7. Check which choice lets Bashir make all four adjacent in Turn 6."], why=_rt + "<p>After Turn 6: Davies 4, Bashir 5, Chhavi 6, Aslam 7. So chairs <b>4, 5, 6 and 7</b>.</p>"),
14: dict(ans="C", hints=[_rh1, "After Turn 6, Bashir is in 5. Chhavi moves in Turn 7 from chair 6. Whichever way she goes, what's left beside Bashir?"], why=_rt + "<p>Chhavi leaves chair 6, so Bashir in 5 has only Davies (4) beside him: <b>Davies only</b>.</p>"),
19: dict(ans="7", hints=[_th1, "Alia's question got 9 and three others got equal counts. Write 9 + Clive + 3k = 40."], why=_tap + "<p>Clive received <b>7</b> taps.</p>"),
20: dict(ans="A", hints=[_th2, "Badal and Clive tapped 14 together, with Clive more. Work out the full grid with the matching rules."], why=_tap + "<p>Alia and Badal both tapped 6, so the answer is <b>Alia and Badal</b>.</p>"),
21: dict(ans="D", hints=[_th2, "Ehsaan's rule: Clive's answer to Ehsaan can't equal Ehsaan's answer to Clive. Fill in Ehsaan's answers first (he tapped 9)."], why=_tap + "<p>Clive answered Ehsaan's question <b>No</b>.</p>"),
22: dict(ans="6", hints=[_th2, "Once the grid is filled in, count the 1-tap answers."], why=_tap + "<p>Yes answers: Alia 2, Badal 2, Clive 1, Ehsaan 1 = <b>6</b>.</p>"),
}
