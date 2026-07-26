#!/usr/bin/env python3
"""
Refresh the PERF5Y snapshot inside simulator.html.

Fetches 5 years of MONTHLY closes from Yahoo Finance for the S&P 500 (^GSPC),
the Jakarta Composite / IHSG (^JKSE), Bitcoin (BTC-USD) and Ethereum (ETH-USD),
computes each series' 5Y price CAGR and annualized volatility, adds a fixed
dividend-yield estimate to the two equity indices to approximate total return,
and rewrites the `const PERF5Y={...}` object in ../simulator.html.

Safety: if ANY series fails to fetch or produces an out-of-range figure, the
script aborts WITHOUT touching simulator.html (never corrupts the live file).

Run manually:  python scripts/refresh_perf5y.py
Scheduled monthly by the "refresh-simulator-5y" task.
"""
import json, urllib.request, urllib.parse, re, math, sys, os, datetime

# (yahoo symbol, PERF5Y key, dividend-yield add-on % for total return)
CONFIG = [("^GSPC", "sp500", 1.4), ("^JKSE", "ihsg", 3.8),
          ("BTC-USD", "btc", 0.0), ("ETH-USD", "eth", 0.0)]
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.join(HERE, "..", "simulator.html")

def fetch(sym):
    url = "https://query1.finance.yahoo.com/v8/finance/chart/" + urllib.parse.quote(sym) + "?range=5y&interval=1mo"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    res = data["chart"]["result"][0]
    ts = res["timestamp"]
    adj = None
    ind = res.get("indicators", {})
    if ind.get("adjclose"):
        adj = ind["adjclose"][0].get("adjclose")
    if not adj:
        adj = ind["quote"][0].get("close")
    pairs = [(t, p) for t, p in zip(ts, adj) if p is not None]
    # drop a trailing duplicate (Yahoo repeats the in-progress month)
    if len(pairs) >= 2 and abs(pairs[-1][1] - pairs[-2][1]) < 1e-9:
        pairs = pairs[:-1]
    return pairs

def compute(pairs):
    p = [x[1] for x in pairs]
    n = len(p)
    years = (n - 1) / 12.0
    cagr = (p[-1] / p[0]) ** (1.0 / years) - 1.0
    rets = [math.log(p[i] / p[i - 1]) for i in range(1, n)]
    m = sum(rets) / len(rets)
    sd = math.sqrt(sum((x - m) ** 2 for x in rets) / len(rets))
    return {"n": n, "cagr": cagr * 100.0, "vol": sd * math.sqrt(12) * 100.0,
            "first": pairs[0][0], "last": pairs[-1][0]}

def main():
    out = {}
    window_first = window_last = None
    for sym, key, div in CONFIG:
        try:
            s = compute(fetch(sym))
        except Exception as e:
            print("ABORT: fetch/compute failed for %s: %s" % (sym, e)); return 1
        if not (s["n"] >= 48 and -60 < s["cagr"] < 300 and 0 < s["vol"] < 250):
            print("ABORT: sanity check failed for %s: %r" % (sym, s)); return 1
        out[key] = {"ret": round(s["cagr"] + div, 1), "vol": round(s["vol"], 1),
                    "priceCagr": round(s["cagr"], 1), "div": div}
        if key == "sp500":
            window_first, window_last = s["first"], s["last"]
        print("  %-6s ret=%.1f  vol=%.1f  (priceCAGR=%.1f + div=%.1f)  n=%d"
              % (key, out[key]["ret"], out[key]["vol"], out[key]["priceCagr"], div, s["n"]))

    as_of = datetime.datetime.now().strftime("%b %Y")
    w0 = datetime.datetime.fromtimestamp(window_first, datetime.timezone.utc).strftime("%b %Y")
    w1 = datetime.datetime.fromtimestamp(window_last, datetime.timezone.utc).strftime("%b %Y")
    block = (
        "const PERF5Y={\n"
        '  asOf:"%s", window:"%s–%s",\n' % (as_of, w0, w1) +
        "  sp500:{ret:%.1f, vol:%.1f, priceCagr:%.1f, div:1.4},   // total return = harga + est. dividen\n" % (out["sp500"]["ret"], out["sp500"]["vol"], out["sp500"]["priceCagr"]) +
        "  ihsg:{ret:%.1f,  vol:%.1f, priceCagr:%.1f,  div:3.8},\n" % (out["ihsg"]["ret"], out["ihsg"]["vol"], out["ihsg"]["priceCagr"]) +
        "  btc:{ret:%.1f,   vol:%.1f},                              // CAGR harga 5Y\n" % (out["btc"]["ret"], out["btc"]["vol"]) +
        "  eth:{ret:%.1f, vol:%.1f}\n" % (out["eth"]["ret"], out["eth"]["vol"]) +
        "};"
    )

    with open(TARGET, "r", encoding="utf-8") as f:
        html = f.read()
    if "const PERF5Y={" not in html:
        print("ABORT: PERF5Y block not found in simulator.html"); return 1
    new_html = re.sub(r"const PERF5Y=\{.*?\n\};", block, html, count=1, flags=re.DOTALL)
    if new_html == html:
        print("No change (numbers identical)."); return 0
    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Updated PERF5Y -> asOf %s (%s-%s)" % (as_of, w0, w1))
    return 0

if __name__ == "__main__":
    sys.exit(main())
