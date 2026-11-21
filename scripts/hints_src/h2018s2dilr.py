_fs = ("<p>Let x be the number in all three. Only L = 2x, only G = 2x − 1. Ten of G's 17 are in another sport, so only G = 7, x = 4 and only L = 8. G's pairs: (G and K only) + (G and L only) = 6.</p>"
 "<p>Only K equals everyone in both K and L (the K-and-L-only group plus the 4 in all three). The total of 39 then gives only K = 9 and K-and-L-only = 5. So K = 18 + (G and K only) and L = 17 + (G and L only).</p>")
_fh1 = "Let x be the number in all three. Write only L and only G in terms of x, then use \"ten students in G are in another sport too\"."
_fh2 = "Read \"both K and L\" as including the students in all three. With the total of 39, that fixes only K."
_fs3 = ("<p>After the withdrawals, say a of the 4 leave G, b leave L and 1 leaves K (a + b = 3). G = 17 − a and L = 17 + gl − b, where gl is G-and-L-only, and G = L − 6. That gives b − a = gl − 6, which works only with gl = 5, a = 2 and b = 1. So G-and-K-only = 1.</p>")
_lc = ("<p>\"is\" = 35 and \"as\" = 56 share S, so S = 5, I = 3, A = 6. In Peacock, C appears twice and there are three 9s, so C = 9 and one more Peacock letter is 9.</p>"
 "<p>designated: D appears twice, so D = 1. E appears twice and fills the 5s with S, so E = 5. \"the\" = 458 then gives T = 8 and H = 4, and G and N are 6 and 7. national has four 6s, so N = 6 and G = 7; O and L are 1 and 9, and \"of\" = 79 gives O = 9, L = 1 and F = 7. Peacock's P and K are both 8. bird gives B and R as 3 and 4 in some order.</p>"
 "<p>Known so far: 1 = D, L, ?; 3 = I, ?, ?; 4 = H, ?, ?; 5 = S, E, ?; 6 = A, N, ?; 7 = G, F, ?; 8 = T, P, K; 9 = C, O; 2 = three letters not yet used.</p>")
_lch1 = "Compare \"is\" (35) and \"as\" (56). Which letter do they share?"
_lch2 = "A letter used twice in a word puts its digit in the code twice. Use that on Peacock, designated and national."
_jb = ("<p>Erina was alone and Room 102 had two people, so the third room had 4: Akil, two others, and Fatima as the 4th. Balaram was 3rd into Room 101, so that big room is 101 and Erina is in 103.</p>"
 "<p>Chitra (7:30) was last into her room, so not 101 (Fatima came after). She's in 102 with Ganeshan, who came before her. That leaves Divya in 101. The 7:45 arrival can't be in 101 or 102, so it's Erina.</p>"
 "<p>Balaram, Divya and Ganeshan arrived at 7:10, 7:15 and 7:25, with Divya before Balaram.</p>")
_jh1 = "Erina's room has 1 and Room 102 has 2. How many does that leave in the third room? Fatima's statement says it has Akil and two others before her."
H = {
9: dict(ans="4", hints=[_fh1, _fh2 + " Then L must be bigger than K."], why=_fs + "<p>L > K needs 17 + gl > 18 + (6 − gl), so gl ≥ 4 (gl = 4 gives L 21, K 20). The minimum is <b>4</b>.</p>"),
10: dict(ans="C", hints=[_fh1, _fh2], why=_fs + "<p>K : L = 19 : 22 with the two pair counts adding up to 6 gives G-and-K-only = 1 and G-and-L-only = 5. L = <b>22</b>.</p>"),
11: dict(ans="2", hints=[_fh1, "Of the 4 in all three, say a leave G, b leave L and 1 leaves K. Use G = L − 6 after."], why=_fs + _fs3 + "<p>G and K after: 1 + the one who dropped L = <b>2</b>.</p>"),
12: dict(ans="D", hints=[_fh1, "Of the 4 in all three, say a leave G, b leave L and 1 leaves K. Use G = L − 6 after."], why=_fs + _fs3 + "<p>G and L after: 5 + the one who dropped K = <b>6</b>.</p>"),
21: dict(ans="C", hints=[_jh1, "Who can be the 7:45 arrival? And which room must Chitra be in to be last?"], why=_jb + "<p>Divya was <b>definitely in Room 101</b>.</p>"),
22: dict(ans="A", hints=[_jh1, "Room 102 has Ganeshan and Chitra. Who arrived first?"], why=_jb + "<p>Ganeshan came before Chitra, so <b>no one</b> was there yet.</p>"),
23: dict(ans="A", hints=[_jh1, "The 7:45 person arrived after Fatima and after Chitra. Which room could they be in?"], why=_jb + "<p>Erina arrived at <b>7:45 am</b>.</p>"),
24: dict(ans="A", hints=[_jh1, "Balaram, Divya and Ganeshan take 7:10, 7:15 and 7:25, with Divya before Balaram."], why=_jb + "<p>With Ganeshan before Divya: Ganeshan 7:10, Divya 7:15, Balaram <b>7:25 am</b>.</p>"),
25: dict(ans="D", hints=[_lch1, _lch2], why=_lc + "<p>L = <b>1</b>.</p>"),
26: dict(ans="D", hints=[_lch1, "In bird (1334), I and D are known. What's left for B and R?"], why=_lc + "<p>B is <b>3 or 4</b>.</p>"),
27: dict(ans="A", hints=[_lch1, _lch2], why=_lc + "<p>Only 8 (T, P, K) and 9 (C, O) are complete: <b>2</b> digits.</p>"),
28: dict(ans="A", hints=[_lch2, "S is 5, and 5 already has S and E. How many spaces does it have left?"], why=_lc + "<p>S, U and V would need two more spaces at digit 5, which has only one left. So <b>S, U, V</b> can't share a digit. X, Y, Z fit at 2; S, E, Z at 5; I, B, M at 3.</p>"),
}
