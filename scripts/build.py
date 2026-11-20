#!/usr/bin/env python3
"""Merge data/raw/*.json with the answer keys into data.js (window.CAT_DATA)."""
import json, glob, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw")

def load_keys(path, strip_sets):
    keys = {}
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        tag, rest = line.split(":", 1)
        d = {}
        for tok in rest.replace("|", " ").split():
            m = re.match(r"^(\d+)(=?)(.+)$", tok)
            if not m:
                continue
            n, eq, val = int(m.group(1)), m.group(2), m.group(3)
            unsure = val.endswith("?")
            val = val.rstrip("?")
            d[n] = {"kind": "TITA" if eq else "MCQ", "val": val, "unsure": unsure}
        keys[tag.strip()] = d
    return keys

qa_keys = load_keys(os.path.join(RAW, "keys-qa.txt"), False)
lr_keys = load_keys(os.path.join(RAW, "keys-dilr.txt"), True)

def answer(q, key):
    """Return (answer, unverified, note)."""
    if key is None:
        return None, True, "no key"
    if q["type"] == "MCQ":
        if key["kind"] != "MCQ" or key["val"] not in "ABCD":
            return None, True, "key type mismatch"
        idx = "ABCD".index(key["val"])
        if idx >= len(q.get("opts", [])):
            return None, True, "key out of range"
        return idx, key["unsure"], ""
    if key["kind"] != "TITA":
        return None, True, "key type mismatch"
    return key["val"], key["unsure"], ""

units, problems = [], []
for path in sorted(glob.glob(os.path.join(RAW, "*.json"))):
    d = json.load(open(path, encoding="utf-8"))
    tag = f'{d["year"]}-s{d["slot"]}'
    base = d["source"]
    if d["section"] == "QA":
        pat = d.get("solPattern", "quants-question-{n}.shtml")
        keys = qa_keys.get(tag, {})
        for it in d["items"]:
            ans, unv, note = answer(it, keys.get(it["n"]))
            if note: problems.append(f"{tag} QA q{it['n']}: {note}")
            units.append({
                "id": f"{tag}-qa-{it['n']}", "kind": "single", "section": "Quant",
                "year": d["year"], "slot": d["slot"],
                "qs": [{"id": f"{tag}-qa-{it['n']}", "n": it["n"], "topic": it.get("topic", ""),
                        "type": it["type"], "q": it["q"], "opts": it.get("opts"),
                        "ans": ans, "unverified": unv,
                        "sol": base + pat.format(n=it["n"])}],
                "source": base})
    else:
        pat = d.get("solPattern", "dilr-question-{n}.shtml")
        keys = lr_keys.get(tag, {})
        for si, s in enumerate(d["sets"]):
            qs = []
            for q in s["qs"]:
                ans, unv, note = answer(q, keys.get(q["n"]))
                if note: problems.append(f"{tag} {s['title']} q{q['n']}: {note}")
                qs.append({"id": f"{tag}-lr-{q['n']}", "n": q["n"], "type": q["type"], "q": q["q"],
                           "opts": q.get("opts"), "ans": ans, "unverified": unv,
                           "sol": (lambda s: s if s.startswith("http") else base + s)(q.get("sol") or pat.format(n=q["n"]))})
            units.append({"id": f"{tag}-set-{si+1}", "kind": "set", "section": s["section"],
                          "year": d["year"], "slot": d["slot"], "title": s["title"],
                          "passage": s["passage"], "qs": qs, "source": base})

out = os.path.join(ROOT, "data.js")
with open(out, "w", encoding="utf-8") as f:
    f.write("window.CAT_DATA = ")
    json.dump({"built": "2026-11-20", "units": units}, f, ensure_ascii=False, separators=(",", ":"))
    f.write(";\n")

from collections import Counter
qs = [(u["section"], u["year"], q) for u in units for q in u["qs"]]
print("questions:", len(qs), "units:", len(units))
print("by section:", dict(Counter(s for s, _, _ in qs)))
print("by year:", dict(sorted(Counter(y for _, y, _ in qs).items())))
print("unverified:", sum(1 for *_, q in qs if q["unverified"]))
print("problems:", problems)
