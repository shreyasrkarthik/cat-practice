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
