"""Price-Spread Pair Trading Viewer -- standalone desktop tool.

Opens a panel with two ticker inputs (target stock, compared stock) and a
Plot button. On click, downloads each stock's recent hourly price history,
plots both prices together (target on the left axis, compared stock on an
independent right axis -- so the two are readable regardless of how
different their price scales are), and renders the price spread between
them as a plain green/red bar subplot underneath. Deliberately unlabeled:
no signal names, no score values, no legend calling it anything -- just
the bars.

Fully standalone. Does not import or depend on any other project in this
environment.

Install (one time):
    pip install yfinance pandas numpy matplotlib

Run:
    python pair_spread_viewer.py
"""
from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

try:
    import yfinance as yf
except ImportError as exc:  # pragma: no cover - environment setup issue, not a code bug
    raise SystemExit(
        "This tool requires yfinance. Install with: pip install yfinance"
    ) from exc

INTERVAL = "1h"
LOOKBACK_DAYS = 90  # yfinance allows up to 730 days of 1h data; 90 keeps fetch/plot snappy
SPREAD_WINDOW = 20  # bars used for the rolling mean/std that normalizes the spread


def fetch_price_series(ticker: str) -> pd.Series:
    """Downloads recent closing prices for one ticker. Raises ValueError
    with a plain-English message on an empty/invalid result rather than
    letting a confusing yfinance/pandas error surface to the user."""
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=LOOKBACK_DAYS)
    data = yf.download(
        ticker, start=start, end=end, interval=INTERVAL,
        progress=False, auto_adjust=True)
    if data is None or data.empty:
        raise ValueError(f"No data returned for '{ticker}'. Check the ticker symbol.")
    close = data["Close"]
    if isinstance(close, pd.DataFrame):  # yfinance can return a 1-column frame
        close = close.iloc[:, 0]
    close = close.dropna()
    if close.empty:
        raise ValueError(f"No usable price data for '{ticker}'.")
    close.name = ticker.upper()
    return close


def compute_price_spread(target: pd.Series, compared: pd.Series, window: int = SPREAD_WINDOW) -> pd.Series:
    """Log-price spread between the two series, normalized to a rolling
    Z-score -- the standard price-spread pair-trading measure. Positive
    means the target is relatively expensive vs. the compared stock over
    the lookback window; negative means relatively cheap. Returned purely
    as a numeric series -- the caller decides how (or whether) to label it."""
    aligned = pd.concat([target, compared], axis=1, join="inner").dropna()
    if aligned.empty:
        raise ValueError("The two tickers have no overlapping price history.")
    log_spread = np.log(aligned.iloc[:, 0]) - np.log(aligned.iloc[:, 1])
    rolling_mean = log_spread.rolling(window, min_periods=window).mean()
    rolling_std = log_spread.rolling(window, min_periods=window).std(ddof=0)
    z = (log_spread - rolling_mean) / rolling_std.replace(0, np.nan)
    z = z.dropna()
    if z.empty:
        raise ValueError(
            f"Not enough overlapping bars to compute a {window}-bar spread. "
            "Try a more actively traded pair.")
    return z


def _sparse_date_ticks(index: pd.DatetimeIndex, count: int = 8) -> tuple[list[int], list[str]]:
    """Evenly spaced x tick positions/labels for a numeric bar index --
    avoids datetime-bar-width plotting issues entirely by keeping both
    subplots on plain integer positions."""
    n = len(index)
    if n == 0:
        return [], []
    step = max(1, n // count)
    positions = list(range(0, n, step))
    labels = [index[i].strftime("%m-%d %H:%M") for i in positions]
    return positions, labels


class PairSpreadApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Price-Spread Pair Viewer")
        self.geometry("1150x780")

        controls = ttk.Frame(self, padding=10)
        controls.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(controls, text="Target stock:").pack(side=tk.LEFT, padx=(0, 4))
        self.target_entry = ttk.Entry(controls, width=10)
        self.target_entry.pack(side=tk.LEFT, padx=(0, 16))

        ttk.Label(controls, text="Compared stock:").pack(side=tk.LEFT, padx=(0, 4))
        self.compared_entry = ttk.Entry(controls, width=10)
        self.compared_entry.pack(side=tk.LEFT, padx=(0, 16))

        self.plot_button = ttk.Button(controls, text="Plot", command=self.on_plot)
        self.plot_button.pack(side=tk.LEFT)

        self.status_var = tk.StringVar(value="Enter two tickers and click Plot.")
        ttk.Label(self, textvariable=self.status_var, padding=(10, 4)).pack(side=tk.TOP, fill=tk.X)

        self.figure = Figure(figsize=(11.5, 7.3), dpi=100)
        self.price_ax = self.figure.add_axes((0.08, 0.32, 0.86, 0.62))
        self.spread_ax = self.figure.add_axes((0.08, 0.08, 0.86, 0.18))
        self.price_ax2 = self.price_ax.twinx()

        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.target_entry.bind("<Return>", lambda _event: self.on_plot())
        self.compared_entry.bind("<Return>", lambda _event: self.on_plot())

    def on_plot(self) -> None:
        target = self.target_entry.get().strip().upper()
        compared = self.compared_entry.get().strip().upper()
        if not target or not compared:
            messagebox.showwarning("Missing input", "Enter both a target and a compared stock ticker.")
            return
        if target == compared:
            messagebox.showwarning("Invalid input", "Target and compared stock must be different.")
            return

        self.status_var.set(f"Loading {target} and {compared} ...")
        self.plot_button.state(["disabled"])
        self.update_idletasks()
        try:
            target_series = fetch_price_series(target)
            compared_series = fetch_price_series(compared)
            spread = compute_price_spread(target_series, compared_series)
            self._draw(target_series, compared_series, spread, target, compared)
            self.status_var.set(f"{target} vs {compared} -- {len(spread)} bars")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))
            self.status_var.set("Failed to plot. See error message.")
        finally:
            self.plot_button.state(["!disabled"])

    def _draw(
        self, target_series: pd.Series, compared_series: pd.Series, spread: pd.Series,
        target_name: str, compared_name: str,
    ) -> None:
        self.price_ax.clear()
        self.price_ax2.clear()
        self.spread_ax.clear()

        common_index = spread.index
        target_plot = target_series.reindex(common_index)
        compared_plot = compared_series.reindex(common_index)
        x = np.arange(len(common_index))

        self.price_ax.plot(x, target_plot.values, color="#1f77b4", linewidth=1.4, label=target_name)
        self.price_ax2.plot(x, compared_plot.values, color="#d62728", linewidth=1.1, label=compared_name)
        self.price_ax.set_ylabel(target_name, color="#1f77b4")
        self.price_ax2.set_ylabel(compared_name, color="#d62728")
        self.price_ax.tick_params(axis="y", labelcolor="#1f77b4")
        self.price_ax2.tick_params(axis="y", labelcolor="#d62728")
        self.price_ax.grid(True, alpha=0.3)
        lines1, labels1 = self.price_ax.get_legend_handles_labels()
        lines2, labels2 = self.price_ax2.get_legend_handles_labels()
        self.price_ax.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=9)

        colors = np.where(spread.values >= 0, "#2ca02c", "#d62728")
        self.spread_ax.bar(x, spread.values, color=colors, width=0.9)
        self.spread_ax.axhline(0, color="black", linewidth=0.7)
        self.spread_ax.set_yticks([])

        tick_positions, tick_labels = _sparse_date_ticks(common_index)
        self.spread_ax.set_xticks(tick_positions)
        self.spread_ax.set_xticklabels(tick_labels, rotation=30, ha="right", fontsize=8)
        self.price_ax.set_xticks(tick_positions)
        self.price_ax.set_xticklabels([])  # dates only on the bottom subplot
        self.price_ax.set_xlim(-1, len(common_index))
        self.spread_ax.set_xlim(-1, len(common_index))

        self.canvas.draw()


def main() -> None:
    app = PairSpreadApp()
    app.mainloop()


if __name__ == "__main__":
    main()
