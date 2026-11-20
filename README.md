# CAT Practice

A small static site for practising past CAT questions (Quant, LR and DI) by hand, one at a time.

- Random order, with LR/DI sets kept together. Reshuffle any time.
- Filter by section and year, or show only unattempted, mistakes or flagged questions.
- Multiple-choice buttons or a box for type-in (TITA) answers, a Check button, and a link to 2IIM's explanation.
- Per-question timer, progress by section, all saved in your browser (localStorage).

## Data

Questions come from past CAT papers (set by the IIMs), transcribed from 2IIM's online question bank
(https://online.2iim.com/CAT-question-paper/). Answer keys are from the same pages. Sets that depend on a chart or
picture are left out. Raw files are in `data/raw/`; `python3 scripts/build.py` rebuilds `data.js`.

No build step is needed to run the site: open `index.html` or serve the folder (GitHub Pages works as is).
