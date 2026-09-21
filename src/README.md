# Simple Price-Spread Viewer

This folder contains a small standalone Python example illustrating one of the
basic ideas used in pair analysis: monitoring the **relative price spread**
between two instruments.

It is provided as a simple educational example and is **not the production
PairMonitor model or signal engine**.

## What It Does

The script allows you to enter two US stock or ETF tickers and then:

- downloads recent hourly price data using `yfinance`,
- plots both instruments on separate price axes,
- calculates the log-price spread between them,
- normalizes the spread using a rolling Z-score,
- and displays the spread as a bar chart below the prices.

Bars become more prominent when the spread moves beyond the preset extreme
level of **±2 Z-score units**, making unusual relative-price conditions easier
to identify visually.

The simplified calculation is:

```text
Log Spread
= log(Target Price) - log(Comparison Price)

              Log Spread - Rolling Mean
Z-Score =  --------------------------------
                 Rolling Std. Dev.
