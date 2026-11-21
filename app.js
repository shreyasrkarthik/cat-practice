(function () {
  "use strict";
  var DATA = window.CAT_DATA || { units: [] };
  var KEY = "catPractice.v1";
  var LETTERS = ["A", "B", "C", "D"];

  // ---------- storage ----------
  function loadStore() {
    try {
      var raw = localStorage.getItem(KEY);
      if (raw) return JSON.parse(raw);
    } catch (e) {}
    return null;
  }
  var store = loadStore() || {};
  store.q = store.q || {};            // per-question state
  store.filters = store.filters || { secs: ["Quant", "LR", "DI"], year: "all", mode: "all" };
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(store)); } catch (e) {}
  }

  // ---------- index ----------
  var unitById = {}, qIndex = {};
  DATA.units.forEach(function (u) {
    unitById[u.id] = u;
    u.qs.forEach(function (q, i) { qIndex[q.id] = { unit: u, q: q, i: i }; });
  });

  function shuffle(arr) {
    var a = arr.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }
  function ensureOrder() {
    var ids = DATA.units.map(function (u) { return u.id; });
    var ok = Array.isArray(store.order) && store.order.length === ids.length &&
      store.order.every(function (id) { return unitById[id]; });
    if (!ok) { store.order = shuffle(ids); store.cur = null; save(); }
  }
  ensureOrder();

  // ---------- helpers ----------
  function st(id) { return store.q[id] || (store.q[id] = {}); }
  function render(html) {
    return String(html).replace(/\[\[([\s\S]*?)\|\|([\s\S]*?)\]\]/g,
      '<span class="frac"><span class="num">$1</span><span class="den">$2</span></span>');
  }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }
  function fmtTime(ms) {
    var s = Math.floor((ms || 0) / 1000), m = Math.floor(s / 60);
    s = s % 60;
    return m + ":" + (s < 10 ? "0" : "") + s;
  }
  function norm(s) { return String(s).trim().toLowerCase().replace(/[\s,₹]/g, ""); }
  function titaMatch(given, ans) {
    var g = norm(given), a = norm(ans);
    if (g === "") return false;
    var gn = Number(g), an = Number(a);
    if (!isNaN(gn) && !isNaN(an)) return Math.abs(gn - an) < 1e-6;
    return g === a;
  }
  function ansText(q) {
    if (q.type === "MCQ") return LETTERS[q.ans] + ". " + q.opts[q.ans];
    return q.ans;
  }

  // ---------- sequence ----------
  var seq = [], pos = 0;
  function buildSeq(keepId) {
    var f = store.filters;
    seq = [];
    store.order.forEach(function (uid) {
      var u = unitById[uid];
      if (f.secs.indexOf(u.section) < 0) return;
      if (f.year !== "all" && String(u.year) !== f.year) return;
      u.qs.forEach(function (q) {
        var s = store.q[q.id] || {};
        if (f.mode === "new" && s.done) return;
        if (f.mode === "mistakes" && !((s.done && !s.lastCorrect) || (s.revealed && !s.done))) return;
        if (f.mode === "flagged" && !s.flag) return;
        seq.push(q.id);
      });
    });
    var idx = keepId ? seq.indexOf(keepId) : -1;
    pos = idx >= 0 ? idx : 0;
  }

  // ---------- timer ----------
  var tick = null, startAt = 0, timedId = null;
  function stopTimer() {
    if (timedId && startAt) {
      var s = st(timedId);
      s.time = (s.time || 0) + (Date.now() - startAt);
      save();
    }
    startAt = 0; timedId = null;
    if (tick) { clearInterval(tick); tick = null; }
  }
  function startTimer(id) {
    stopTimer();
    var s0 = st(id);
    if (s0.done && !s0.retrying) { showTime(id); return; }
    timedId = id; startAt = Date.now();
    tick = setInterval(function () { showTime(id); }, 500);
    showTime(id);
  }
  function liveTime(id) {
    var t = (store.q[id] && store.q[id].time) || 0;
    if (timedId === id && startAt) t += Date.now() - startAt;
    return t;
  }
  function showTime(id) {
    var el = document.getElementById("timer");
    if (el) el.textContent = fmtTime(liveTime(id));
  }
  document.addEventListener("visibilitychange", function () {
    var id = seq[pos];
    if (document.hidden) stopTimer();
    else if (id) startTimer(id);
  });

  // ---------- stats ----------
  function renderStats() {
    var tot = { all: [0, 0, 0] }, bySec = { Quant: [0, 0, 0], LR: [0, 0, 0], DI: [0, 0, 0] };
    var timeSum = 0, solved = 0;
    DATA.units.forEach(function (u) {
      u.qs.forEach(function (q) {
        var s = store.q[q.id] || {};
        bySec[u.section][2]++; tot.all[2]++;
        if (s.done) {
          bySec[u.section][0]++; tot.all[0]++;
          if (s.firstCorrect) { bySec[u.section][1]++; tot.all[1]++; }
          timeSum += s.time || 0;
        }
        if (s.solved || (s.done && s.lastCorrect && !s.peeked && s.solved === undefined)) solved++;
      });
    });
    var a = tot.all, acc = a[0] ? Math.round(100 * a[1] / a[0]) : 0;
    var html = '<span>Solved <b>' + solved + "</b>/" + a[2] + "</span>" +
      '<span>Right first time <b>' + a[1] + "</b> (" + acc + "%)</span>";
    ["Quant", "LR", "DI"].forEach(function (k) {
      var b = bySec[k];
      if (b[2]) html += "<span>" + k + " <b>" + b[1] + "</b>/" + b[0] + " right</span>";
    });
    if (a[0]) html += "<span>Avg <b>" + fmtTime(timeSum / a[0]) + "</b></span>";
    document.getElementById("stats").innerHTML = html;
  }

  // ---------- card ----------
  var picked = null;
  function show() {
    var card = document.getElementById("card");
    var posEl = document.getElementById("pos");
    if (!seq.length) {
      stopTimer();
      var msg = store.filters.mode === "mistakes" ? "No mistakes to review with these filters. Nice."
        : store.filters.mode === "flagged" ? "Nothing flagged yet. Use the Flag button on a question to save it here."
        : "No questions match these filters.";
      card.innerHTML = '<div class="empty">' + msg + "</div>";
      posEl.textContent = "";
      document.getElementById("prevBtn").disabled = true;
      document.getElementById("nextBtn").disabled = true;
      renderStats();
      return;
    }
    var id = seq[pos], info = qIndex[id], u = info.unit, q = info.q, s = st(id);
    store.cur = id; save();
    picked = null;

    var meta = '<div class="meta"><span class="tag sec">' + u.section + "</span>" +
      '<span class="tag">CAT ' + u.year + " · Slot " + u.slot + "</span>" +
      (q.topic ? '<span class="tag">' + esc(q.topic) + "</span>" : "") +
      '<span class="tag">' + (q.type === "TITA" ? "Type in answer" : "Multiple choice") + "</span>" +
      '<span class="spacer"></span>' +
      '<button class="flag' + (s.flag ? " on" : "") + '" id="flagBtn">' + (s.flag ? "Flagged" : "Flag") + "</button>" +
      '<span class="timer" id="timer" title="Time on this question">0:00</span></div>';

    var qhtml = '<div class="qpart">';
    if (u.kind === "set") {
      qhtml += '<p class="setnote">Question ' + (info.i + 1) + " of " + u.qs.length + " in this set</p>";
    }
    qhtml += '<div class="qtext">' + render(q.q) + "</div>";
    if (q.type === "MCQ") {
      qhtml += '<div class="opts">';
      q.opts.forEach(function (o, i) {
        qhtml += '<button class="opt" data-i="' + i + '"><span class="k">' + LETTERS[i] + "</span><span>" + render(o) + "</span></button>";
      });
      qhtml += "</div>";
    } else {
      qhtml += '<div class="tita"><input id="titaIn" type="text" inputmode="decimal" autocomplete="off" placeholder="Your answer" aria-label="Your answer"></div>';
    }
    qhtml += '<div class="actions"><button class="check" id="checkBtn" disabled>Check</button>' +
      '<button class="ghost" id="hintBtn">Hint</button>' +
      '<button class="ghost reveal" id="explainBtn">Explain answer</button></div>';
    qhtml += '<div id="hints"></div><div id="result"></div></div>';

    var body;
    if (u.kind === "set") {
      body = '<div class="layout set"><div class="passage"><h3>' + esc(u.title) + "</h3>" + render(u.passage) + "</div>" + qhtml + "</div>";
    } else {
      body = '<div class="layout">' + qhtml + "</div>";
    }
    card.innerHTML = meta + body;

    posEl.textContent = (pos + 1) + " of " + seq.length;
    document.getElementById("prevBtn").disabled = pos === 0;
    document.getElementById("nextBtn").disabled = pos >= seq.length - 1;

    wireCard(id, q, s);
    paintState(id, q, s);
    startTimer(id);
    renderStats();
  }

  // ---------- answering flow ----------
  // 1. Answer and press Check. Right or wrong is shown, but a wrong try does not give the answer away.
  // 2. Hint shows up to two nudges, one at a time.
  // 3. Explain answer shows the answer and the full working. If it is opened before you get the
  //    question right, the question is not counted as solved and stays in "My mistakes".
  function hintsOf(q) { return q.hints || []; }
  function isLocked(s) { return !!(s.done && s.lastCorrect && !s.retrying); }
  function showsExplain(s) { return !!(s.explainOpen && !s.retrying); }

  function wireCard(id, q, s) {
    var checkBtn = document.getElementById("checkBtn");
    document.getElementById("flagBtn").onclick = function () { toggleFlag(); };
    if (q.type === "MCQ") {
      Array.prototype.forEach.call(document.querySelectorAll(".opt"), function (b) {
        b.onclick = function () { pick(Number(b.getAttribute("data-i"))); };
      });
    } else {
      var inp = document.getElementById("titaIn");
      inp.oninput = function () { checkBtn.disabled = inp.value.trim() === ""; };
      inp.onkeydown = function (e) { if (e.key === "Enter") { e.preventDefault(); doCheck(); } };
      if (!isLocked(s) && !showsExplain(s)) setTimeout(function () { try { inp.focus({ preventScroll: true }); } catch (e) {} }, 0);
    }
    checkBtn.onclick = doCheck;
    document.getElementById("hintBtn").onclick = nextHint;
    document.getElementById("explainBtn").onclick = explain;
  }

  // Draw everything below the options from the saved state of this question.
  function paintState(id, q, s) {
    var locked = isLocked(s), expl = showsExplain(s);
    var hints = hintsOf(q), shown = Math.min(s.hints || 0, hints.length);
    if (s.retrying) shown = Math.min(shown, hints.length);
    // options / input
    if (q.type === "MCQ") {
      Array.prototype.forEach.call(document.querySelectorAll(".opt"), function (b) {
        var i = Number(b.getAttribute("data-i"));
        b.classList.remove("picked", "right", "wrong");
        b.disabled = locked || expl;
        if ((locked || expl) && i === q.ans) b.classList.add("right");
        if (locked && !s.lastCorrect && i === s.lastAnswer) b.classList.add("wrong");
        if (!locked && !expl && s.done && !s.lastCorrect && !s.retrying && i === s.lastAnswer) {
          b.classList.add("wrong"); b.disabled = true;
        }
      });
    } else {
      var inp = document.getElementById("titaIn");
      inp.disabled = locked || expl;
      if (locked) inp.value = s.lastAnswer;
      else if (s.done && !s.lastCorrect && !s.retrying && !expl) inp.value = s.lastAnswer;
    }
    var checkBtn = document.getElementById("checkBtn");
    checkBtn.style.display = locked || expl ? "none" : "";
    checkBtn.disabled = true;
    // hints
    var hb = document.getElementById("hintBtn");
    hb.style.display = (!locked && !expl && shown < hints.length) ? "" : "none";
    hb.textContent = shown === 0 ? "Hint" : "Hint " + (shown + 1) + " of " + hints.length;
    var hh = "";
    for (var k = 0; k < shown; k++) hh += '<div class="hint"><span class="hk">Hint ' + (k + 1) + "</span>" + render(hints[k]) + "</div>";
    document.getElementById("hints").innerHTML = hh;
    // explain button
    var eb = document.getElementById("explainBtn");
    eb.style.display = expl ? "none" : "";
    eb.textContent = locked ? "Explain why" : "Explain answer";
    // result line
    var res = "";
    if (expl) {
      res = '<div class="result shown"><div>The answer is <b>' + render(ansText(q)) + "</b>" + (/[.?!]\s*$/.test(ansText(q)) ? "" : ".") + "</div>" +
        (q.why ? '<div class="why">' + render(q.why) + "</div>" : "") +
        '<div class="sub"><a href="' + esc(q.sol) + '" target="_blank" rel="noopener">2IIM\'s explanation</a>' +
        (s.done && s.lastCorrect && !s.peeked ? "" : " · Not counted as solved.") +
        (q.unverified ? " · Answer key not double-checked." : "") +
        (s.done && s.lastCorrect ? ' · <button class="retry" id="hideBtn">Hide</button>'
          : ' · <button class="retry" id="hideBtn">Hide and try again</button>') + "</div></div>";
    } else if (locked) {
      res = '<div class="result good"><b>Correct.</b>' +
        '<div class="sub">Time ' + fmtTime(s.time) +
        (s.tries > 1 ? " · " + s.tries + " tries" : "") +
        (s.hints ? " · " + s.hints + (s.hints === 1 ? " hint" : " hints") : "") +
        (!s.firstCorrect ? " · counted as a miss in your first-try score" : "") +
        (s.peeked ? " · not counted as solved, you opened the explanation first" : "") +
        ' · <button class="retry" id="retryBtn">Try again</button></div></div>';
    } else if (s.done && !s.lastCorrect && !s.retrying) {
      res = '<div class="result bad"><b>Not quite.</b> ' +
        (q.type === "MCQ" ? "Pick another option" : "Change your answer") +
        (shown < hints.length ? ", or take a hint." : ", or open the explanation.") + "</div>";
    }
    document.getElementById("result").innerHTML = res;
    var rb = document.getElementById("retryBtn"); if (rb) rb.onclick = retry;
    var hd = document.getElementById("hideBtn"); if (hd) hd.onclick = hideExplain;
  }

  function nextHint() {
    var id = seq[pos], q = qIndex[id].q, s = st(id);
    s.hints = Math.min((s.hints || 0) + 1, hintsOf(q).length); save();
    paintState(id, q, s);
  }

  function explain() {
    var id = seq[pos], q = qIndex[id].q, s = st(id);
    if (!(s.done && s.lastCorrect)) { s.revealed = true; s.peeked = true; }
    s.explainOpen = true; s.retrying = false; save();
    stopTimer();
    paintState(id, q, s);
    renderStats();
  }

  function hideExplain() {
    var id = seq[pos], q = qIndex[id].q, s = st(id);
    s.explainOpen = false;
    if (!(s.done && s.lastCorrect)) s.retrying = true;
    save();
    show();
  }

  function pick(i) {
    var id = seq[pos], q = qIndex[id].q, s = st(id);
    if (isLocked(s) || showsExplain(s)) return;
    var b0 = document.querySelector('.opt[data-i="' + i + '"]');
    if (!b0 || b0.disabled) return;
    picked = i;
    Array.prototype.forEach.call(document.querySelectorAll(".opt"), function (b) {
      b.classList.toggle("picked", Number(b.getAttribute("data-i")) === i);
    });
    document.getElementById("checkBtn").disabled = false;
  }

  function doCheck() {
    var id = seq[pos], info = qIndex[id], q = info.q, s = st(id);
    if (isLocked(s) || showsExplain(s)) return;
    var given, ok;
    if (q.type === "MCQ") {
      if (picked === null) return;
      given = picked; ok = picked === q.ans;
    } else {
      var v = document.getElementById("titaIn").value;
      if (v.trim() === "") return;
      given = v.trim(); ok = titaMatch(v, q.ans);
    }
    if (!s.done) { s.firstCorrect = ok; s.firstAnswer = given; }
    s.done = true; s.retrying = false;
    s.lastCorrect = ok; s.lastAnswer = given;
    s.tries = (s.tries || 0) + 1;
    if (ok) { stopTimer(); if (!s.peeked) s.solved = true; }
    save();
    picked = null;
    paintState(id, q, s);
    if (!ok && q.type === "TITA") { var inp = document.getElementById("titaIn"); try { inp.focus(); inp.select(); } catch (e) {} }
    renderStats();
  }

  function retry() {
    var s = st(seq[pos]);
    s.retrying = true; s.explainOpen = false; save();
    show();
  }
  function toggleFlag() {
    var id = seq[pos], s = st(id);
    s.flag = !s.flag; save();
    var b = document.getElementById("flagBtn");
    b.classList.toggle("on", s.flag);
    b.textContent = s.flag ? "Flagged" : "Flag";
  }

  function go(d) {
    var n = pos + d;
    if (n < 0 || n >= seq.length) return;
    stopTimer();
    var prevUnit = qIndex[seq[pos]].unit;
    var cs = store.q[seq[pos]];
    if (cs && cs.retrying) { cs.retrying = false; save(); }
    pos = n;
    show();
    var qp = document.querySelector(".qpart");
    if (qIndex[seq[pos]].unit === prevUnit && qp && window.innerWidth <= 820) {
      qp.scrollIntoView({ block: "start" });
    } else {
      window.scrollTo(0, 0);
    }
  }

  // ---------- filters ----------
  function initFilters() {
    var years = {};
    DATA.units.forEach(function (u) { years[u.year] = 1; });
    var ys = document.getElementById("yearSel");
    Object.keys(years).sort().reverse().forEach(function (y) {
      var o = document.createElement("option"); o.value = y; o.textContent = y; ys.appendChild(o);
    });
    var f = store.filters;
    ys.value = f.year;
    document.getElementById("modeSel").value = f.mode;
    Array.prototype.forEach.call(document.querySelectorAll(".chip"), function (c) {
      var sec = c.getAttribute("data-sec");
      c.classList.toggle("on", f.secs.indexOf(sec) >= 0);
      c.onclick = function () {
        var i = f.secs.indexOf(sec);
        if (i >= 0) { if (f.secs.length === 1) return; f.secs.splice(i, 1); }
        else f.secs.push(sec);
        c.classList.toggle("on", f.secs.indexOf(sec) >= 0);
        refilter();
      };
    });
    ys.onchange = function () { f.year = ys.value; refilter(); };
    document.getElementById("modeSel").onchange = function () { f.mode = this.value; refilter(); };
    document.getElementById("shuffleBtn").onclick = function () {
      stopTimer();
      store.order = shuffle(store.order); save();
      buildSeq(null); show();
    };
  }
  function refilter() {
    stopTimer(); save();
    buildSeq(seq[pos]); show();
  }

  // ---------- theme ----------
  function applyTheme() {
    if (store.theme) document.documentElement.setAttribute("data-theme", store.theme);
    else document.documentElement.removeAttribute("data-theme");
  }
  document.getElementById("themeBtn").onclick = function () {
    var dark = store.theme ? store.theme === "dark" : window.matchMedia("(prefers-color-scheme: dark)").matches;
    store.theme = dark ? "light" : "dark"; save(); applyTheme();
  };

  // ---------- reset ----------
  var resetArmed = false;
  document.getElementById("resetBtn").onclick = function () {
    var b = this;
    if (!resetArmed) {
      resetArmed = true; b.textContent = "Tap again to erase all progress";
      setTimeout(function () { resetArmed = false; b.textContent = "Reset progress"; }, 4000);
      return;
    }
    stopTimer();
    store.q = {}; store.order = shuffle(store.order); save();
    resetArmed = false; b.textContent = "Reset progress";
    buildSeq(null); show();
  };

  // ---------- keys ----------
  document.addEventListener("keydown", function (e) {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    var t = e.target;
    var typing = t && (t.tagName === "INPUT" || t.tagName === "SELECT" || t.tagName === "TEXTAREA");
    if (e.key === "ArrowRight" && !typing) { go(1); return; }
    if (e.key === "ArrowLeft" && !typing) { go(-1); return; }
    if (typing) return;
    var k = e.key.toUpperCase();
    var id = seq[pos]; if (!id) return;
    var q = qIndex[id].q;
    if (q.type === "MCQ") {
      var i = LETTERS.indexOf(k);
      if (i < 0 && /^[1-4]$/.test(k)) i = Number(k) - 1;
      if (i >= 0 && i < q.opts.length) { pick(i); return; }
    }
    if (e.key === "Enter") { doCheck(); return; }
    if (k === "F") toggleFlag();
  });

  document.getElementById("prevBtn").onclick = function () { go(-1); };
  document.getElementById("nextBtn").onclick = function () { go(1); };

  applyTheme();
  initFilters();
  buildSeq(store.cur);
  show();
})();

/* Tap a chart or diagram to see it full size */
(function () {
  var box = document.createElement("div");
  box.className = "zoom";
  box.hidden = true;
  box.setAttribute("role", "dialog");
  box.setAttribute("aria-label", "Figure, full size");
  box.innerHTML = '<button class="zoom-close" aria-label="Close">&times;</button><div class="zoom-inner"><img alt=""></div>';
  document.body.appendChild(box);
  var big = box.querySelector("img");
  function close() { box.hidden = true; big.removeAttribute("src"); document.body.classList.remove("zoomed"); }
  document.addEventListener("click", function (e) {
    var t = e.target;
    if (t.tagName === "IMG" && t.closest(".passage, .qtext")) {
      big.src = t.getAttribute("src");
      big.alt = t.alt || "";
      box.hidden = false;
      document.body.classList.add("zoomed");
    } else if (!box.hidden && (t === box || t.classList.contains("zoom-close") || t.classList.contains("zoom-inner"))) {
      close();
    }
  });
  document.addEventListener("keydown", function (e) {
    if (!box.hidden) { e.stopPropagation(); if (e.key === "Escape") close(); }
  }, true);
})();
