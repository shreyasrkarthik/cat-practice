_air = "<p>To go from X to Y and come back the same day, you need a morning flight X→Y and an evening flight Y→X. Every direct link between two cities that people use therefore needs 4 flights: morning both ways and evening both ways.</p>"
_ah1 = "For one pair of cities, list the flights needed so that someone in either city can go out in the morning and come back in the evening."
_g = ("<p>Allowed links: A–G2 (3), B–G3 (2), C–G4 (2) and the G1 links A–B, B–C, C–A. The 7 outer cities each hang off one G1 city, so all 7 of those links are needed.</p>"
 "<p>The official answer counts all 3 G1 links: 10 links × 4 = 40. Note: if a B-to-C trip may change planes at A, only 2 G1 links are needed and the count would be 36. The key treats every G1 pair as a direct link, so go with 40 here.</p>")
_gh2 = "Each outer city can only fly to one G1 city. Count the links, then multiply by the flights each link needs."
_car = ("<p>Route A-M-B with k cars takes 6 + 3(k−1) + 20 + 0.9(k−1) = 26 + 3.9(k−1). Route A-N-B with j cars takes 20 + (j−1) + 6 + 3(j−1) = 26 + 4(j−1).</p>"
 "<p>Split 2 and 2: A-M-B takes 29.9 and A-N-B takes 30. A car that switches joins a route with 3 cars (33.8 or 34), so nobody gains. A 3–1 split fails: a car on the 3-car route saves time by moving.</p>")
_ch1 = "Write the time for each route as a formula in the number of cars on it. Then try each split of the 4 cars."
_ch2 = "A split works only if no single car can switch routes and arrive sooner."
_car3 = ("<p>With a cars on A-M-B, b on A-N-B and c on A-M-N-B: A-M takes 6 + 3(a+c−1), N-B takes 6 + 3(b+c−1), M-N takes 7 + (c−1), M-B takes 20 + 0.9(a−1), A-N takes 20 + (b−1).</p>"
 "<p>a = 1, b = 1, c = 2: A-M = 12, M-B = 20, A-N = 20, N-B = 12, M-N = 8. Every route takes <b>32</b> minutes. Check any one car moving: each move puts it on a slower route, so this is the only split that holds.</p>")
_ch3 = "Let a, b, c be the cars on A-M-B, A-N-B and A-M-N-B. The A-M road carries a + c cars; the N-B road carries b + c."
_cet = ("<p>Let x be the count at or above 80 in only P (also only C, only M) and y the count in all three. 3x + 150 + y = 200, so 3x + y = 50.</p>"
 "<p>Below 80 in P = 2x + (C and M only), in C = 2x + (P and M only), in M = 2x + (P and C only). With the ratio 4k : 2k : k and the three pair groups adding to 150: 6x + 150 = 7k. With x at most 16, x = 3 (k = 24) or x = 10 (k = 30).</p>"
 "<p>x = 3: PC 18, PM 42, CM 90, all three 41. x = 10: PC 10, PM 40, CM 80, all three 20.</p>")
_eh1 = "Let x be the number in only P (= only C = only M) and y the number in all three. What does 200 give you?"
_eh2 = "Write each \"below 80th percentile\" count in terms of x and the pair groups, then use the ratio 4:2:1."
_ff = ("<p>Client 1 (10:00): Anish makes the burger 10:00–10:10, Bani the ice cream 10:00–10:02, fries 10:00–10:05.</p>")
_fh1 = "Draw a time line for Anish, Bani and the fryer, starting at 10:00."
_fh2 = "Fries can only start once the order is in and the fryer is free. Nothing can be added to a batch already frying."
_sq = ("<p>For each person, look outward in all four directions. Someone counts if they're lower than this person and higher than everyone between them. The counts for each platform, row by row:</p>"
 "<p>Row 1: 3, 0, 1, 3, 0. Row 2: 4, 2, 2, 0, 5. Row 3: 1, 4, 1, 6, 1. Row 4: 1, 4, 3, 0, 1. Row 5: 0, 2, 2, 1, 6.</p>")
_sh1 = "Check the example first: the 8 in row 3 is reached by 4 people. Then do the same count for each platform."
_sh2 = "Walking away from a person, the first lower one always counts. After that, only someone taller than everyone passed so far (and still lower than the person) counts."
_tp = ("<p>21 people in 5 teams with the challenging team one bigger: four teams of 4 and one of 5. In month 1 the SE counts go down by one from T1, and add to 10: T1 4, T2 3, T3 2, T4 1, T5 0.</p>"
 "<p>As (SE, RE): Month 1: T1 (4,1), T2 (3,1), T3 (2,2), T4 (1,3), T5 (0,4). Month 2: (1,3), (4,1), (2,2), (2,2), (1,3). Month 3: (0,4), (1,3), (4,1), (3,1), (2,2). Month 4: (0,4), (1,3), (2,2), (5,0), (2,2). Month 5: (0,4), (0,4), (2,2), (4,0), (4,1).</p>")
_th1 = "Team sizes first: 21 people, five teams, one team one bigger. Then the SE counts in month 1 must add to 10."
_th2 = "Apply rule a, then rule b, one month at a time. Rule b is skipped when T1 has no SE or T5 has no RE (same for T2 and T4)."
_pts = "<p>Each person works in one team every month, so 5 projects. A challenging project gives 200/5 = 40 points each, a standard one 100/4 = 25. With k challenging projects: 125 + 15k, so the possible totals are 125, 140, 155, 170, 185 and 200.</p>"
H = {
1: dict(ans="C", hints=[_ah1, "Count the ordered pairs of cities, then the flights each needs."], why=_air + "<p>Each of the 45 pairs needs 4 flights: 45 × 4 = <b>180</b>. (45 or 90 forgets the return trip or one of the two directions.)</p>"),
2: dict(ans="C", hints=[_ah1, "Every flight touches a hub. Count each hub's links to the other 9 cities, but don't count a hub-to-hub link twice."], why=_air + "<p>Each hub links to 9 cities: 3 × 9 = 27 links, minus the 3 hub-to-hub links counted twice = 24 links. 24 × 4 = <b>96</b>. Any two non-hub cities connect through one hub.</p>"),
3: dict(ans="40", hints=[_ah1, _gh2], why=_air + _g),
4: dict(ans="4", hints=[_ah1, "After the change, A links only to B, and C–A is gone. Count the links before and after."], why=_air + _g + "<p>After the change: A–B and B–C, plus the 7 outer cities (G2 moves under B or C). That's 9 links, 36 flights. The reduction is 40 − 36 = <b>4</b>.</p>"),
5: dict(ans="2", hints=[_ch1, _ch2], why=_car + "<p>So <b>2</b> cars take A-N-B.</p>"),
6: dict(ans="B", hints=[_ch1, _ch2], why=_car + "<p>30 − 29.9 = <b>0.1</b> minutes.</p>"),
7: dict(ans="2", hints=[_ch3, "Try the splits where no route has all 4 cars. In the right one every car takes the same time."], why=_car3 + "<p><b>2</b> cars take A-M-N-B.</p>"),
8: dict(ans="B", hints=[_ch3, "Try the splits where no route has all 4 cars. In the right one every car takes the same time."], why=_car3 + "<p>The time is <b>32</b> minutes. 29.9 and 30 were the times before the new road, and that split no longer holds.</p>"),
9: dict(ans="A", hints=[_eh1, _eh2], why=_cet + "<p>The separate test is for those at or above 80 in P but not eligible for the AET, which means only P: x = <b>3 or 10</b>.</p>"),
10: dict(ans="60", hints=[_eh1, _eh2 + " Then use \"multiple of 5\" to pick x."], why=_cet + "<p>All three = 41 or 20; only 20 is a multiple of 5, so x = 10. P and M: 40 + 20 = <b>60</b>.</p>"),
11: dict(ans="170", hints=[_eh1, _eh2 + " Then use \"multiple of 5\" to pick x."], why=_cet + "<p>With x = 10: AET takes everyone in at least two sections: 150 + 20 = <b>170</b>.</p>"),
12: dict(ans="A", hints=[_eh2, "Count everyone at or above 80 in P in both cases. Then remember that only AET candidates skip BIE's separate test."], why=_cet + "<p>At or above 80 in P: x = 3 gives 3 + 18 + 42 + 41 = 104; x = 10 gives 80. So x = 3. AET candidates with P: 18 + 42 + 41 = 101. Of the 400 with P at 80+, the rest sit the separate test: 400 − 101 = <b>299</b>.</p>"),
13: dict(ans="B", hints=[_fh1, "The burger is the slowest item."], why=_ff + "<p>The order is done when the burger is done: <b>10:10</b>.</p>"),
14: dict(ans="C", hints=[_fh1, "One order at a time: client 2 starts only at 10:10, client 3 only after client 2 is done."], why=_ff + "<p>Client 2: fries 10:10–10:15, ice cream 10:10–10:12, done 10:15. Client 3: burger 10:15–10:25, fries 10:15–10:20. Done at <b>10:25</b>.</p>"),
15: dict(ans="A", hints=[_fh1, _fh2], why=_ff + "<p>Client 2 at 10:05: the fryer is free (client 1's fries just finished), so fries 10:05–10:10. Bani is free and makes the ice cream 10:05–10:07. Done at <b>10:10</b>.</p>"),
16: dict(ans="B", hints=[_fh1, "Client 3's burger goes to whoever is free first at 10:07. Then mark each minute where exactly one person is working."], why=_ff + "<p>Bani: ice cream for client 2 10:05–10:07, then client 3's burger 10:07–10:17. Anish is free from 10:10.</p><p>Exactly one idle: 10:02–10:05 (Bani idle, Anish busy) = 3 min, and 10:10–10:17 (Anish idle, Bani busy) = 7 min. After 10:17 both are idle. Total <b>10</b> minutes.</p>"),
25: dict(ans="C", hints=[_sh1, _sh2], why=_sq + "<p>Count the 1s: <b>7</b>.</p>"),
26: dict(ans="D", hints=[_sh1, "Who could be lower than 1?"], why="<p>No one is lower than 1 m, so a person at 1 m <b>can't be reached by anyone</b>.</p>"),
27: dict(ans="C", hints=[_sh1, _sh2], why=_sq + "<p>The zeros are at row 1 col 2, row 1 col 5, row 2 col 4, row 4 col 4 and row 5 col 1. Two of them sit in the <b>fourth column</b>.</p>"),
28: dict(ans="C", hints=[_sh1, _sh2], why=_sq + "<p>Every row has a repeated count (3 and 0 twice; 2 twice; 1 three times; 1 twice; 2 twice), so C holds. A fails in row 1, B fails in row 3 (no zero), and the 9 in row 2 is reached by only 4, so D fails.</p>"),
29: dict(ans="B", hints=[_th1, _th2], why=_tp + "<p>T2 stays (1,3) from month 3 to month 4: once. T4 changes every month: 0 times. Answer <b>(1, 0)</b>.</p>"),
30: dict(ans="A", hints=[_th1, _th2], why=_tp + "<p>Month 3: T1 has 0 SE and T5 has 2. Answer <b>(0, 2)</b>.</p>"),
31: dict(ans="B", hints=["How many projects does each employee work on, and how many points does each kind give per person?", "A challenging team has 5 people, a standard one has 4."], why=_pts + "<p><b>150</b> is not on the list.</p>"),
32: dict(ans="D", hints=["185 = 125 + 15k. How many challenging projects did Aneek work on?", "If Aneek missed T2's challenging month, where could Aneek be in month 2, and can Aneek reach T3 in month 3 from there?"], why=_pts + "<p>185 means 4 challenging projects: Aneek was in Ti in month i for four months. Option D skips T2 in month 2.</p><p>Aneek is in T1 in month 1. Not going to T2 means Aneek is in T1 or T5 in month 2. Between months 2 and 3, T1 and T5 only swap people with each other, and T3 only takes people from T2. So Aneek can't be in T3 in month 3. <b>D can't be true.</b></p>"),
}

# ---- DI ----
_rk = ("<p>Kids: NE 7500, W 12500, S 10000. All regions: G 16500, P 11100, O 2400.</p>"
 "<p>S: G = 60% = 6000. Kids of mothers who finished school are all in school, so S's O kids are just the 300 in the table. S's P = 10000 − 6000 − 300 = 3700.</p>"
 "<p>NE: the table's 300 O kids are half, so NE has 600 O kids. W's O = 2400 − 600 − 300 = 1500. G in NE = G in W = (16500 − 6000) ÷ 2 = 5250.</p>")
_rkh1 = "Start with the region sizes: 50 kids per village. Then work out S fully, using fact 1."
_rkh2 = "The table only counts kids whose mothers dropped out. Subtract it from the region totals to get the other group."
_rk2 = ("<p>Follow-up: out-of-school kids were NE 600, W 1500, S 300, and 1200 of the 2400 joined G. The only split that gives 1200 is NE 25% (150), W 50% (750), S 100% (300).</p>")
_rkh3 = "Try the three rates (25%, 100%, 50%) on NE 600, W 1500 and S 300 in every order. Which order gives 1200 joining G?"
_sh = ("<p>Score counts: S has three 3s, three 4s, two 5s, one 6, one 7. F has two 1s, one 2, two 3s, one 4, three 5s, one 7. C has one 1, three 2s, four 3s, one 4, one 6.</p>"
 "<p>Amda and Calla match and total 7. S can't be below 3, so both have S 3, and F + C = 4 with a value both can share: F 1, C 3.</p>"
 "<p>Zooma's 17 must include S 6: either (6, 7, 4) or (6, 5, 6). Each happy country holds exactly one of the top scores (S 7, F 7, C 6).</p>")
_shh1 = "Amda and Calla have identical scores, so each value they use must appear at least twice in the chart."
_shh2 = "A happy country holds one top score (S 7, F 7 or C 6) and none of the others. What's the most Zooma can make with each?"
H.update({
17: dict(ans="A", hints=[_rkh1, _rkh2], why=_rk + "<p>S's P share: 3700 ÷ 10000 = <b>37%</b>.</p>"),
18: dict(ans="A", hints=[_rkh1, "W's O kids = all O kids minus NE's and S's. Then remove the table's W figure."], why=_rk + "<p>W's O kids of mothers who finished school: 1500 − 1200 = <b>300</b>.</p>"),
19: dict(ans="A", hints=[_rkh2, _rkh3], why=_rk + _rk2 + "<p>G in W now: 5250 + 750 = <b>6000</b>.</p>"),
20: dict(ans="A", hints=[_rkh2, _rkh3], why=_rk + _rk2 + "<p>In S, all 300 O kids (all with mothers who dropped out) joined G. So that group's G = 5100 + 300 = 5400 of 5700 = <b>94.7%</b>.</p>"),
21: dict(ans="1", hints=[_shh1, "What's the lowest S anyone can have?"], why=_sh + "<p>Amda's F is <b>1</b>.</p>"),
22: dict(ans="6", hints=[_shh1, _shh2], why=_sh + "<p>With S 7, the best is 7 + 5 + 4 = 16, short of 17. Both ways to reach 17 use S 6. Zooma's S is <b>6</b>.</p>"),
23: dict(ans="B", hints=[_shh2, "Zooma takes the only S 6. Try both versions of Zooma and find the best equal score for the other two happy countries."], why=_sh + "<p>If Zooma is (6, 7, 4): the S 7 country gets at most 7 + 5 + 3 = 15. If Zooma is (6, 5, 6): the S 7 and F 7 countries each reach 16 only with C 4, and there's just one C 4, so a tie tops out at 15. Maximum <b>15</b>.</p>"),
24: dict(ans="B", hints=[_shh2, "The five non-happy countries share the leftover scores and must each stay at 13 or below. What's left after the five known countries?"], why=_sh + "<p>Either way Benga 16 and Delma 15 work out, the leftover scores are S 3, 4, 4, 4, 5; F 2, 3, 3, 4, 5; C 1, 2, 2, 2, 3. A 13 needs 5 + 5 + 3, and there's only one 5 in each list, so at most <b>1</b> country scores 13.</p>"),
})
