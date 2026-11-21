"""Write data/hints/<tag>.json from scripts/hints_src/h<tag>.py (H dict)."""
import importlib.util, json, os, sys
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
src = os.path.join(root, "scripts", "hints_src")
for f in sorted(os.listdir(src)):
    if not (f.startswith("h") and f.endswith(".py")): continue
    spec = importlib.util.spec_from_file_location(f[:-3], os.path.join(src, f))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    tag = getattr(m, "TAG", None)
    if not tag:
        b = f[1:-3]  # e.g. 2023s1qa
        tag = f"{b[:4]}-s{b[5]}-{b[6:]}"
    out = os.path.join(root, "data", "hints", tag + ".json")
    json.dump({str(k): m.H[k] for k in sorted(m.H)}, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(tag, len(m.H))
