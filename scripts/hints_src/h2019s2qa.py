H = {
1: dict(ans="A", hints=[
 "Let t = 2<sup>3x</sup>. Then 2<sup>6x</sup> = t<sup>2</sup> and 2<sup>3x+2</sup> = 4t.",
 "Solve t<sup>2</sup> + 4t − 21 = 0, keep the positive root, then undo t = 2<sup>3x</sup>."],
 why="<p>(t + 7)(t − 3) = 0, and t must be positive, so t = 3.</p><p>2<sup>3x</sup> = 3 gives 3x = log<sub>2</sub>3, so x = <b>(log<sub>2</sub>3)/3</b>.</p>"),
2: dict(ans="C", hints=[
 "The 30 numbers add up to 150. The other 10 numbers are all more than 5, so each is at least 6.",
 "To make the 20 as big as possible, make the other 10 as small as possible."],
 why="<p>The 10 bigger numbers add up to at least 60. So the 20 add up to at most 90.</p><p>Average of the 20 ≤ 90/20 = <b>4.5</b> (for example, ten 4s and ten 5s). 5 is the trap: the 20 can't all be 5 when the others must be 6 or more.</p>"),
3: dict(ans="A", hints=[
 "There's an identity: (a<sup>2</sup> + b<sup>2</sup>)(x<sup>2</sup> + y<sup>2</sup>) = (ax + by)<sup>2</sup> + (ay − bx)<sup>2</sup>.",
 "Put in 25, 169 and 65."],
 why="<p>25 × 169 = 4225 = 65<sup>2</sup> + k<sup>2</sup>, and 65<sup>2</sup> = 4225.</p><p>So k<sup>2</sup> = 0 and <b>k = 0</b>.</p>"),
4: dict(ans="C", hints=[
 "The centroid G splits each median 2 : 1 from the vertex. So AG = 8 and BG = 6.",
 "Triangle ABG has a right angle at G. How does its area compare with the whole triangle's?"],
 why="<p>Area ABG = ½ × 8 × 6 = 24.</p><p>The centroid splits a triangle into three equal areas (ABG, BCG, CAG), so ABC = 3 × 24 = <b>72</b>.</p>"),
5: dict(ans="B", hints=[
 "Put in n = 1, 2, 3, ... and solve for each new term in turn.",
 "You'll find odd terms are 1 and even terms are −1."],
 why="<p>a<sub>1</sub> = 1; 1 − a<sub>2</sub> = 2 gives a<sub>2</sub> = −1; and so on.</p><p>From a<sub>51</sub> to a<sub>1022</sub>, each odd/even pair adds to 0. Only a<sub>1023</sub> = 1 is left, so the sum is <b>1</b>.</p>"),
6: dict(ans="44", hints=[
 "Write it in prime factors first: 10<sup>4</sup> = 2<sup>4</sup> × 5<sup>4</sup>.",
 "A square factor uses an even power of each prime. Count the even powers allowed for each, then drop the factor 1."],
 why="<p>The number is 2<sup>8</sup> × 3<sup>5</sup> × 5<sup>4</sup>.</p><p>Even powers: 2 → 0, 2, 4, 6, 8 (5 choices); 3 → 0, 2, 4 (3); 5 → 0, 2, 4 (3). That's 45 square factors.</p><p>Leave out 1: <b>44</b>.</p>"),
7: dict(ans="B", hints=[
 "Two circles of radii R and r that touch each other and the same line touch the line 2√(Rr) apart.",
 "The small circle sits between the two big ones on the line. Its two gaps add up to the gap between the big ones."],
 why="<p>The big circles touch the line 2√(16) = 8 cm apart.</p><p>The small circle's gaps: 2√(4r) + 2√(4r) = 8√r. Set 8√r = 8, so r = <b>1 cm</b>.</p>"),
8: dict(ans="D", hints=[
 "Factor top and bottom. A common factor cancels.",
 "You get (n + 4)/(n − 4) = 1 + 8/(n − 4). When is that a whole number?"],
 why="<p>(n + 3)(n + 4)/((n − 4)(n + 3)) = 1 + 8/(n − 4).</p><p>n − 4 must divide 8, and the biggest choice is 8. So n = <b>12</b>, which gives 2.</p>"),
9: dict(ans="A", hints=[
 "If both had grown 10%, the total would be 12650. The extra 110 comes from non-fiction's additional 2%.",
 "So 2% of non-fiction (2010) = 110."],
 why="<p>Non-fiction 2010 = 5500, so fiction 2010 = 6000.</p><p>Fiction 2015 = 6000 × 1.1 = <b>6600</b>. 6000 is the trap: that's the 2010 figure.</p>"),
10: dict(ans="12", hints=[
 "f(1) = f(1 × 1) = f(1)<sup>2</sup>, so f(1) = 1. And 24 = 2<sup>3</sup> × 3.",
 "So f(2)<sup>3</sup> × f(3) = 54, with f(2) > 1. Which whole numbers work?"],
 why="<p>54 = 27 × 2, so f(2) = 3 and f(3) = 2. (f(2) can't be 1, since f(2) > f(1).)</p><p>f(18) = f(2) × f(3)<sup>2</sup> = 3 × 4 = <b>12</b>.</p>"),
11: dict(ans="150", hints=[
 "Interior angle of a regular n-gon = 180 − 360/n.",
 "Set 180 − 360/(2a) = 1.5 × (180 − 360/a) and solve for a."],
 why="<p>180 − 180/a = 270 − 540/a gives 360/a = 90, so a = 4 and b = 8 (angles 90° and 135°).</p><p>A 12-sided polygon has interior angle 180 − 30 = <b>150°</b>.</p>"),
12: dict(ans="C", hints=[
 "The 45th motorcycle leaves at 10:45 and just reaches B at 11:00. So a motorcycle takes 15 minutes.",
 "At double speed the cyclist arrives at 10:30. Which motorcycles get there by then?"],
 why="<p>A motorcycle reaches B by 10:30 only if it left by 10:15.</p><p>Those leave at 10:01, 10:02, ..., 10:15: <b>15</b> motorcycles. 22 or 23 is the trap of just halving 45.</p>"),
13: dict(ans="C", hints=[
 "Real and distinct roots need the discriminant to be greater than 0.",
 "16 + 4 log<sub>2</sub>A > 0. Solve for A."],
 why="<p>log<sub>2</sub>A > −4, so A > 2<sup>−4</sup> = <b>1/16</b>.</p>"),
14: dict(ans="48", hints=[
 "In the same time, John covers 9 laps of A and Mary 5 laps of B. Distance is speed × time.",
 "So 9A : 5B = 6 : 7.5. Find A : B, then use A + B = 325."],
 why="<p>A/B = (6/9)/(7.5/5) = 4/9, so A = 100 m and B = 225 m.</p><p>Mary's speed: 7.5 km/h = 25/12 m/s. 100 ÷ 25/12 = <b>48 seconds</b>.</p>"),
15: dict(ans="A", hints=[
 "Anil does 5% a day and Sunil 2.5% a day. Anil's first 3 days do 15%.",
 "Bimal does 10%. The rest is done by Anil and Sunil together after day 3."],
 why="<p>After the first 3 days, Anil and Sunil do 100 − 15 − 10 = 75%, at 7.5% a day. That's 10 more days.</p><p>Total = 3 + 10 = <b>13 days</b>.</p>"),
16: dict(ans="B", hints=[
 "Let the revised scores be 11k, 10k and 3k. So the originals are 11k − 6, 10k − 6 and 3k − 6.",
 "Use 12 × Rama's original = Mohan's original + Anjali's original."],
 why="<p>12(3k − 6) = 21k − 12 gives 15k = 60, so k = 4.</p><p>Anjali 38, Rama 6 originally: the difference is <b>32</b> (and still 32 after both gain 6).</p>"),
17: dict(ans="80", hints=[
 "Chain the percentages: A = 0.9B, B = 1.25C, C = 0.8D.",
 "Multiply them to get A in terms of D."],
 why="<p>A = 0.9 × 1.25 × 0.8 × D = 0.9D.</p><p>72 = 0.9D gives D = <b>80</b>.</p>"),
18: dict(ans="A", hints=[
 "The top is straight above the centre of the square base. Its distance from a corner is half the diagonal.",
 "Half the diagonal is 10√2. The slanting edge is 20. Use Pythagoras."],
 why="<p>h<sup>2</sup> = 20<sup>2</sup> − (10√2)<sup>2</sup> = 400 − 200 = 200.</p><p>h = <b>10√2</b>.</p>"),
19: dict(ans="C", hints=[
 "A square root needs what's inside to be ≥ 0, and a natural log is ≥ 0 when its input is ≥ 1.",
 "So (4x − x<sup>2</sup>)/3 ≥ 1."],
 why="<p>4x − x<sup>2</sup> ≥ 3 gives x<sup>2</sup> − 4x + 3 ≤ 0, so (x − 1)(x − 3) ≤ 0.</p><p>That's <b>1 ≤ x ≤ 3</b>.</p>"),
20: dict(ans="A", hints=[
 "A right angle at A means A lies on the circle with BC as its diameter.",
 "AP is A's height above BC. How high can a point on that circle get?"],
 why="<p>The circle has radius 10, so the highest A can be is 10 above the diameter (the isosceles case).</p><p>Maximum AP = <b>10 cm</b>.</p>"),
21: dict(ans="A", hints=[
 "When they meet, A has done 60% of the track and B 40%. So their speeds are 3 : 2.",
 "A does the remaining 40% in 12 minutes. Use that to work out when they started and how long B takes for a full lap."],
 why="<p>A covers 40% in 12 min, so 60% took 18 min: they started at 9:42. A full lap takes A 30 min.</p><p>B is 2/3 as fast, so a lap takes B 45 min. B returns at 9:42 + 45 min = <b>10:27 am</b>.</p>"),
22: dict(ans="4", hints=[
 "n<sup>2</sup> − m<sup>2</sup> = (n − m)(n + m) = 105.",
 "List factor pairs of 105 with the smaller first. Each pair gives one (m, n) if both factors have the same parity."],
 why="<p>105 = 1 × 105 = 3 × 35 = 5 × 21 = 7 × 15. All factors are odd, so each pair works, and m > 0 every time.</p><p>That's <b>4</b> pairs, for example (52, 53) and (4, 11).</p>"),
23: dict(ans="A", hints=[
 "Let 2010 salaries be 6k, 5k and 7k. Ramesh's 2015 salary is 7.5k.",
 "In 2015 Rajesh earns the same as Ramesh (ratio 3 : 4 : 3)."],
 why="<p>Rajesh: 7k to 7.5k.</p><p>Increase = 0.5/7 ≈ 7.1%, closest to <b>7</b>.</p>"),
24: dict(ans="D", hints=[
 "Fewest cylinders means each one is as big as possible, while dividing all three volumes exactly. Find the HCF of 405, 783 and 351.",
 "Each cylinder is 27 cc with r = 3, which fixes its height. Then find one cylinder's total surface area."],
 why="<p>HCF = 27, so there are 15 + 29 + 13 = 57 cylinders. 9πh = 27 gives h = 3/π.</p><p>One cylinder: 2πr<sup>2</sup> + 2πrh = 18π + 18.</p><p>Total = 57 × 18(π + 1) = <b>1026(1 + π)</b>.</p>"),
25: dict(ans="B", hints=[
 "Sum of roots = −b and product = c. So b = −7a and c = 12a<sup>2</sup>.",
 "b<sup>2</sup> + c = 61a<sup>2</sup>. Which option is 61 times a perfect square?"],
 why="<p>549 = 61 × 9, so a = 3 works.</p><p>So the answer is <b>549</b>. 3721 is the trap: it's 61<sup>2</sup>, which would need a<sup>2</sup> = 61.</p>"),
26: dict(ans="7", hints=[
 "Call the first digit a. Write every other digit in terms of a.",
 "The fourth digit turns out to be 7a. A digit can't be more than 9."],
 why="<p>The digits are a, 2a, a, then 7a, 3a, 4a.</p><p>7a ≤ 9 forces a = 1, so the fourth digit is <b>7</b> (the number is 121734).</p>"),
27: dict(ans="D", hints=[
 "Let each bicycle cost p. Six gain 0.25p each, four lose 0.25p each.",
 "The net is 2 × 0.25p."],
 why="<p>Net profit = 0.5p = 2000.</p><p>p = <b>₹4000</b>.</p>"),
28: dict(ans="A", hints=[
 "The first common term is 19. After that, common terms step by the LCM of 4 and 5.",
 "Count terms 19, 39, 59, ... that stay within both lists, so up to 415."],
 why="<p>19 + 20k ≤ 415 gives k ≤ 19.8, so k = 0 to 19.</p><p>That's <b>20</b> terms (the last is 399).</p>"),
29: dict(ans="4851", hints=[
 "Count the terms: 1, 3, 5, ..., 47 is 24 odd numbers.",
 "The sum is 24 × 2n + (1 + 3 + ... + 47) = 48n + 24<sup>2</sup>."],
 why="<p>48n + 576 = 5280 gives n = 98.</p><p>1 + 2 + ... + 98 = 98 × 99/2 = <b>4851</b>.</p>"),
30: dict(ans="D", hints=[
 "Track grams of salt. A has 50 g, B 110 g and C 160 g at the start.",
 "100 ml of a solution carries (strength) grams. Recalculate each strength after each move."],
 why="<p>A → B: 10 g moves. B is 120 g in 600 ml, which is 20%.</p><p>B → C: 20 g moves. C is 180 g in 600 ml, which is 30%.</p><p>C → A: 30 g moves. A is 40 + 30 = 70 g in 500 ml, so <b>14%</b>.</p>"),
31: dict(ans="13", hints=[
 "Let u = 5<sup>x</sup> and v = 3<sup>y</sup>. The second equation becomes u/5 + 3v = 9686.",
 "Multiply it by 5, then subtract the first equation to find v."],
 why="<p>u + 15v = 48430 and u − v = 13438 give 16v = 34992, so v = 2187 = 3<sup>7</sup>.</p><p>u = 15625 = 5<sup>6</sup>. So x + y = 6 + 7 = <b>13</b>.</p>"),
32: dict(ans="20920", hints=[
 "Amal's first investment earns a plain 8% for one year. The second earns 3% twice.",
 "Add the two interests, then set 7.5% of Bimal's money equal to that."],
 why="<p>12000 × 0.08 = 960. 10000 × (1.03<sup>2</sup> − 1) = 609. Total 1569.</p><p>0.075B = 1569 gives B = <b>₹20920</b>.</p>"),
33: dict(ans="A", hints=[
 "Bimal pays 1.2 × 1.3 × p and Barun pays 0.8 × 0.7 × p.",
 "Subtract and divide by p."],
 why="<p>x = 1.56p and y = 0.56p.</p><p>(x − y)/p = <b>1</b>.</p>"),
34: dict(ans="12", hints=[
 "Let R be regular hours and O overtime hours. Overtime pay is twice regular pay per hour.",
 "114 O = 0.15 × 57 R, and R + O = 172."],
 why="<p>2O = 0.15R gives R = 40O/3.</p><p>40O/3 + O = 172 gives 43O/3 = 172, so O = <b>12 hours</b>.</p>"),
}
