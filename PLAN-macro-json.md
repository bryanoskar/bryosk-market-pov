# Plan A Tier 1 — Macro JSON (single source of truth)

**Goal:** stop hard-typing macro values in 15+ places across `index.html`. Keep them in ONE file (`macro.json`), render from there. Eliminates the recurring staleness/contradiction bugs (e.g. the 27 Jun WTI "$97 vs $92" contradiction).

**Status:** Step 1 + 2 DONE (2026-06-27). Steps 3–4 remain — do them in a focused daytime session.

---

## ✅ Step 1 — DONE: `macro.json` created
Single file holding every macro indicator. Each value carries:
- `label` — display name
- `value` — current value (string, e.g. "4.52%")
- `delta` — change note (e.g. "−3bps", "unchanged")
- `note` — one-line context
- `source` — `{ provider, series }` = the FRED / Trading Economics endpoint it will auto-fetch from in Tier 2. **This pre-maps Tier 2, so half that work is already done.**

This file is currently INERT — nothing reads it yet, so the live site is unaffected. Zero risk.

## ✅ Step 2 — DONE: this plan document

---

## ⬜ Step 3 — Wire `index.html` to render FROM macro.json (the consequential step)
This touches live render logic — do it carefully, test before publish.

1. In the render engine (`<script>` section of `index.html`), add a fetch at startup:
   ```js
   let MACRO = null;
   fetch('macro.json').then(r=>r.json()).then(d=>{ MACRO = d; renderMacro(); }).catch(()=>{ /* leave hard-coded fallback visible */ });
   ```
   **Important:** GitHub Pages serves `macro.json` same-origin, so fetch works. Keep the existing hard-typed values as a fallback if the fetch fails (don't blank the page).

2. Add a `renderMacro()` that injects values into the spots that currently hard-code them. Candidate spots (search these in index.html):
   - `techMacro[]` array (Macro tab technicals) — 10Y, WTI, DXY, USD/IDR, Gold
   - `snapshot[]` rows — 10Y UST, Gold, WTI, USD/IDR
   - Any inline mention of BI rate / Fed funds / CPI in bottomLine, news, corp
   - Add an "as of {macro.asOf}" stamp on the Macro tab so readers see freshness

3. Decide the rendering approach (pick one, document choice):
   - **(a) Data-attribute injection** — put `<span data-macro="us10y">` placeholders, fill from JSON. Cleanest, but requires editing the HTML spots to placeholders.
   - **(b) Keep arrays, source their values from MACRO** — e.g. `techMacro` becomes a function that reads MACRO. Less HTML churn.
   - Recommendation: (b) for the structured arrays (techMacro, snapshot), (a) for inline prose mentions.

## ⬜ Step 4 — Test + publish
- Open locally, confirm every macro value renders from JSON, fallback works if `macro.json` renamed temporarily.
- Confirm "as of" stamp shows.
- Publish (cp to repo + skill template, commit, push).
- Then daily macro refresh = edit `macro.json` only (1 file), never hunt through index.html again.

---

## ➡️ Tier 2 (LATER) — auto-fetch via GitHub Actions
Once Tier 1 renders from the file, a daily cron fills `macro.json` automatically:
- FRED API (free, unlimited) for US series: DGS10, FEDFUNDS, CPIAUCSL, PCEPI, DCOILWTICO, DTWEXBGS
  - Bryan action (~5 min): get free key at fred.stlouisfed.org/docs/api → add GitHub secret `FRED_API_KEY`
- Trading Economics for Indonesia: indonesia/interest-rate, indonesia/currency
  - Bryan action: signup + key → add secret `TE_API_KEY` (verify current free-tier limits first)
- Gold: no clean free daily series — keep manual or add a market-data API in a later tier.

The `source` field in each macro.json value already names the exact series to fetch — Tier 2 just loops over them.
