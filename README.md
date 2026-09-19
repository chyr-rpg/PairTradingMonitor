# PairMonitor

**A relative-value research and signal-monitoring system using unsupervised learning and statistical pair analysis across US stocks and ETFs, delivered through Telegram.**

> 🧪 **Limited Trial Access:** [Open PairResearchBot](https://t.me/PairResearchBot)
>
> PairMonitor is currently in a limited trial stage. Access may be granted temporarily while the system is being evaluated ahead of a broader commercial release.

---

## What is PairMonitor?

PairMonitor monitors relationships between US stocks, sector ETFs and broad-market ETFs such as SPY, QQQ and DIA.

Instead of analysing a stock only through its own price history, PairMonitor asks a relative question:

> **Is this stock behaving unusually compared with instruments that have historically shown meaningful relationships with it?**

The system evaluates pair relationships after newly closed hourly bars and highlights statistically unusual divergence, convergence and relative-momentum conditions.

The objective is not to tell users what to buy or sell.

It is to surface **relative-price behaviour that may deserve further investigation**.

---

## Why I Built It

PairMonitor is a **personal, independently developed quantitative research project**.

One of the original research questions behind the project were:

> **To what extent can unsupervised clustering help identify useful instruments for pair and relative-value research?**
> **To what extent can residual spread and price spread based statistical models help identify opportunties from relative price valuation?** 

Selecting a good comparison instrument is not always obvious.

Two companies may belong to the same sector but behave very differently, while instruments from different classifications may still exhibit useful statistical relationships.

PairMonitor therefore explores a two-stage idea:

```text
Market Universe
      ↓
Feature Construction
      ↓
Unsupervised Clustering
      ↓
Comparable-Instrument Candidates
      ↓
Pair-Level Statistical Analysis
      ↓
Signal & Context Monitoring
```

Clustering is used as a **candidate-selection mechanism**, not as proof that two instruments form a good trading pair.

The broader research challenge is to determine which candidate relationships remain statistically meaningful enough to provide useful relative-price context.

---

## What Makes a Useful Pair?

PairMonitor does not assume that two instruments form a useful pair simply because they appear in the same cluster.

Candidate relationships can also be evaluated through characteristics such as:

```text
Historical Co-Movement
Relative-Price Stability
Residual Behaviour
Correlation
Mean-Reversion Characteristics
Signal Consistency
Market / Sector Relationship
and Data Availability
```

A statistically related pair is not necessarily a profitable trading opportunity.

Relationships can also weaken, change or disappear as market conditions evolve.

For this reason, PairMonitor is designed primarily as a **research and monitoring system**, rather than as an automatic pair-trading execution engine.

---

## Why Market Researchers and Analysts May Find It Useful

- **Objective and systematic.** Alerts are generated from repeatable statistical rules rather than discretionary chart interpretation, providing an independent input that can be compared with an existing market view.

- **Unsupervised pair discovery.** Clustering helps narrow a large market universe into potentially relevant comparison candidates for selected target stocks.

- **Relative-value perspective.** Pair analysis can help separate broad market movement from behaviour that appears unusual relative to a sector, ETF or comparable instrument.

- **Two analytical engines.** A Residual-spread model and an optional Price-spread model evaluate the same relationship independently. Agreement or disagreement between the two can itself provide additional research context.

- **Continuous monitoring.** Relationships are re-evaluated after newly closed hourly bars so users do not need to manually monitor every pair.

- **Context rather than labels alone.** Alerts include model scores and charts so users can inspect the underlying relationship rather than relying only on a text signal.

---

## What Does a PairMonitor Signal Mean?

A PairMonitor signal means that the relationship between two instruments has reached a condition identified by one of the system's statistical models.

It does **not** mean:

```text
Guaranteed Mispricing
Guaranteed Mean Reversion
Guaranteed Direction
Automatic Buy / Sell Recommendation
or Guaranteed Profit
```

A signal is better interpreted as:

> **Something statistically unusual is happening in this relative-price relationship and may be worth investigating.**

Signals are intended to complement broader market, fundamental and risk analysis.

---

## What You Can Do With It

| Command | What it does |
|---|---|
| `/watchlist` | See and manage the stocks/ETFs you're following |
| `/setlist`, `/addstock`, `/removestock` | Build your personal watchlist |
| `/coverage`, `/coverage etf` | Browse supported stocks and ETFs |
| `/context TICKER` | View the current relative-value context for a target across its comparison pairs |
| `/pair TARGET COMPONENT` | Inspect one specific pair on demand, including its chart |
| `/addpair TARGET COMPONENT` | Follow a custom pair you're personally interested in |
| `/tracked`, `/untrack` | Manage the pairs you're actively following |
| `/priceon`, `/priceoff` | Enable or disable the secondary Price-spread model |

Automatic alerts and `/context` / `/pair` responses include charts so the underlying relationship can be inspected visually.

---

## Coverage

Current coverage focuses on approximately **100 large US stocks** across major sectors, together with broad-market and sector ETFs including:

```text
SPY
QQQ
DIA
XLK
XLF
XLE
XLV
and others
```

Extended-session market data is incorporated where supported so that relative-price changes outside the regular trading session can also contribute to the analysis.

Coverage may continue to expand as the research and infrastructure develop.

---

## Project Status

PairMonitor is currently operating in a **limited trial stage**.

The project is not intended to remain a permanently free public service.

Trial access is currently being used to evaluate:

```text
Signal Quality
User Experience
Pair Selection
Infrastructure Requirements
Alert Reliability
and User Feedback
```

A paid subscription model is planned following the trial stage.

Final plan features, pricing and access terms will be published through the official PairMonitor subscription page when the commercial service launches.

Early trial users and founding subscribers may receive separate launch terms.

---

## Infrastructure & Availability

PairMonitor is independently operated on **lightweight cloud infrastructure** during its current trial stage.

Because the project is still being actively developed:

- response times may occasionally vary,
- development or maintenance may temporarily interrupt service,
- coverage and processing schedules may change,
- and Telegram delivery should not be interpreted as guaranteed real-time infrastructure.

There is currently no service-level agreement or guaranteed uptime.

Infrastructure will be expanded progressively as usage and product requirements increase.

---

## Current Research Areas

PairMonitor remains an active research project.

Current areas of development include:

```text
Clustering & Pair Candidate Selection
Relative-Price Modelling
Residual Analysis
Signal Quality Scoring
Multi-Timeframe Context
Alert Filtering
Historical Signal Evaluation
Pair Stability
and Infrastructure Reliability
```

Not every experimental feature is necessarily enabled in the Telegram bot, and the methodology may evolve as additional testing is completed.

---

## Getting Started

1. Open the bot: **[t.me/PairResearchBot](https://t.me/PairResearchBot)**
2. Send the bot a message to receive the current introduction and access information.
3. Once trial access is enabled, use `/setlist` to configure your research watchlist.
4. Use `/context TICKER` or `/pair TARGET COMPONENT` to explore relationships directly.

### Trial Access

PairMonitor is currently available only through **limited trial access**.

The trial is intended to allow selected users to experience the system while signal behaviour, usability and infrastructure continue to be evaluated.

The bot should not be interpreted as a permanently free service.

Future access, subscription plans, supported coverage and features may change as the project develops.

---

## Development Philosophy

The project continues to investigate:

> **Can data-driven pair selection identify relationships that provide useful market context?**

and:

> **What characteristics distinguish a genuinely useful research pair from two instruments that merely happened to move together historically?**

The Telegram bot is the practical layer built around those questions: continuously monitoring selected relationships and making the resulting analysis easier to consume.

---

## Disclaimer

PairMonitor provides systematic, model-generated information for **market research and educational purposes only**.

Nothing generated by the system constitutes financial advice, a recommendation to buy or sell any security, or a representation of future investment performance.

Statistical relationships can weaken or fail, and historical signal behaviour does not guarantee future results.

Users should independently evaluate any market information before making investment decisions.
