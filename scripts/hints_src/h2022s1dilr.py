_cls = ("<p>Boys at the 2-day event = 0.6b, and 70% of those are neither singers nor dancers, so 0.42b must be a whole number. That makes b a multiple of 50: b = 50. So 30 boys want 2 days, 21 of them neither, and 9 singers or dancers.</p>"
 "<p>All 4 male singers want 3 days, so 2 days too. The other 5 of the 9 are male dancers.</p>"
 "<p>Singers at 2 days = dancers at 2 days + 1: 4 + (girl singers) = 5 + (girl dancers) + 1. Girl singers are at most 2, so girl singers = 2 and girl dancers = 0. Girls' singers and dancers at 2 days make up 40% of the girls at 2 days: 2 = 40% of 5. So 5 girls want 2 days.</p>")
_ch1 = "70% of 60% of the boys must be a whole number. What's the smallest class size that allows that?"
_ch2 = "Write singers at 2 days as 4 + (girl singers) and dancers as 5 + (girl dancers). Girl singers can't be more than 2."
_hk = ("<p>The four totals are different, at least 1 each, and add up to 12: either 1, 2, 3, 6 or 1, 2, 4, 5. Bimla scored in at least 4 matches, and Harita beat her, so it's Bimla 4 and Harita 5. Harita is the top scorer, so she scored in matches 4 and 8 (one goal each, since even matches have one goal) plus one more match with 3 goals.</p>"
 "<p>Bimla scored in Match 1 and in three consecutive matches that avoid 4 and 8: 5, 6, 7. Odd matches hold 8 goals in total, and Match 3 equals Match 7. Harita's 3-goal match can only be Match 1, which gives Match 1 = 4, Match 5 = 2, Match 3 = Match 7 = 1.</p>"
 "<p>Amla and Sarita (1 and 2 goals) share the goals in matches 2, 3 and 5, one goal each.</p>")
_kh1 = "List the ways four different totals of at least 1 can add up to 12. Bimla has at least 4 goals and Harita has more."
_kh2 = "Harita scores 1 + 1 in matches 4 and 8, so her third match has 3 goals. Odd matches total 8. Which odd match can hold her 3 goals?"
_tok = ("<p>Factor the amounts (in thousands): 390 = 2·3·5·13, 210 = 2·3·5·7, 165 = 3·5·11, 77 = 7·11, 66 = 2·3·11.</p>"
 "<p>Adhara's value appears in only one amount: 13, so Pragnyaa got 390. Fathima's value is in all but one: 3, so Qahira got 77. Rasheeda had the most tokens, so she got 210 (2, 3, 5, 7). She got nothing from Esther, so Esther's value is 11. Dhanavi gave to Qahira (7·11), so Dhanavi is 7.</p>"
 "<p>Bithi and Chhaya are 2 and 5 in some order, and Smera and Tantra are 165 and 66 in some order. Each order works.</p>")
_tkh1 = "Factor each amount into primes. Which value appears in only one amount, and which in all but one?"
_mt = ("<p>Count the stops from the map. M to N: 3 stations, R, 9 stations, S, 5 stations: 20 gaps at 2 min each, plus 21 min of stops (2 at a junction, 1 elsewhere), so 61 min end to end. PQ is the same. A to B: 2 stations, R, 3 stations, T, 2 stations: 10 gaps at 3 min, plus 11 min of stops, so 41 min. CD is the same.</p>")
_mh1 = "Count the stations between each pair of points on the map, then add travel time per gap and stop time per station."
H = {
1: dict(ans="50", hints=[_ch1, "Also check that 80% and 60% of the boys come out whole."], why=_cls + "<p>So there are <b>50</b> boys.</p>"),
2: dict(ans="D", hints=[_ch1, "All girls want the 1-day event. Do we know whether the sixth male dancer does?"],
 why=_cls + "<p>All 4 girl dancers want the 1-day event (every girl does), so II is known. For boys at 1 day who are neither, we'd need to know if the sixth male dancer is in: 31 or 30. So <b>only II</b>.</p>"),
3: dict(ans="C", hints=[_ch1, _ch2], why=_cls + "<p>30 boys + 5 girls = 35 of 65 students: <b>7/13</b>.</p>"),
4: dict(ans="A", hints=[_ch1, "Five male dancers want 2 days, so they want 1 day too. What about the sixth?"], why=_cls + "<p>Five are certain, and the sixth is unknown: <b>5 or 6</b>.</p>"),
5: dict(ans="A", hints=[_ch1, _ch2], why=_cls + "<p>Girl dancers at 2 days = <b>0</b>.</p>"),
6: dict(ans="D", hints=[_mh1, "East-west trains leave M every 10 minutes from 6:00. Which train can Hari catch, and how long is M to N?"],
 why=_mt + "<p>The next train leaves M at 8:10. Adding 61 minutes, he reaches N at <b>9:11 am</b>.</p>"),
7: dict(ans="C", hints=[_mh1, "Try both routes: north to R then east to S, or east to V then north to S. A train from B reaches T 11 min after leaving and departs 2 min later."],
 why=_mt + "<p>Via R: the northbound train leaves T at 10:28 and reaches R at 10:43, just as an eastbound train leaves R (M departures + 13 min). It reaches S at 11:12.</p><p>Via V she'd reach S at 11:28. Earliest: <b>11:12 am</b>.</p>"),
8: dict(ans="B", hints=[_mh1, "The last southbound train from A leaves at midnight and leaves R at 0:13. Which westbound train from N reaches R by then?"],
 why=_mt + "<p>Westbound trains take 48 min from N to R and leave S 19 min after N. The 23:20 train from N reaches R at 0:08, in time for the 0:13 southbound (B at 0:41). It leaves S at 23:39. The 23:30 would reach R at 0:18, too late.</p><p>So the latest is <b>11:39 pm</b>.</p>"),
9: dict(ans="8", hints=[_mh1, "After a 41-min trip and 15-min rest, when is the next 15-minute departure slot? How long is one train's full round trip?"],
 why=_mt + "<p>A train leaves A at 0, reaches B at 41, rests until 56, so it takes the 60 departure back, and is ready at A to leave at 120. A 120-min cycle with a train every 15 min needs 120/15 = <b>8</b> trains.</p>"),
10: dict(ans="48", hints=[_mh1, "Do for each line what you'd do for AB: trip time, plus 15 min rest, rounded up to the next departure slot, gives half the cycle."],
 why=_mt + "<p>AB and CD: 120-min cycle at 15-min gaps, 8 trains each. MN and PQ: 61 + 15 = 76, next 10-min slot at 80, so a 160-min cycle at 10-min gaps: 16 trains each.</p><p>Total = 8 + 8 + 16 + 16 = <b>48</b>.</p>"),
11: dict(ans="D", hints=[_kh1, _kh2], why=_hk + "<p>Match 7 had <b>1</b> goal.</p>"),
12: dict(ans="B", hints=[_kh1, _kh2], why=_hk + "<p>Matches 1, 3, 5, 7: <b>4, 1, 2, 1</b>.</p>"),
13: dict(ans="B", hints=[_kh1, "Amla and Sarita only score in matches 2, 3 and 5, one goal each match. Where does Harita score?"],
 why=_hk + "<p>Amla and Sarita never share a match (one goal each in 2, 3 and 5), and Harita plays only in 1, 4 and 8. <b>Both</b> statements are true.</p>"),
14: dict(ans="A", hints=[_kh1, "Count matches scored in: Harita 3, Bimla 4, and Amla and Sarita 1 and 2."],
 why=_hk + "<p>Every match has a goal, and the match counts 3, 4, 1, 2 are all different. <b>Neither</b> statement is false.</p>"),
15: dict(ans="A", hints=[_kh1, "Then Sarita scored in 2 of matches 2, 3, 5 and Amla in the other one. Do those have to be next to each other?"],
 why=_hk + "<p>Sarita could have 2 and 5 (not consecutive), and Amla has a single match. So <b>neither</b> statement must be true.</p>"),
16: dict(ans="2", hints=[_tkh1, "Qahira is the one Fathima skipped. Factor her amount."], why=_tok + "<p>Qahira got 77 = 7 × 11: <b>2</b> tokens.</p>"),
17: dict(ans="C", hints=[_tkh1, "Bithi gives 2 or 5, and Dhanavi gives 7. Who has both 2 and 5 but no 7?"], why=_tok + "<p><b>Pragnyaa</b> (390 = 2·3·5·13) has both 2 and 5 and no 7, so she got Bithi's token either way and not Dhanavi's.</p>"),
18: dict(ans="3", hints=[_tkh1, "Chhaya gives 2 or 5. Count how many amounts each of those divides."], why=_tok + "<p>2 divides 390, 210 and 66; 5 divides 390, 210 and 165. Either way Chhaya awarded <b>3</b> tokens.</p>"),
19: dict(ans="3", hints=[_tkh1, "Smera got 165 or 66. How many prime factors does each have?"], why=_tok + "<p>165 = 3·5·11 and 66 = 2·3·11. Either way Smera got <b>3</b> tokens.</p>"),
20: dict(ans="C", hints=[_tkh1, "Bithi's value decides which of 165 and 66 is Smera's. Is either choice ruled out?"], why=_tok + "<p>Both orders fit, so Tantra could have got <b>either amount</b>.</p>"),
}
