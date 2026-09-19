# FAQ

**Is this financial advice?**
No. PairMonitor sends systematic, model-generated statistical signals for
research and educational purposes. It is not a recommendation to buy or
sell anything, and it's not a substitute for your own research or a
licensed advisor. See the full disclaimer in the [README](README.md).

**What does PairMonitor actually compare?**
Pairs of related US stocks and ETFs — a stock against its sector peers,
a stock against a broad-market or sector ETF (SPY, QQQ, DIA, XLK, XLF, XLE,
XLV, and more), or any two instruments you choose to follow yourself with
`/addpair`. See a real example in [SAMPLE_ALERT.md](SAMPLE_ALERT.md).

**How often do alerts fire?**
Signals are evaluated every hour against freshly closed price bars,
including extended trading-session data — but an alert only fires when a
new signal actually confirms, not on a fixed schedule. Quiet periods with
no alerts are normal; it means nothing new has confirmed yet, not that
anything is broken.

**What markets/instruments are covered?**
US large/mid-cap stocks across major sectors, plus broad-market and sector
ETFs. Run `/coverage` or `/coverage etf` inside the bot any time for the
full, current list — it changes as coverage is extended, so that's always
more up to date than any static list here.

**What's the difference between the Residual and Price models?**
Residual is the default engine and looks at the statistical spread between
two instruments after accounting for their normal relationship. Price is an
optional secondary model that looks at simple relative price behavior
instead. You can turn Price on alongside Residual with `/priceon` (and back
off with `/priceoff`) to see both perspectives on the same pair — agreement
between the two is itself a useful signal.

**What does the confidence/quality (Q) score mean?**
Every signal comes with a Q score reflecting how strong and well-formed the
underlying statistical setup is — a low-Q signal firing is technically valid
but weaker evidence than a high-Q one. It's shown alongside every signal so
you can weigh it yourself rather than treating every alert as equal.

**Do I need to know anything about statistics or pair trading to use this?**
No. Every message is written in plain English with the numbers included for
anyone who wants to dig in, but the "Relatively Low / Relatively High" and
directional-arrow language is designed to be read at a glance.

**How much does it cost / how do I get access?**
Message the bot to get started — access is currently by invite, and you may
be granted a short trial period automatically. There's no self-serve pricing
page; just start a conversation with [@PairResearchBot](https://t.me/PairResearchBot).

**Where does the price data come from?**
Real-time and historical market data from established market-data providers,
refreshed continuously throughout the trading session.

**Can I follow a custom pair that isn't in the default coverage?**
Yes — `/addpair TARGET COMPONENT` lets you follow any two covered
instruments together, with a preview chart before you commit.

**Is my data/watchlist private?**
Your watchlist and tracked pairs are tied to your own Telegram account and
are not shared with other users.

**I have a question that's not answered here.**
Message the bot directly — [t.me/PairResearchBot](https://t.me/PairResearchBot).
