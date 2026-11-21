_obj = ("<p>Values of 10 fix two objects: Barat gets o9 and Elise gets o10. Barat's total must be even and at most 16, so his other object is o7 (10 + 6 = 16). Elise's must be even and at most 16, so her other object is o1 or o5 (10 + 6).</p>"
 "<p>A third person is at 16, and it can't be Disha (her total is odd). Checking the rest against the rules on o1, o2, o3 and o8 and on envy leaves one allocation:</p>"
 "<p>Amar o2 + o6 (12), Barat o7 + o9 (16), Charles o3 + o8 (16), Disha o1 + o4 (13), Elise o5 + o10 (16). Amar envies Barat and Charles, Disha envies Barat, and nobody else envies anyone.</p>")
_oh1 = "Start with the 10s: who must get o9 and o10? Then their totals must be even and at most 16. What can the second object be?"
_oh2 = "Disha's own total is odd, so the third person at 16 is Amar or Charles. Try each and check the envy rule: only people below 16 may envy, and only people at 16."
_ch = ("<p>Count games: a group's top seed plays at least the group final; a 2nd/3rd seed who wins the group plays 2 group games. Aruna (3 games) never met Arif, so Aruna must be Group A's top seed. Azul beat Arif, then lost to Aruna.</p>"
 "<p>Group D: Donna and Deb each played once, so Dipen was in the first game, won both group games, and lost his semi-final (3 games). So Group C's winner reached the final. Chitra is the only one in C who can have 3 games as winner: she's C's top seed, beat Chetan, beat Dipen, and played the final.</p>"
 "<p>Biju (3 games) won Group B from 2nd/3rd seed and lost the semi to Aruna. Aruna played the final against Chitra, and Chitra didn't win, so <b>Aruna</b> is the champion.</p>")
_chh1 = "Write how many games each kind of player can play: top seed who wins the group, 2nd/3rd seed who wins the group, and so on. Then match those to Aruna's 3, Azul's 2, Arif's 1."
_chh2 = "In Group D, Donna and Deb played one game each. Could Dipen be the top seed? Then how far did Dipen get?"
_rv = ("<p>Behaviour: Atal 7, Deepak 5, Bihari and Chirag 6. Timeliness: Atal beats Bihari and Chirag, so Bihari, Chirag and Deepak share a value x and Atal has y, with 3x + y = 21.</p>"
 "<p>Packaging and Hygiene, with Chirag's two equal, Bihari top in Packaging, Chirag top in Hygiene, and Atal and Deepak holding the same rank in both, work out to only: Packaging Atal 5, Bihari 9, Chirag 8, Deepak 7; Hygiene Atal 5, Bihari 7, Chirag 8, Deepak 6. The ₹120 total then needs x = 5 and y = 6.</p>"
 "<p>Totals: Atal 23, Bihari 27, Chirag 27, Deepak 23. Bihari and Chirag get ₹20 bonuses (₹40), so Atal and Deepak tip ₹80 between them: one ₹30 and one ₹50.</p>")
_rh1 = "Behaviour is fixed straight away: unique max Atal, unique min Deepak, all between 5 and 7. In Timeliness, who must share the repeated value?"
_rh2 = "Packaging: four different values adding to 29, Bihari highest. Hygiene: four different adding to 26, Chirag highest, and his Packaging equals his Hygiene. List the small number of options."
H = {
1: dict(ans="D", hints=[_oh1, _oh2], why=_obj + "<p>So o8 went to <b>Charles</b>.</p>"),
2: dict(ans="A", hints=[_oh1, _oh2], why=_obj + "<p>Of the four options, only <b>Amar</b> envies someone.</p>"),
3: dict(ans="12", hints=[_oh1, _oh2], why=_obj + "<p>Amar values his own bundle at 9 + 3 = <b>12</b>.</p>"),
4: dict(ans="A", hints=[_oh1, _oh2], why=_obj + "<p>o4 went to <b>Disha</b>.</p>"),
5: dict(ans="B", hints=[_oh1, "Elise's second object is o1 or o5. Which one leaves o1, o2 and o3 with three different people?"], why=_obj + "<p>o5 went to <b>Elise</b>.</p>"),
6: dict(ans="D", hints=[_oh1, _oh2], why=_obj + "<p>o1 went to <b>Disha</b> (o1 + o4 = 13, her odd total).</p>"),
11: dict(ans="C", hints=[_chh1, _chh2], why=_ch + "<p>Dipen played the opening group game, so he was <b>definitely not</b> a top seed.</p>"),
12: dict(ans="D", hints=[_chh1, _chh2], why=_ch + "<p>Chitra and Dipen met in the semi-final. (Donna and Deb never met: Dipen played one, then the other.) Answer: <b>Chitra, Dipen</b>.</p>"),
13: dict(ans="D", hints=[_chh1, "Who reaches the final from each side? Remember Chitra did not win."], why=_ch),
14: dict(ans="D", hints=[_chh1, _chh2], why=_ch + "<p>Chitra played Chetan, Dipen and Aruna, but not <b>Biju</b>.</p>"),
15: dict(ans="5", hints=[_rh1, _rh2], why=_rv + "<p>The lowest rating anywhere is <b>5</b>.</p>"),
16: dict(ans="B", hints=[_rh1, _rh2], why=_rv + "<p>The top total, 27, is shared by <b>Bihari and Chirag</b>.</p>"),
17: dict(ans="6", hints=[_rh1, "3x + y = 21 allows x = 4, y = 9 or x = 5, y = 6. The ₹120 of bonuses and tips decides which."], why=_rv + "<p>Atal gave <b>6</b> for Timeliness.</p>"),
18: dict(ans="A", hints=[_rh2, "Who earns a bonus (total 25 or more)? Whatever's left of ₹120 comes from tips of ₹30 or ₹50."], why=_rv + "<p>Deepak tipped <b>either ₹30 or ₹50</b>.</p>"),
19: dict(ans="A", hints=[_rh1, _rh2], why=_rv + "<p>Atal's ratings: Behaviour 7, Packaging 5, Hygiene 5, Timeliness 6. Highest: <b>Behaviour</b>.</p>"),
20: dict(ans="B", hints=[_rh2, "Deepak must have the same rank in Packaging and Hygiene, and so must Atal."], why=_rv + "<p>Deepak gave <b>7</b> for Packaging.</p>"),
}

# ---- DI ----
_so = ("<p>Orders as (booked–dispatched): Art 1–3, 3–4, 4–6, 6–13, 13–21. Binders 1–2, 2–4, 4–5, 5–16. Paper 2–4, 4–7, 7–12. Phones 2–4, 4–5, 5–17. Appliances 2–4, 4–12. Bookcases 3–4, 4–6, 6–7. Fasteners 2–4, 4–6, 6–8. Furnishings 1–5, 5–12. Labels 2–4, 4–12. Tables 2–4, 4–10. Chairs 2–3, 3–9. Accessories 1–19. Envelopes 3–7. Storage 2–7, 7–22. That's 35 orders.</p>")
_soh1 = "List each bar as (booking day, dispatch day). A colour change inside a row starts a new order."
H.update({
7: dict(ans="6", hints=[_soh1, "Bookings happen only at the left end of each bar. Which days from Sep 1 to 14 have no left end?"], why=_so + "<p>Bookings fall on Sep 1–7 and Sep 13 only. No booking on Sep 8, 9, 10, 11, 12 and 14: <b>6</b> days.</p>"),
8: dict(ans="11", hints=[_soh1, "Which rows are a single colour all the way?"], why=_so + "<p>Only Accessories (18 days) and Envelopes (4 days) use one ship mode. Average (18 + 4) ÷ 2 = <b>11</b>.</p>"),
9: dict(ans="D", hints=[_soh1, "Average processing time = (last dispatch − first booking) ÷ number of orders, since orders follow each other with no gap."], why=_so + "<p>Phones 15/3 = 5, Art 20/5 = 4, Binders 15/4 = 3.75, Paper 10/3 ≈ 3.33. Order: <b>Phones, Art, Binders, Paper</b>.</p>"),
10: dict(ans="B", hints=[_soh1, "Count the bars exactly one day long, and count all bars."], why=_so + "<p>One-day orders: Art 3–4, Binders 1–2 and 4–5, Phones 4–5, Bookcases 3–4 and 6–7, Chairs 2–3: 7 of 35 = <b>20%</b>.</p>"),
})
