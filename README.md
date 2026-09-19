# PairMonitor

**A pair-trading signal bot using unsupervised learning and statistical research for relative-price analysis on US stocks and ETFs, delivered straight to Telegram.**

> 👉 **Try it now: [t.me/PairResearchBot](https://t.me/PairResearchBot)**

---

## What is PairMonitor?

PairMonitor watches relationships between US stocks, sector ETFs, and broad-market ETFs (SPY, QQQ, DIA, and the sector SPDRs) and alerts you the moment two related instruments drift apart or converge in a statistically meaningful way — the same relative-value idea professional pair traders and market-neutral desks use, delivered automatically to your phone.

Instead of tracking a stock's price in isolation, PairMonitor asks a more useful question: **"Is this stock relatively cheap or expensive right now, compared to what it usually trades like versus its peers and the broader market?"**

## Why market researchers and analysts use it

- **Objective and systematic.** Every alert comes from a rules-based statistical model, not discretionary chart-reading — useful as an independent, repeatable signal to cross-check your own thesis against.
- **Unsupervised machine learning.** Clustering is used to select price pairs for selected target stocks and rank most confidently relevant pairs for market research, price analysis and signal delivery.
- **Relative-value, market-neutral lens.** Pair analysis strips out broad market noise, surfacing moves that are specific to a stock relative to its sector or comparison instrument — a genuinely different angle from single-name technicals.
- **Two independent models, one view.** A Residual-spread engine and an optional Price-spread engine each score signals independently; seeing both agree (or disagree) is itself useful research signal.
- **Always watching, never tired.** Signals are evaluated every hour against freshly closed price bars — you get notified, you don't have to go looking.
- **Built-in context, not just an alert.** Every signal comes with a confidence/quality score and a chart, so you can judge it yourself rather than trusting a black box.

## What you can do with it

| Command | What it does |
|---|---|
| `/watchlist` | See and manage the stocks/ETFs you're following |
| `/setlist`, `/addstock`, `/removestock` | Build your personal watchlist |
| `/coverage`, `/coverage etf` | Browse every supported stock and ETF |
| `/context TICKER` | Get a full relative-value report for one target: every compared pair's latest signal, direction, and confidence, plus a chart |
| `/pair TARGET COMPONENT` | Inspect one specific pair on demand, with its chart |
| `/addpair TARGET COMPONENT` | Start following a custom pair you're personally interested in |
| `/tracked`, `/untrack` | Manage the pairs you're actively following |
| `/priceon`, `/priceoff` | Turn on the secondary Price-spread model alongside the default Residual model |

Every automatic alert and every `/context`/`/pair` response includes a chart, so you're never just trusting a text label.

## Coverage

US large/mid-cap stocks across major sectors, plus broad-market and sector ETFs (SPY, QQQ, DIA, XLK, XLF, XLE, XLV, and more) — extended trading-session data, so nothing is missed between the regular close and the next open.

## Getting started

1. Open the bot: **[t.me/PairResearchBot](https://t.me/PairResearchBot)**
2. Send it any message — you'll get a welcome guide back immediately.
3. Set your watchlist with `/setlist` and you're live.

Access is currently by invite/trial — message the bot to get started, and you may be granted a short trial period to see it in action.

---

*PairMonitor provides systematic, model-generated signals for market research and educational purposes only. Nothing it sends is financial advice or a recommendation to buy or sell any security. Past signal performance does not guarantee future results. Always do your own research and consult a licensed financial advisor before making investment decisions.*
