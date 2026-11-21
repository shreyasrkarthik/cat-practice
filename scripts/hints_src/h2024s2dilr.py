_wd = "Fill in every distance first. Columns are 150, 300 and 300 apart (P–O–N–M), rows are 400, 200 and 400 apart (M–L–E–D). The diagonals IG and OK are 250 and 500 (3-4-5 triangles)."
_walk = "<p>Distances: AB = 150, BC = CD = 300; each vertical walkway is 400 (top), 200 (middle) and 400 (bottom); IG = 250 and OK = 500.</p>"
_gym = ("<p>Player-4 is even and Player-1 is odd, so their shared coach is Xena. Player-2 (even) is Xena or Yuki. If it were Xena, Players 3 and 5 would both need Zara. So Player-2 is Yuki's, and Players 3 and 5 are Xena's and Zara's in some order.</p>"
 "<p>Ratings: seven different values plus the repeat for Players 5 and 7. With eight ratings averaging 4, the total is 32 = (1 + ... + 7) + 4. So Players 5 and 7 both have 4, and every value 1–7 is used once otherwise. Player-2 has 7. Player-4 < 4 and is double Player-8, so Player-4 = 2 and Player-8 = 1. Players 1, 3 and 6 share 3, 5 and 6.</p>"
 "<p>If Players 5 and 7 were Xena's, Zara would have only Player-3. So Zara has 5 and 7 (average 4), Yuki averages 6 and Xena 3. Yuki = Players 2 and 6, so Player-6 = 5. Xena = Players 1, 3, 4 and 8 (1 and 3 share 3 and 6 in either order; the average 12/4 = 3 checks).</p>")
_gh1 = "Players 1 and 4 share a coach, one odd and one even. Which coach can train both? Then who must train Player-2?"
_gh2 = "The eight ratings add up to 32, but seven different values use up 1 + ... + 7 = 28. What does that make the repeated rating?"
_grid = ("<p>The grid has 10 slots in a staircase. 10 must be the largest in its row and column, so it sits at the top of Column 4. 1 is the smallest in its row and column, so it sits at the bottom of Column 4 (it must share a row or column with 10).</p>"
 "<p>Working through the rest of the rules leaves only two grids. Row 1: 4, 6, 9, 10. Row 2: 2 or 3, then 5, 8. Row 3: 3 or 2, then 7. Row 4: 1. Only 2 and 3 can swap.</p>")
_grh1 = "Where can 10 go so that it's bigger than everything to its left and below it? Where can 1 go?"
_grh2 = "9 can't share a row or column with 7 or 8. Combined with 4 and 6 being in one row, that fixes Row 1."
H = {
1: dict(ans="A", hints=[_wd, "Find the shortest route between each pair: L to P, P to B, and B back to L. The diagonal OK helps get from L to P."],
 why=_walk + "<p>L → K → O → P = 300 + 500 + 150 = 950. P → I → G → B = 400 + 250 + 400 = 1050. B → G → F → K → L (or any other shortest route) = 1200.</p><p>Total = <b>3200 m</b>.</p>"),
2: dict(ans="A", hints=[_wd, "List only the walkways that run along a lake's edge. Can he walk every one of them exactly once and come back to C?"],
 why=_walk + "<p>The three lakes' edges add up to 1400 + 1000 + 1400 = 3800 m. Every point on these edges touches an even number of them (F and K touch four), so one loop from C covers them all once.</p><p>He walks <b>3800 m</b>.</p>"),
3: dict(ans="5100", hints=[_wd, "To make the loop long, go around the outside and dip into the inner points where you can. Use the diagonals only if they add length."],
 why=_walk + "<p>Best loop: A → B → G → F → C → D → E → L → M → N → K → J → O → P → I → H → A.</p><p>That's 150 + 400 + 300 + 400 + 300 + 400 + 200 + 400 + 300 + 400 + 300 + 400 + 150 + 400 + 200 + 400 = <b>5100 m</b>.</p>"),
4: dict(ans="3500", hints=[_wd, "Visitors can't touch A, H, M or L, which also rules out walkways AH and ML. Find the longest loop from C on what's left."],
 why=_walk + "<p>Best loop: C → B → G → J → I → P → O → N → K → F → E → D → C.</p><p>That's 300 + 400 + 200 + 150 + 400 + 150 + 300 + 400 + 200 + 300 + 400 + 300 = <b>3500 m</b>.</p>"),
5: dict(ans="C", hints=[_gh1, "Zara can only train odd players, and Player-1 is Xena's. Check whether Players 5 and 7 can be Xena's."],
 why=_gym + "<p>So Zara trains exactly <b>2</b> players.</p>"),
6: dict(ans="4", hints=[_gh1, _gh2], why=_gym + "<p>Player-7's rating is <b>4</b>.</p>"),
7: dict(ans="5", hints=[_gh2, "Yuki's average is 2 more than Zara's. Zara has Players 5 and 7. What must Player-6 score for Yuki's two players to average that?"],
 why=_gym + "<p>Player-6's rating is <b>5</b>.</p>"),
8: dict(ans="6", hints=[_gh2, "Find each rating you can. Which players are left sharing two values?"],
 why=_gym + "<p>Fixed: Players 2, 4, 5, 6, 7 and 8. Players 1 and 3 could be 3 and 6 either way. So <b>6</b> ratings are certain.</p>"),
9: dict(ans="C", hints=[_gh1, "Xena trains more players than Yuki. Use the averages to decide whether Players 6 and 8 belong to Xena or Yuki."],
 why=_gym + "<p>Xena trained <b>Players 1, 3, 4 and 8</b>.</p>"),
10: dict(ans="4", hints=[_grh1, "Row 4 has a single slot. What goes there?"], why=_grid + "<p>Row 4 holds just 1, so <b>Row 4</b> has the smallest sum.</p>"),
11: dict(ans="A", hints=[_grh1, "10 has to be at the end of a row and the top of a column at once."], why=_grid + "<p>10 is in Row 1 and 1 is in Row 4. <b>Both</b> are true.</p>"),
12: dict(ans="B", hints=[_grh1, _grh2], why=_grid + "<p>2 and 3 can swap between Column 2 and Column 3, so <b>neither</b> statement must be true.</p>"),
13: dict(ans="2", hints=[_grh1, _grh2], why=_grid + "<p>Only the two slots holding 2 and 3 are uncertain: <b>2</b>.</p>"),
14: dict(ans="26", hints=[_grh1, _grh2], why=_grid + "<p>Column 4 holds 10, 8, 7 and 1, which add up to <b>26</b>.</p>"),
}

# ---- DI ----
_rt = ("<p>Day 2 (from the chart): 5 ones, 10 twos, 5 threes, 20 fours, 10 fives. That's 50 buyers and a total of 170.</p>"
 "<p>Day 1 has n buyers averaging 3: (3n + 170) ÷ (n + 50) = 3.1, so n = 150.</p>"
 "<p>Day 3: ones = twos = x, threes = 2x, fours = fives = y with y bigger than 2x (4 and 5 are the modes). 4x + 2y = 100 with multiples of 10 gives x = 10, y = 30: 10, 10, 20, 30, 30. Total 360.</p>")
_rth1 = "Find Day 2's total and count from the chart, then use the cumulative averages 3 and 3.1."
_rth2 = "For Day 3, let ones = twos = x and fours = fives = y. The modes being 4 and 5 means y beats 2x."
_fm = ("<p>Reading the plots (ES, PAT): 2019: A (800, 3000), B (1000, 2800), C (600, 2400), D (600, 3900), E (1200, 2400), F (800, 2500). 2023: A (1300, 3900), B (1000, 3800), C (800, 3000), D (800, 2400), E (1400, 3500), F (1000, 3200).</p>"
 "<p>R&D spend = PAT × PRD, and PRD is shown by the circle's area.</p>")
_fmh1 = "Read each firm's ES (across) and PAT (up) from both plots."
H.update({
15: dict(ans="150", hints=[_rth1, "Set up (3n + 170) ÷ (n + 50) = 3.1."], why=_rt + "<p>Day 1 had <b>150</b> buyers.</p>"),
16: dict(ans="D", hints=[_rth2, "Only one value of x works with 4x + 2y = 100."], why=_rt + "<p>360 ÷ 100 = <b>3.6</b>.</p>"),
17: dict(ans="4", hints=[_rth2, "With 100 ratings, the median is the average of the 50th and 51st."], why=_rt + "<p>Counting up: 10, 20, 40, then 70 after the fours. The 50th and 51st are both 4, so the median is <b>4</b>.</p>"),
18: dict(ans="C", hints=[_rth1, _rth2], why=_rt + "<p>Day 3 cumulative: (450 + 170 + 360) ÷ 300 ≈ 3.27. From 3.1, that's up about 5.4%: <b>between 5% and 8%</b>.</p>"),
19: dict(ans="D", hints=[_fmh1, "With a constant growth rate, the firm whose PAT grew most from 2019 to 2023 has the highest rate."], why=_fm + "<p>2023 ÷ 2019 PAT: A 1.30, B 1.36, C 1.25, E 3500 ÷ 2400 ≈ 1.46. <b>Firm E</b> grew fastest.</p>"),
20: dict(ans="B", hints=[_fmh1, "Compare the widths of C's circles in the two years. Area grows with the square of the width."], why=_fm + "<p>C's 2019 circle is about 1.5 times as wide as its 2023 circle, so its PRD is about 2.25 times. R&D ratio = (2400 × 2.25) : (3000 × 1) = 1.8 : 1, about <b>9 : 5</b>.</p>"),
21: dict(ans="A", hints=[_fmh1, "Divide 2023 PAT by 2023 ES for each firm."], why=_fm + "<p>A 3900/1300 = 3.0, C 3000/800 = 3.75, E 3500/1400 = 2.5, F 3200/1000 = 3.2. <b>Firm C</b> is highest.</p>"),
22: dict(ans="A", hints=[_fmh1, "R&D per employee = (PAT ÷ ES) × PRD. C, D and F have circles of about the same size; E's is much bigger."], why=_fm + "<p>PAT per employee in 2023: C 3.75, D 3.0, F 3.2, E 2.5. C, D and F have similar circles, so D is lowest of those. E's circle is nearly twice the area, which lifts it well above 3.0. <b>Firm D</b> spends least per employee.</p>"),
})
