# What an alert actually looks like

Every automated signal and every on-demand `/pair` or `/context` reply follows
the same layout: a plain-English readout of the relationship, then the
numbers behind it, then a chart. Nothing here is copy-pasted marketing text —
this is the real shape of what lands in your Telegram chat.

## 🔔 A confirmed signal alert

> 🔔 **NVDA vs SMH — Bullish Divergence confirmed**
> 19 Sep 14:00 EDT (2 bars ago) · Residual engine
>
> NVDA $121.45 | SMH $248.10
>
> Z −2.31σ → −1.64σ (Δ +0.67σ) | Spread Δ +1.8% since entry
>
> Entry: NVDA $118.90 / SMH $246.30
>
> [chart attached as caption — 160 bars of NVDA vs SMH spread with the
> signal entry point marked]

**How to read it:** NVDA had drifted statistically cheap relative to its
semiconductor-ETF peer SMH — over 2 standard deviations below its normal
relationship — and has now started reverting back toward the mean. The alert
fires the moment that reversion is *confirmed*, not the moment it's merely
guessed at, and keeps showing you the live Z-score gap so you can see the
move continuing (or stalling) in real time.

## 🧩 An on-demand `/context TICKER` report

Send `/context NVDA` any time and you'll get a full snapshot across every
pair NVDA is compared against:

> 🧩 **NVDA detailed context**
> 🕒 Latest closed bar: 19 Sep 15:00 EDT
> Compared pairs: 6
>
> 📊 NVDA vs SMH — sector peer
>   Residual: Relatively Low · reverting ↗️ · 19 Sep 14:00 EDT · Q 78 · current Z −1.64
>   🔄 Previous opposite: Relatively High ↘️ · 15 Sep 10:00 EDT · Q 65
>
> 📊 NVDA vs QQQ — broad market
>   Residual: no confirmed signal
>
> *(one block like this per compared pair, then the chart as a follow-up message)*

**How to read it:** this is the "check in on a name whenever you want" view —
every relationship NVDA has, its current read, and its last time it flipped
the other way, so you can see whether today's move is fresh or has been
building.

## 📊 An on-demand `/pair TARGET COMPONENT` snapshot

Send `/pair NVDA SMH` for a deep dive into just that one relationship:

> 📊 **NVDA vs SMH — sector peer**
> NVDA $121.45 | SMH $248.10
> Residual: −1.64σ (12th pct) → NVDA Relatively Low vs SMH
> Regime: Mean-reverting ✅ (DF −3.1 vs crit −2.86, VR 0.42, HL 18 bars)
>
> Peer vote: 4/6 components suggest UNDERVALUED, 1/6 OVERVALUED
> Weighted bias: Moderately Undervalued (weighted score −0.58)
>
> Most tradable-regime signal: Bullish Divergence, 19 Sep 14:00 EDT (2 bars ago)
>   Z −2.31σ → −1.64σ (Δ +0.67σ)
>   Entry: NVDA $118.90 / SMH $246.30
>
> [chart attached as caption]

**How to read it:** the "regime" line tells you whether this pair is
currently behaving in a way that makes mean-reversion signals trustworthy at
all (some pairs drift and don't revert — the model tells you which state
you're in, not just the raw Z-score). The peer vote adds a second opinion:
how NVDA looks against *every* comparable name, not just this one.

---

*All figures above are illustrative examples built from the bot's real
message format — not a live trade recommendation. See the
[disclaimer](README.md) for details.*
