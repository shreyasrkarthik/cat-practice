H = {
1: dict(ans="A", hints=[
 "Selling at ₹264 with 10% profit means the 10 litres cost ₹240, so ₹24 a litre on average.",
 "If A makes up a fraction f of the mixture, the average cost is B + 8f. B gets bigger as f gets smaller. How small can f be?"],
 why="<p>B + 8f = 24, so B = 24 − 8f. B can't exceed A in the mix, so f ≥ ½.</p><p>At f = ½, B = 24 − 4 = <b>₹20</b>. 22 and 26 would need less than half the mix to be A.</p>"),
2: dict(ans="D", hints=[
 "The sector R has area (60/360) × π × 1<sup>2</sup> = π/6.",
 "OC = OD with a 60° angle between them makes OCD equilateral. Its area is (√3/4)OC<sup>2</sup>."],
 why="<p>(√3/4)OC<sup>2</sup> = π/12 gives OC<sup>2</sup> = π/(3√3).</p><p>OC = <b>(π/(3√3))<sup>1/2</sup></b>.</p>"),
3: dict(ans="54", hints=[
 "Let f(10) = k. Use the rule to write f(12), f(13), f(14) and f(15) in terms of k and 91.",
 "Each term is the sum of the two before it."],
 why="<p>f(12) = k + 91, f(13) = k + 182, f(14) = 2k + 273, f(15) = 3k + 455.</p><p>3k + 455 = 617 gives k = <b>54</b>.</p>"),
4: dict(ans="D", hints=[
 "Let Narayan take t hours. Partha takes t + 4.",
 "Partha reaches the midpoint in half his time, (t + 4)/2, and that's t − 2."],
 why="<p>(t + 4)/2 = t − 2 gives t = 8. Partha takes 12 hours.</p><p>Speed = 60/12 = <b>5 km/h</b>.</p>"),
5: dict(ans="60", hints=[
 "Let there be n tests with average a, so the total is na. The first 10 add up to 200, the last 10 to 300.",
 "Write (na − 200)/(n − 10) = a + 1 and (na − 300)/(n − 10) = a − 1."],
 why="<p>The first gives n − 10a = −190 and the second gives n + 10a = 310.</p><p>Add them: 2n = 120, so n = <b>60</b> (and a = 25).</p>"),
6: dict(ans="B", hints=[
 "The cost price of the mix is 40/1.1 for 3 : 2 and 40/1.05 for 2 : 3.",
 "So 3a + 2b = 5 × 40/1.1 and 2a + 3b = 5 × 40/1.05. Solve for a and b."],
 why="<p>3a + 2b = 2000/11 and 2a + 3b = 4000/21. Solving gives a = 7600/231 and b = 9600/231.</p><p>a : b = 76 : 96 = <b>19 : 24</b>.</p>"),
7: dict(ans="C", hints=[
 "Let peanuts cost the wholesaler p a kg, so walnuts cost 3p. Find what the shopkeeper paid in total.",
 "The shopkeeper sells the 16 kg left at ₹166 and gets 25% over what he paid."],
 why="<p>Shopkeeper paid 8 × 1.1p + 16 × 3.6p = 66.4p.</p><p>16 × 166 = 2656 = 1.25 × 66.4p = 83p, so p = 32.</p><p>Walnuts cost the wholesaler 3 × 32 = <b>₹96</b> a kg.</p>"),
8: dict(ans="C", hints=[
 "Let A take a days, so B takes 1.25a. A's half-job takes a/2 days.",
 "Fractions of the job: ½ + 4(1/a + 1/(1.25a)) + 0.05 = 1."],
 why="<p>4 × 1.8/a = 0.45 gives a = 16, so B takes 20 days.</p><p>Check the 13 days: A alone 8 days, together 4, B alone does 5% in 1 day. So B alone: <b>20 days</b>.</p>"),
9: dict(ans="A", hints=[
 "Each new triangle has half the side, so a quarter of the area.",
 "Area of T1 = (√3/4) × 24<sup>2</sup>. Then sum the geometric series."],
 why="<p>T1 = 144√3. Sum = 144√3 / (1 − ¼) = 144√3 × 4/3.</p><p>That's <b>192√3</b>.</p>"),
10: dict(ans="40", hints=[
 "Let the other two numbers be x and y. The product went up by (73 − 37)xy = 720.",
 "So xy = 20. What's the smallest x<sup>2</sup> + y<sup>2</sup> can be for a fixed xy?"],
 why="<p>x<sup>2</sup> + y<sup>2</sup> ≥ 2xy (since (x − y)<sup>2</sup> ≥ 0).</p><p>So the minimum is 2 × 20 = <b>40</b>, when x = y = √20.</p>"),
11: dict(ans="B", hints=[
 "Take log base 2 of both sides: x = log<sub>5</sub>2 × log<sub>2</sub>3.",
 "That product of logs simplifies to one log. Then see which option equals it."],
 why="<p>x = log<sub>5</sub>2 × log<sub>2</sub>3 = log<sub>5</sub>3.</p><p>log<sub>5</sub>3 = log<sub>5</sub>5 + log<sub>5</sub>(3/5) = <b>1 + log<sub>5</sub>(3/5)</b>.</p>"),
12: dict(ans="B", hints=[
 "p = log<sub>12</sub>81 = 4 log<sub>12</sub>3. Let t = log<sub>12</sub>3, so the fraction is (1 − t)/(1 + t).",
 "1 − t = log<sub>12</sub>4 and 1 + t = log<sub>12</sub>36."],
 why="<p>(1 − t)/(1 + t) = log 4 / log 36 = log<sub>36</sub>4 = log<sub>6</sub>2.</p><p>3 log<sub>6</sub>2 = <b>log<sub>6</sub>8</b>.</p>"),
13: dict(ans="198", hints=[
 "The cut leaves a small cone on top of height 12 − 9 = 3 ft. It's a scaled copy of the whole cone.",
 "Scale factor 1/4, so its radius is 1. Subtract its volume from the whole cone."],
 why="<p>Whole cone: ⅓ × π × 16 × 12 = 64π. Small cone: ⅓ × π × 1 × 3 = π.</p><p>Remaining: 63π = 63 × 22/7 = <b>198</b>.</p>"),
14: dict(ans="502", hints=[
 "Pick any set of digits. There's exactly one way to write them in ascending order.",
 "So count subsets of the 9 digits with at least 2 members."],
 why="<p>All subsets: 2<sup>9</sup> = 512. Remove the empty set and the 9 single digits.</p><p>512 − 1 − 9 = <b>502</b>.</p>"),
15: dict(ans="121000", hints=[
 "Let each instalment be x. After year 1 the loan is 1.1 × 210000, minus x.",
 "That balance grows 10% in year 2 and must equal x."],
 why="<p>(231000 − x) × 1.1 = x gives 254100 = 2.1x.</p><p>x = <b>₹1,21,000</b>.</p>"),
16: dict(ans="D", hints=[
 "Move −4v(u + v) to the left side. u<sup>2</sup> + 4uv + 4v<sup>2</sup> is a perfect square.",
 "Two squares add up to zero only if both are zero."],
 why="<p>(u + 2v)<sup>2</sup> + (u − 2v − 1)<sup>2</sup> = 0, so u = −2v and u − 2v = 1.</p><p>Then v = −¼ and u = ½. u + 3v = ½ − ¾ = <b>−¼</b>.</p>"),
17: dict(ans="12", hints=[
 "Let AP = d, so BP = 3d. Car 1 has speed 2s and car 2 has speed s.",
 "Car 1 takes d/(2s). Car 2 takes 3d/s. Compare the two times."],
 why="<p>Car 2's time is 6 times car 1's. The difference, 5 × car 1's time, is 60 minutes.</p><p>Car 1 takes <b>12 minutes</b>.</p>"),
18: dict(ans="D", hints=[
 "A rectangle in a circle has its diagonal as a diameter: 26 cm.",
 "Check which pair has length<sup>2</sup> + breadth<sup>2</sup> = 26<sup>2</sup> = 676."],
 why="<p>24<sup>2</sup> + 10<sup>2</sup> = 576 + 100 = 676.</p><p>So <b>24, 10</b>. The others miss: 25, 10 gives 725; 24, 12 gives 720; 25, 9 gives 706.</p>"),
19: dict(ans="B", hints=[
 "\"Short by 68%\" means 36 is 32% of the pass mark.",
 "Pass mark = 0.45N. So 36 = 0.32 × 0.45N."],
 why="<p>N = 36/0.144 = 250.</p><p>That fits <b>243 ≤ N ≤ 252</b>.</p>"),
20: dict(ans="D", hints=[
 "Write y = xr and z = xr<sup>2</sup>. In an AP, twice the middle term is the sum of the outer two.",
 "32xr = 5x + 12xr<sup>2</sup>. Solve for r, and remember x < y < z."],
 why="<p>12r<sup>2</sup> − 32r + 5 = 0 gives r = (32 ± 28)/24, so r = 5/2 or 1/6.</p><p>The GP is increasing, so r > 1: <b>5/2</b>. 1/6 is the trap root.</p>"),
21: dict(ans="5", hints=[
 "Only whole x make 2<sup>x</sup> + 2 a whole number to divide. 0.25 < 2<sup>x</sup> < 200 allows x = 0 to 7.",
 "Just list 2<sup>x</sup> + 2 for each: 3, 4, 6, 10, ..."],
 why="<p>Values: 3, 4, 6, 10, 18, 34, 66, 130. Divisible by 3 or 4: 3, 4, 6, 18, 66.</p><p>That's <b>5</b> values of x (0, 1, 2, 4, 6).</p>"),
22: dict(ans="52", hints=[
 "Nobody studies P alone. Split the rest into: only H, only E, H and E only (20), all three (10), H and P only, E and P only.",
 "The four unknown regions add up to 74 − 30 = 44. H = E means (only H + H and P only) = (only E + E and P only)."],
 why="<p>Each of those two sums is 22.</p><p>H = 22 + 20 + 10 = <b>52</b>.</p>"),
23: dict(ans="15", hints=[
 "At Z, T has done 3/5 of the route and S has done 2/5. T has run one hour longer than S.",
 "Let T run t hours to Z. Then 3/5 D = vt and 2/5 D = 0.75v(t − 1)."],
 why="<p>Divide: 3/2 = t/(0.75(t − 1)), so 1.125(t − 1) = t and t = 9 hours.</p><p>T covers 3/5 of the route in 9 hours, so the whole route takes <b>15 hours</b>.</p>"),
24: dict(ans="A", hints=[
 "Take the big square's side as 1. A square inside a square cuts each side into the same two pieces, say a and b, with a + b = 1.",
 "The inner square's area is a<sup>2</sup> + b<sup>2</sup> = 0.625."],
 why="<p>2ab = 1 − 0.625 = 0.375, so a and b are ¼ and ¾.</p><p>CG is the longer piece and EB the shorter, so EB : CG = <b>1 : 3</b>.</p>"),
25: dict(ans="D", hints=[
 "Divide the second equation by the first: y<sup>2</sup>/x<sup>2</sup> = 16.",
 "So y = ±4x. Put it back into the first equation to find x."],
 why="<p>With y = 4x: 4<sup>2017</sup>x<sup>4035</sup> = ½, so x = ½ and y = 2. (y = −4x gives x = −½, y = 2: the same answer.)</p><p>x<sup>2</sup> + y<sup>3</sup> = ¼ + 8 = <b>33/4</b>.</p>"),
26: dict(ans="D", hints=[
 "The total doesn't change. 4 + 9 = 13 parts before and 5 + 6 = 11 parts after, so use a total of 143.",
 "Before: 44 and 99. After: 65 and 78."],
 why="<p>Lalitha gave 99 − 78 = 21 marbles.</p><p>21/99 = <b>7/33</b> of what she had.</p>"),
27: dict(ans="B", hints=[
 "Undo the first log: 5 + log<sub>3</sub>a = 2<sup>3</sup> = 8.",
 "Then put a into the second: 4a + 12 + log<sub>2</sub>b = 5<sup>3</sup>."],
 why="<p>log<sub>3</sub>a = 3, so a = 27. Then 120 + log<sub>2</sub>b = 125, so b = 32.</p><p>a + b = <b>59</b>.</p>"),
28: dict(ans="B", hints=[
 "Let a human do h a day and a robot r. The work is 30(15h + 5r) = 60(5h + 15r).",
 "Solve for h in terms of r, then find the work in units of r."],
 why="<p>450h + 150r = 300h + 900r gives h = 5r. Work = 30 × 80r = 2400r.</p><p>Fifteen humans do 75r a day: 2400/75 = <b>32 days</b>.</p>"),
29: dict(ans="C", hints=[
 "Area = base × height. With base CD = 9, the height AP = 72/9.",
 "AP = 8 and AD = 16. Triangle APD has a right angle at P."],
 why="<p>PD = √(16<sup>2</sup> − 8<sup>2</sup>) = √192 = 8√3.</p><p>Area APD = ½ × 8 × 8√3 = <b>32√3</b>.</p>"),
30: dict(ans="A", hints=[
 "Half-chords are 2 and 3. If their distances from the centre are d<sub>1</sub> and d<sub>2</sub>: r<sup>2</sup> = 4 + d<sub>1</sub><sup>2</sup> = 9 + d<sub>2</sub><sup>2</sup>.",
 "Same side of the centre means d<sub>1</sub> − d<sub>2</sub> = 1."],
 why="<p>d<sub>1</sub><sup>2</sup> − d<sub>2</sub><sup>2</sup> = 5 and d<sub>1</sub> − d<sub>2</sub> = 1, so d<sub>1</sub> + d<sub>2</sub> = 5. That gives d<sub>1</sub> = 3 and d<sub>2</sub> = 2.</p><p>r<sup>2</sup> = 4 + 9 = 13, so r = <b>√13</b>.</p>"),
31: dict(ans="10", hints=[
 "Let a filling pipe add f per hour and a draining pipe remove d. Then 6(6f − 5d) = 1 and 60(5f − 6d) = 1.",
 "So 6f − 5d = 10(5f − 6d). That gives d in terms of f."],
 why="<p>55d = 44f, so d = 0.8f. Then 6f − 4f = 2f = 1/6, so f = 1/12.</p><p>Two filling and one draining: 2f − 0.8f = 1.2f = 1/10 per hour. That's <b>10 hours</b>.</p>"),
32: dict(ans="D", hints=[
 "Only burger = 134 − (both). Find the smallest and largest possible overlap.",
 "Overlap is at most 105 (everyone who likes pizza). It's at least 105 + 134 − 200."],
 why="<p>Overlap runs from 39 to 105, so only burger runs from 29 to 95.</p><p>The only option in that range is <b>93</b>. 96 is just over the top.</p>"),
33: dict(ans="32", hints=[
 "2x<sup>2</sup> grows with x while 52 − 5x falls. Their minimum is largest where they meet.",
 "Solve 2x<sup>2</sup> = 52 − 5x for positive x."],
 why="<p>2x<sup>2</sup> + 5x − 52 = 0 gives x = 4.</p><p>f(4) = 2 × 16 = <b>32</b>.</p>"),
34: dict(ans="D", hints=[
 "Total age = 38 × (30 + m), where m ≤ 39 is the number under 51.",
 "To make the young group's average high, make the older 30 as young as allowed (all exactly 51) and try the largest m."],
 why="<p>Young total ≤ 38(30 + m) − 30 × 51 = 38m − 390, so their average ≤ 38 − 390/m.</p><p>That grows with m. At m = 39 it's 38 − 10 = <b>28</b>.</p>"),
}
