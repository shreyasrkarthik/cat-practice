H = {
1: dict(ans="20", hints=[
 "Let Barun be 5k and Arun 2k (40%). After t years, 2k + t = (5k + t)/2.",
 "Solve for t in terms of k, then compare t with Barun's present age."],
 why="<p>4k + 2t = 5k + t gives t = k.</p><p>Barun goes from 5k to 6k, an increase of <b>20%</b>.</p>"),
2: dict(ans="15", hints=[
 "Call one person's daily work 1 unit. The job is 120 units.",
 "On day n there are n people. Work done after n days is 1 + 2 + ... + n."],
 why="<p>n(n + 1)/2 = 120 gives n = 15 exactly (15 × 16/2 = 120).</p><p>So <b>15 days</b>.</p>"),
3: dict(ans="11", hints=[
 "The group has at least one 57 kg person and one 53 kg person. Everyone else weighs at least 53 kg.",
 "To fit the most people, make everyone else 53 kg. 57 + 53(n − 1) ≤ 630."],
 why="<p>53(n − 1) ≤ 573 gives n − 1 ≤ 10.8, so n ≤ 11.</p><p>Check: 57 + 10 × 53 = 587 ≤ 630, while 12 people need at least 640. Answer <b>11</b>.</p>"),
4: dict(ans="20", hints=[
 "Between the two speeds, the walking time changes by 10 + 10 = 20 minutes.",
 "d/12 − d/15 = 1/3 hour."],
 why="<p>d/60 = 1/3, so d = <b>20 km</b>.</p>"),
5: dict(ans="70000", hints=[
 "Let savings be S. Fixed deposits get 0.5S. Stocks get 30% of the other half.",
 "Savings bank gets what's left of that half. Add fixed deposits and savings bank."],
 why="<p>Stocks: 0.15S. Savings bank: 0.35S. Bank total: 0.5S + 0.35S = 0.85S = 59500.</p><p>S = <b>₹70000</b>.</p>"),
6: dict(ans="D", hints=[
 "Take cost price as 100. A 15% discount still leaves her 102.",
 "So 0.85 × retail = 102. Find the retail price, then compare with 120."],
 why="<p>Retail = 102/0.85 = 120.</p><p>A 20% profit means selling at 120, which is just the retail price: <b>sell at retail price</b>.</p>"),
7: dict(ans="B", hints=[
 "Let the boat's speed be b and the river's r. Total time is d/(b + r) + d/(b − r) = 2db/(b<sup>2</sup> − r<sup>2</sup>).",
 "With speed 2b the time is 4db/(4b<sup>2</sup> − r<sup>2</sup>), which equals one quarter of the old time."],
 why="<p>4b/(4b<sup>2</sup> − r<sup>2</sup>) = 2b/(4(b<sup>2</sup> − r<sup>2</sup>)) gives 16b<sup>2</sup> − 16r<sup>2</sup> = 8b<sup>2</sup> − 2r<sup>2</sup>, so 8b<sup>2</sup> = 14r<sup>2</sup>.</p><p>b<sup>2</sup>/r<sup>2</sup> = 7/4, so b : r = <b>√7 : 2</b>.</p>"),
8: dict(ans="A", hints=[
 "C2 sits in both ratios. Scale them so C2 has the same number: 10 and 18 both go into 90.",
 "Then C5 − C1 in those units equals 19 crore."],
 why="<p>C1 : C2 : C3 = 81 : 90 : 72 and C2 : C4 : C5 = 90 : 95 : 100.</p><p>C5 − C1 = 19 units = 19 crore, so 1 unit = 1 crore.</p><p>Total = 81 + 90 + 72 + 95 + 100 = <b>438 crore</b>.</p>"),
9: dict(ans="D", hints=[
 "Take 100 boys and 200 girls.",
 "Count who gets in, then who doesn't."],
 why="<p>Admitted: 45 boys + 60 girls = 105 of 300, which is 35%.</p><p>Not admitted: <b>65%</b>. 35 is the trap: that's the admitted share.</p>"),
10: dict(ans="A", hints=[
 "Popcorn total is 40 parts and chips 35 parts. Those totals are equal.",
 "So one popcorn part : one chips part = 35 : 40 = 7 : 8. Now compare jumbo: 16 popcorn parts vs 14 chips parts."],
 why="<p>Jumbo popcorn : jumbo chips = 16 × 7 : 14 × 8 = 112 : 112.</p><p>That's <b>1 : 1</b>.</p>"),
11: dict(ans="B", hints=[
 "Say good mangoes cost 2 a kg and medium ones 1 a kg.",
 "He sells all 120 kg at 10% below 2, so at 1.8 a kg."],
 why="<p>Cost: 80 × 2 + 40 × 1 = 200. Sales: 120 × 1.8 = 216.</p><p>Profit = 16/200 = <b>8%</b>.</p>"),
12: dict(ans="D", hints=[
 "Let each toy cost c. Selling 60 toys at 0.6P each gives 1.2 × 60c, so P = 2c.",
 "She wants the same total profit (12c), so the 50 remaining toys must bring in 72c."],
 why="<p>Each of the 50 must sell for 72c/50 = 1.44c = 0.72P.</p><p>That's a discount of <b>28%</b>.</p>"),
13: dict(ans="D", hints=[
 "Take square roots: a + 3 = ±3b and a − 1 = ±2(b − 1). That's four sign cases.",
 "Keep only the case where a and b are integers with opposite signs."],
 why="<p>a + 3 = −3b with a − 1 = 2(b − 1) gives b = −2/5, no. a + 3 = −3b with a − 1 = −2(b − 1) gives b = −6 and a = 15. (The other cases give a fraction, or a = 3, b = 2 with the same sign.)</p><p>a<sup>2</sup> : b<sup>2</sup> = 225 : 36 = <b>25 : 4</b>.</p>"),
14: dict(ans="A", hints=[
 "Let the boys' mid-sem average be m, so the girls' is m + 5 and the class average is m + 3.",
 "Final: girls m + 2, boys m + x, and the class m + 5. Write the class average as a weighted mean."],
 why="<p>(20(m + x) + 30(m + 2))/50 = m + 0.4x + 1.2 = m + 5.</p><p>0.4x = 3.8, so x = <b>9.5</b>.</p>"),
15: dict(ans="C", hints=[
 "|x| + |y| = 2 is a square tilted on its corner, through (2, 0), (0, 2), (−2, 0) and (0, −2).",
 "Its diagonals are both 4. Area of a rhombus = ½ × d<sub>1</sub> × d<sub>2</sub>."],
 why="<p>Area = ½ × 4 × 4 = <b>8</b>. 4π and 2π are circles, which this isn't.</p>"),
16: dict(ans="B", hints=[
 "Find the triangle's area with Heron's formula: s = 50.",
 "The centroid splits a triangle into three equal parts, so GBC is one third of it."],
 why="<p>Area = √(50 × 10 × 25 × 15) = √187500 = 250√3.</p><p>What's left is two thirds: 500√3/3 = <b>500/√3</b>.</p>"),
17: dict(ans="B", hints=[
 "BC = 6√2, so the semicircle on BC has area ½π(3√2)<sup>2</sup> = 9π.",
 "The arc BPC is part of a circle of radius 6 around A, with a 90° angle. The area between it and BC is a quarter-circle minus triangle ABC."],
 why="<p>Area between arc BPC and BC: 9π − 18.</p><p>Area between the two arcs: 9π − (9π − 18) = <b>18</b>.</p>"),
18: dict(ans="B", hints=[
 "The volumes add to 64, so the original cube had side 4. The small cubes have sides 1, 1, 2, 3, 3.",
 "Surface area is 6 × side<sup>2</sup>. Compare the totals."],
 why="<p>Original: 6 × 16 = 96. New: 6 × (1 + 1 + 4 + 9 + 9) = 144.</p><p>144 is 50% more than 96, so <b>50</b>.</p>"),
19: dict(ans="6", hints=[
 "πr<sup>2</sup> × 3 = 9π gives the cylinder's radius: √3. The ball (radius 2) sits in that round opening.",
 "Picture a right triangle: ball's centre, the rim, and the centre of the opening. How high is the ball's centre above the rim?"],
 why="<p>Centre above rim = √(2<sup>2</sup> − (√3)<sup>2</sup>) = 1 cm.</p><p>Top of the ball = 3 (cylinder) + 1 + 2 (radius) = <b>6 cm</b>.</p>"),
20: dict(ans="24", hints=[
 "The quickest way to a line is straight at it, along the perpendicular.",
 "Height to the hypotenuse = (AB × AC)/BC, and BC = 25."],
 why="<p>Height = 15 × 20 / 25 = 12 km.</p><p>12 km at 30 km/h takes <b>24 minutes</b>.</p>"),
21: dict(ans="D", hints=[
 "x = 3<sup>a</sup> and y = 12<sup>a</sup>.",
 "G = √(xy). What is 3 × 12?"],
 why="<p>xy = 36<sup>a</sup>, so G = 6<sup>a</sup>.</p><p>log<sub>6</sub>G = <b>a</b>.</p>"),
22: dict(ans="D", hints=[
 "Use x<sup>2</sup> = x + 1 to lower the powers: x<sup>4</sup> = (x + 1)<sup>2</sup>.",
 "You'll get x<sup>4</sup> = 3x + 2. Then x = (1 + √5)/2."],
 why="<p>x<sup>4</sup> = x<sup>2</sup> + 2x + 1 = 3x + 2. 2x<sup>4</sup> = 6x + 4 = 3(1 + √5) + 4.</p><p>That's <b>7 + 3√5</b>.</p>"),
23: dict(ans="C", hints=[
 "0.008 = 1/125 = 5<sup>−3</sup>, and √5 = 5<sup>1/2</sup>.",
 "√3 = 3<sup>1/2</sup> and 81 = 3<sup>4</sup>. Divide the powers."],
 why="<p>log<sub>0.008</sub>√5 = (1/2)/(−3) = −1/6. log<sub>√3</sub>81 = 4/(1/2) = 8.</p><p>−1/6 + 8 − 7 = <b>5/6</b>.</p>"),
24: dict(ans="B", hints=[
 "Write both as powers of 3: 9<sup>2x−1</sup> = 3<sup>4x−2</sup> and 81<sup>x−1</sup> = 3<sup>4x−4</sup>.",
 "Let u = 3<sup>4x−4</sup>. Then the first is 9u."],
 why="<p>9u − u = 8u = 1944, so u = 243 = 3<sup>5</sup>.</p><p>4x − 4 = 5 gives x = <b>9/4</b>.</p>"),
25: dict(ans="B", hints=[
 "x = 25 + y + z, and x ≤ 40 means y + z ≤ 15.",
 "Count pairs (y, z) of positive integers with y + z ≤ 15, then remove those where y or z is above 12."],
 why="<p>Pairs with y + z ≤ 15: 1 + 2 + ... + 14 = 105.</p><p>Too big: y = 13 (z = 1, 2), y = 14 (z = 1), and the same for z. That's 6.</p><p>105 − 6 = <b>99</b>.</p>"),
26: dict(ans="11", hints=[
 "Expand and simplify to a quadratic in n.",
 "You get n<sup>2</sup> − 18n + 56 ≤ 0. Factor it."],
 why="<p>(n − 4)(n − 14) ≤ 0 means 4 ≤ n ≤ 14.</p><p>That's <b>11</b> integers.</p>"),
27: dict(ans="24", hints=[
 "f<sub>1</sub>(x) = x becomes x<sup>2</sup> + 10x + n = 0.",
 "Two distinct real roots need the discriminant > 0."],
 why="<p>100 − 4n > 0 gives n < 25.</p><p>Largest whole n = <b>24</b>.</p>"),
28: dict(ans="2", hints=[
 "The sum would be 0 only if all four were 7.5, which isn't an integer.",
 "Try a, b, c, d as close to 7.5 as possible, like a mix of 7s and 8s. Can the sum be 1?"],
 why="<p>A sum of 1 needs a = b = c and d = a ± 1, so 4a ± 1 = 30, which has no integer answer.</p><p>a = 8, b = c = 7, d = 8 gives 1 + 1 + 0 = <b>2</b>.</p>"),
29: dict(ans="160", hints=[
 "Start with all ways to choose 3 of the 11 points.",
 "Three points fail to make a triangle only when they're on one line. Which sets of three are on one line?"],
 why="<p>C(11, 3) = 165. Each diameter's two ends plus O are on a line: 5 such sets. No three points on the circle are on a line.</p><p>165 − 5 = <b>160</b>.</p>"),
30: dict(ans="A", hints=[
 "Draw y = |x − 1| + |x + 1|. Between x = −1 and 1, it's flat at y = 2.",
 "The point (½, 1) sits right under that flat part."],
 why="<p>The nearest point on the curve is (½, 2), straight above it. The corners (±1, 2) are farther away.</p><p>Distance = <b>1</b>. 0 is the trap: the line y = 2x passes through (½, 1), but the curve only follows it for x ≥ 1.</p>"),
31: dict(ans="A", hints=[
 "Write the terms as a + 6d, a + 2d and a + 16d.",
 "(a + 6d)<sup>2</sup> = (a + 2d)(a + 16d). Expand and cancel."],
 why="<p>a<sup>2</sup> + 12ad + 36d<sup>2</sup> = a<sup>2</sup> + 18ad + 32d<sup>2</sup> gives 4d<sup>2</sup> = 6ad.</p><p>a/d = <b>2 : 3</b>.</p>"),
32: dict(ans="A", hints=[
 "Give everyone 1 eraser first. Now share the 3 left over, with nobody getting more than 2 extra.",
 "Count all ways to share 3 among 4 kids, then remove the ways where one kid gets all 3."],
 why="<p>Ways to share 3 among 4: C(6, 3) = 20. One kid gets all 3: 4 ways.</p><p>20 − 4 = <b>16</b>.</p>"),
33: dict(ans="A", hints=[
 "Work out f(3) first, then put that into f again.",
 "f(3) = 17/4. f(17/4) comes out neat."],
 why="<p>f(17/4) = (85/4 + 2)/(51/4 − 5) = (93/4)/(31/4) = 3. So f(f(3)) = 3.</p><p>g(3) = 9 − 6 − 1 = <b>2</b>.</p>"),
34: dict(ans="B", hints=[
 "The AP is 3, 7, 11, ... The sum of 3n terms is 3n(6n + 1).",
 "Set that to 1830 to find n. Then sum the first n terms."],
 why="<p>n(6n + 1) = 610 gives n = 10. First 10 terms: 5 × (3 + 39) = 210.</p><p>m × 210 > 1830 needs m > 8.7, so m = <b>9</b>.</p>"),
}
