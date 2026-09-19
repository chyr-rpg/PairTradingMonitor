# FAQ

**Is this financial advice?**
No. PairMonitor is a research and monitoring system that surfaces
statistically unusual relative-price behaviour between related instruments —
it does not tell you what to buy or sell, and a signal is not a guarantee of
mispricing, mean reversion, direction, or profit. See the full
[Disclaimer](README.md#disclaimer) and [What Does a PairMonitor Signal Mean?](README.md#what-does-a-pairmonitor-signal-mean)
sections in the README.

**What does PairMonitor actually compare?**
Pairs of related US stocks and ETFs — a stock against comparison instruments
identified through unsupervised clustering (sector peers, broad-market or
sector ETFs like SPY/QQQ/DIA, or statistically related instruments that
aren't obvious from sector labels alone), or any two covered instruments you
choose to follow yourself with `/addpair`. See real examples in
[sample_screenshots](sample_screenshots/).

**Why clustering instead of just sector groupings?**
Two companies in the same sector can behave very differently, while
instruments from different classifications can still move together in a
statistically meaningful way. Clustering is used only as a candidate-
selection step — it narrows the universe down to plausible comparison
instruments, not proof that a pair is tradeable. Every candidate is then
evaluated on its own statistical characteristics (co-movement, residual
behaviour, mean-reversion tendencies, signal consistency, and more) before
it's treated as a monitored pair.

**How often do alerts fire?**
Relationships are re-evaluated after every newly closed hourly bar,
including extended trading-session data — but an alert only fires when a
condition actually confirms, not on a fixed schedule. Quiet periods are
normal; they mean nothing new has confirmed, not that anything is broken.

**What markets/instruments are covered?**
Currently around 100 large US stocks across major sectors, plus broad-market
and sector ETFs (SPY, QQQ, DIA, XLK, XLF, XLE, XLV, and others). Run
`/coverage` or `/coverage etf` inside the bot any time for the current list —
coverage is expected to expand as the project develops.

**What's the difference between the Residual and Price models?**
Residual is the default engine and evaluates the statistical spread between
two instruments after accounting for their historical relationship. Price is
an optional secondary model based on relative price behaviour instead. You
can enable Price alongside Residual with `/priceon` (and disable it with
`/priceoff`) — agreement or disagreement between the two engines is itself
useful research context.

**Is this a free service?**
No — PairMonitor is currently in a limited trial stage, not a permanent free
service. A paid subscription model is planned once the trial concludes; full
pricing and plan details will be published separately when that happens.
Trial access may be granted temporarily while the system is evaluated, and
there's no guaranteed uptime or SLA during this stage. See
[Project Status](README.md#project-status) and
[Infrastructure & Availability](README.md#infrastructure--availability) in
the README for the current details.

**How do I get access?**
Message the bot — [t.me/PairResearchBot](https://t.me/PairResearchBot) — to
receive the current introduction and access information.

**Where does the price data come from?**
Established market-data providers, refreshed continuously through the
trading session, including extended-session data where supported.

**Can I follow a custom pair that isn't in the default coverage?**
Yes — `/addpair TARGET COMPONENT` lets you follow any two covered
instruments together, with a preview chart before you commit.

**Is my data/watchlist private?**
Your watchlist and tracked pairs are tied to your own Telegram account and
are not shared with other users.

**I have a question that's not answered here.**
Message the bot directly — [t.me/PairResearchBot](https://t.me/PairResearchBot).
