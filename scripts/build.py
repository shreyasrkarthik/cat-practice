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
HINTS = os.path.join(ROOT, "data", "hints")
hint_stats = {"with": 0, "without": 0, "mismatch": []}

def load_hints(name):
    p = os.path.join(HINTS, name)
    if not os.path.exists(p):
        return {}
    return {int(k): v for k, v in json.load(open(p, encoding="utf-8")).items()}

def add_hints(qd, h, label):
    """Attach hints/why. h["ans"] is the answer my own working reached; it must match the key."""
    if not h:
        hint_stats["without"] += 1
        return
    hint_stats["with"] += 1
    qd["hints"] = h.get("hints", [])
    qd["why"] = h.get("why", "")
    mine = str(h.get("ans", "")).strip()
    if qd["ans"] is None:
        return
    key = "ABCD"[qd["ans"]] if qd["type"] == "MCQ" else str(qd["ans"])
    if mine != key:
        hint_stats["mismatch"].append(f"{label}: my working gives {mine!r}, key says {key!r}")
for path in sorted(glob.glob(os.path.join(RAW, "*.json"))):
    d = json.load(open(path, encoding="utf-8"))
    tag = f'{d["year"]}-s{d["slot"]}'
    base = d["source"]
    if d["section"] == "QA":
        pat = d.get("solPattern", "quants-question-{n}.shtml")
        keys = qa_keys.get(tag, {})
        hints = load_hints(f"{tag}-qa.json")
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
            add_hints(units[-1]["qs"][0], hints.get(it["n"]), f"{tag} QA q{it['n']}")
    else:
        pat = d.get("solPattern", "dilr-question-{n}.shtml")
        keys = lr_keys.get(tag, {})
        hints = load_hints(f"{tag}-dilr.json")
        for si, s in enumerate(d["sets"]):
            qs = []
            for q in s["qs"]:
                ans, unv, note = answer(q, keys.get(q["n"]))
                if note: problems.append(f"{tag} {s['title']} q{q['n']}: {note}")
                qs.append({"id": f"{tag}-lr-{q['n']}", "n": q["n"], "type": q["type"], "q": q["q"],
                           "opts": q.get("opts"), "ans": ans, "unverified": unv,
                           "sol": (lambda s: s if s.startswith("http") else base + s)(q.get("sol") or pat.format(n=q["n"]))})
                add_hints(qs[-1], hints.get(q["n"]), f"{tag} DILR q{q['n']}")
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
print("with hints:", hint_stats["with"], "without:", hint_stats["without"])
print("hint answer mismatches:", hint_stats["mismatch"])

# Stamp index.html so browsers fetch the new data.js/app.js/styles.css instead of a cached copy.
import hashlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
h = hashlib.md5()
for f in ("data.js", "app.js", "styles.css"):
    h.update(open(os.path.join(ROOT, f), "rb").read())
idx = os.path.join(ROOT, "index.html")
html = open(idx, encoding="utf-8").read()
new = re.sub(r'((?:data|app)\.js|styles\.css)(\?v=[0-9a-z]*)?"', r'\1?v=' + h.hexdigest()[:8] + '"', html)
if new != html:
    open(idx, "w", encoding="utf-8").write(new)
print("cache stamp:", h.hexdigest()[:8])
