_gh1 = "There's exactly 1 item of type a, and each next type has at least double the one before. The counts add up to 100."
_ss = ("<p>4 savouries (D, E, F, and K at 16) must come last: D, E, F in 13–15 and shelf 12 empty. Shelves 1–11 hold 5 biscuits, 3 candies and 3 empties.</p>"
 "<p>C (candy) has two empties right before it, so it starts the candy group. L has exactly one empty before it, so it starts a group too, and that group must be the biscuits. Two layouts work: empty 1, 2 / candies 3–5 / empty 6 / biscuits 7–11, or empty 1 / biscuits 2–6 / empty 7, 8 / candies 9–11.</p>"
 "<p>L and J are biscuits, so I is too (I and J are side by side), and A, B (side by side, before I and J) are biscuits. That makes G and H candies with C. Biscuits run L, A, B, then I and J in either order; candies run C, then G and H in either order.</p>")
_sh1 = "Where must the savouries go, given K is on shelf 16? That fixes shelves 12–16."
_sh2 = "C needs two empty shelves right before it and L needs exactly one. Which groups do they start?"
_dn = ("<p>Each composer assigns exactly 2 items, since Princess and Queen use four different composers between them, and so do Rani and Samragni. The order of dancers is P, ?, ?, R and then again P, ?, ?, R.</p>"
 "<p>Badal is at 1 and Gagan at 8. With the same gap for Badal, Gagan and Dyu, and Ashman's two side by side, the only order that fits every rule is: Badal, Dyu, Gagan, Ashman, Ashman, Badal, Dyu, Gagan. The dancers are Princess, Samragni, Queen, Rani, then the same again.</p>")
_dh1 = "Princess and Queen share no composer, and Rani and Samragni share none. How many items must each composer have assigned?"
_dh2 = "Badal is at 1 and Gagan at 8, with the same gap for Badal, Gagan and Dyu. Ashman's two are next to each other. Try gap sizes."
_st = ("<p>The only triangles formed by street segments are b-c-g and b-f-g, so X, U and Z are on those corners. X sees only U and Z, which rules out c and g for X (each sees too many). So X is at b.</p>"
 "<p>U sees V right behind Z, and W can see neither V nor Z. Testing the remaining spots leaves one arrangement: U at g, Z at f, V at e, X at b, Y at k, W at l.</p>")
_sth1 = "Find the triangles made by three street segments. There are only two, and they share the diagonal b–g."
_sth2 = "X must see only U and Z. Which corner of the triangle lets X see the other two but nobody else?"
_ar = ("<p>Read the bonus rounds: Tanzi and Yonita had 1 bull's eye, Umeza and Zeneca 2, Xyla 3, Wangdu 0. That's 9 bull's eyes, and Round 2 = 2 × Round 3. Xyla scored 5 in Round 1, so Round 3 has 2, Round 2 has 4 and Round 1 has 3.</p>"
 "<p>Round 2's four are Umeza, Xyla, Yonita and Zeneca. Tanzi and Zeneca match in Round 1, so both got 5 there; Round 3's two are Xyla and Umeza.</p>"
 "<p>Totals: Tanzi 14 + r3, Umeza 13 + r1, Yonita 13 + r1, which must be equal. All three can't be off a multiple of 3, so they're all 15: Tanzi's Round 3 = 1. Then Wangdu is lowest (at most 12) and the top is 2 × 12 + 1 = 25: Xyla 25, Zeneca 24, Wangdu 12.</p>")
_arh1 = "From the bonus rounds, count each player's bull's eyes in Rounds 1–3. Then use Round 2 = 2 × Round 3."
_arh2 = "Tanzi, Umeza and Yonita have equal totals, and only one total is not a multiple of 3. So those three must be multiples of 3."
_lt = ("<p>The sum has an extra digit, so A = 1. Units: F + F ends in F, so F = 0. Hundreds: 1 + 0 + carry 1 = 2 = C (the tens G + K must be 11 to end in 1). Ten-thousands: H + H ends in 0, so H = 5 with a carry. Then B + 1 + 1 = 11, so B = 9.</p>"
 "<p>Thousands: 1 + J = G. With G + K = 11 and the digits left being 3, 4, 6, 7, 8, the options are J, G, K = 3, 4, 7 or 6, 7, 4 or 7, 8, 3. D and E take the two digits left over.</p>")
_lh1 = "A six-digit plus a six-digit number gives a seven-digit number. What must the first digit be? Then look at the units column."
H = {
1: dict(ans="2", hints=[_gh1, "Can you do it with just two types?"], why="<p>1 type a and 99 type b works, since 99 is at least double 1. So the minimum is <b>2</b>.</p>"),
2: dict(ans="6", hints=[_gh1, "Use the smallest counts possible: 1, 2, 4, 8, ... When does the total pass 100?"], why="<p>1 + 2 + 4 + 8 + 16 + 32 = 63. A seventh type would need at least 64, too many. Six types work, for example 1, 2, 4, 8, 16, 69. Maximum: <b>6</b>.</p>"),
3: dict(ans="D", hints=[_gh1, "For each option, ask whether there's room for the types before it (each at most half the next) and the ones after it (each at least double)."],
 why="<p>With 45 of type c, type d would need 90 or more, so c must be the last type. Then 1 + b + 45 = 100 makes b = 54, but b can be at most 22. So <b>45 of type c</b> is impossible.</p><p>The others work: 1, 30, 69; 1, 2, 4, 18, 75; 1, 9, 30, 60.</p>"),
4: dict(ans="A", hints=[_gh1, "Box 45's type has 31 + 1 + 43 = 75 items. Could any type come after it? How many types fit in the other 25?"],
 why="<p>No type can follow 75 (it would need 150). The other 25 items need doubling counts each at most half the next: 1, 2, 4, 18 fits, but five types need at least 1 + 2 + 4 + 8 + 16 = 31. So at most 4 + 1 = <b>5</b> types.</p>"),
5: dict(ans="C", hints=[_sth1, _sth2], why=_st + "<p>Nobody is at a: <b>no one</b>.</p>"),
6: dict(ans="B", hints=[_sth1, _sth2], why=_st + "<p>V at e sees along column e (Z at f, U at g) and row a-e-i (nobody). So <b>U and Z only</b>.</p>"),
7: dict(ans="B", hints=[_sth1, "Once you've placed X and Y, find the shortest way along the streets from one to the other."], why=_st + "<p>X at b goes along the diagonal to g, then along the row to k: <b>2</b> segments.</p>"),
8: dict(ans="D", hints=[_sth1, "From d you can see along column a-b-c-d and row d-h-l."], why=_st + "<p>From d: X at b (column) and W at l (row). So <b>W and X only</b>.</p>"),
17: dict(ans="D", hints=[_sh1, _sh2], why=_ss + "<p>2 layouts × 2 orders of I, J × 2 orders of G, H = <b>8</b> ways.</p>"),
18: dict(ans="D", hints=[_sh1, "L and J are biscuits, and items side by side share a type. Which items does that pull in with them?"], why=_ss + "<p><b>G</b> is a candy, not a biscuit.</p>"),
19: dict(ans="C", hints=[_sh1, _sh2], why=_ss + "<p>Empty shelves are 1, 2, 6, 12 or 1, 7, 8, 12. Only <b>1, 2, 6, 12</b> is offered.</p>"),
20: dict(ans="D", hints=[_sh1, "Find B and C in both layouts."], why=_ss + "<p>Layout 1: C at 3, B at 9 (5 shelves between). Layout 2: B at 4, C at 9 (4 shelves between). The others depend on the layout, so the answer is <b>at least four shelves between B and C</b>.</p>"),
21: dict(ans="C", hints=[_arh1, _arh2], why=_ar + "<p>Highest total: <b>25</b>.</p>"),
22: dict(ans="D", hints=[_arh1, _arh2], why=_ar + "<p>Zeneca: 5 + 5 + 4 + 5 + 5 = <b>24</b> (her Round 3 can't be 1, which is Tanzi's).</p>"),
23: dict(ans="C", hints=[_arh1, _arh2], why=_ar + "<p><b>Xyla</b> was the highest scorer, with 25.</p>"),
24: dict(ans="A", hints=[_arh1, _arh2], why=_ar + "<p>Tanzi's Round 3 score was <b>1</b>.</p>"),
25: dict(ans="1", hints=[_lh1, "The carry into a new leftmost column can only be 1."], why=_lt + "<p>A = <b>1</b>.</p>"),
26: dict(ans="9", hints=[_lh1, "Work right to left: F, then C, then H. The leftmost column then fixes B."], why=_lt + "<p>B = <b>9</b>.</p>"),
27: dict(ans="7", hints=[_lh1, "List the three options for J, G and K. D gets one of the two digits left over each time."], why=_lt + "<p>D can be 6, 8, 3 or 4, but never <b>7</b>.</p>"),
28: dict(ans="6", hints=[_lh1, "G = J + 1 and G + K = 11, with 3, 4, 6, 7, 8 left."], why=_lt + "<p>G can be 4, 7 or 8, but never <b>6</b>.</p>"),
29: dict(ans="B", hints=[_dh1, _dh2], why=_dn + "<p>The 2nd performance was <b>Dyu's</b>.</p>"),
30: dict(ans="A", hints=[_dh1, _dh2], why=_dn + "<p>Queen performed items 3 (Gagan) and 7 (Dyu), so \"Queen did not perform any Gagan item\" is <b>false</b>.</p>"),
31: dict(ans="C", hints=[_dh1, _dh2], why=_dn + "<p>The 6th performance was <b>Badal's</b>.</p>"),
32: dict(ans="C", hints=[_dh1, _dh2], why=_dn + "<p>The <b>first and sixth</b> are both Badal's.</p>"),
}

# ---- DI ----
_cr = ("<p>Reading the bars (IPC, SLL, Other): Delhi 64, 35, 44. Karnataka 16, 49, 26. Goa 27, 34, 19. Tamil Nadu 2, 25, 36. Maharashtra 16, 34, 6. Haryana 3, 28, 7. Kerala 8, 15, 11. Puducherry about 0, 1, 30. Telangana 4, 15, 6. West Bengal 0, 520, 0.</p>"
 "<p>The ranks given in the table match these readings (e.g. SLL: West Bengal 1, Karnataka 2, Goa and Maharashtra tied 4). Any state outside the top ten has a total below Telangana's 25.</p>")
_crh1 = "Read the three parts of each bar. Then check them against the ranks the table does give."
_crh2 = "A state outside the top ten has fewer than 25 cases in total. Could it beat any of the numbers you need?"
_vd = ("<p>Approximate scores from the chart (Reliability, Reach, Quality, Features, Customer Service, Cost): V1 52, 85, 70, 40, about 52, 75. V2 40, 65, 70, 45, 40, 80. V3 75, 70, 60, 55, about 48, 90. V4 30, 40, 40, 90, 70, 70. V5 60, 75, 50, 70, 40, 50.</p>")
_vdh1 = "Read each vendor's six scores off the chart, using the given ones (V1 Reliability 52, V2 Features 45, V3 Cost 90) to calibrate."
H.update({
9: dict(ans="5", hints=[_crh1, _crh2], why=_cr + "<p>IPC: Delhi 64, Goa 27, Karnataka and Maharashtra 16 are above Kerala's 8. Telangana (4) is ranked 6, so only five states beat 4, and Kerala is one of them. Kerala's rank is <b>5</b>.</p>"),
10: dict(ans="C", hints=[_crh1, "West Bengal's 520 cases are all SLL. Is it in the top two?"], why=_cr + "<p>The top two by total are West Bengal (520) and Delhi (143). IPC: 0 + 64 = 64. SLL: 520 + 35 = 555. 64 : 555 is about <b>1 : 9</b>.</p>"),
11: dict(ans="B", hints=[_crh1, _crh2], why=_cr + "<p>Other crimes: Delhi 44, Tamil Nadu 36, Puducherry about 30, then Karnataka 26. No state outside the list can reach 30. So Tamil Nadu is 2 and Puducherry 3: <b>both are true</b>.</p>"),
12: dict(ans="5", hints=[_crh1, _crh2], why=_cr + "<p>Delhi: IPC 1 (64 is the most), SLL 3 (behind West Bengal and Karnataka), Other 1 (44 is the most). Sum = <b>5</b>.</p>"),
13: dict(ans="D", hints=[_vdh1, "For each option, sort the five scores and take the middle one."], why=_vd + "<p>Medians: Cost 75, Quality 60, Reliability 52, Customer Service about 48. <b>Customer Service</b> is least.</p>"),
14: dict(ans="B", hints=[_vdh1, "Add each vendor's six scores. The highest total has the highest average."], why=_vd + "<p>Totals: V3 about 398, V1 about 374, V2 340, V4 340, V5 345. <b>Vendor 3</b> leads.</p>"),
15: dict(ans="D", hints=[_vdh1, "For each aspect, mark the top two vendors, then count the marks."], why=_vd + "<p>Top two: Reliability V3, V5. Reach V1, V5. Quality V1, V2. Features V4, V5. Customer Service V4, V1. Cost V3, V2. V1 and V5 are top two 3 times each, more than anyone else: <b>Vendor 1 and Vendor 5</b>.</p>"),
16: dict(ans="D", hints=[_vdh1, "Knock out any vendor that's 4th or 5th on even one aspect."], why=_vd + "<p>V1 is 5th on Features, V2 is 4th on Reliability, V4 is last on Reliability, V5 is last on Cost. V3 is in the top three everywhere (it's 3rd on Reach, Quality, Features and Customer Service). <b>Only Vendor 3</b>.</p>"),
})
