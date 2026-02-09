# Volatility Breakout Backtest (SPY)

A lightweight research repo that implements a volatility breakout signal, converts signals into fixed-horizon positions, and evaluates performance under transaction costs and regime filters.

This project is intentionally designed to be modular and readable, with feature engineering, signal generation, and backtesting separated into standalone Python modules.

# Project Overview

This strategy tests a simple hypothesis:
  Large daily ranges relative to recent volatility (ATR) may signal short-     term directional continuation.

The pipeline:
- Compute volatility proxy using rolling ATR (high–low range)
- Generate breakout signals when range exceeds k × ATR
- Convert signals into positions held for a fixed horizon
- Compute net strategy returns with proportional transaction costs
- Run diagnostics + robustness checks (high-volatility regimes)

#Repo Structure
src/
  features.py        # ATR + volatility features
  signals.py         # breakout signal logic
  backtest.py        # position construction + returns + costs
notebooks/
  01_backtest_pipeline.ipynb
  02_volatility_classifier.ipynb
data/
  spy_yahoo.csv
README.md

Note: notebooks are included for transparency and reproducibility.
Core logic is implemented in src/ so the pipeline can run end-to-end without notebooks.

# Results Summary (High Level)
The equity curve shows gradual decay with occasional positive spikes.

Key observations:
- Strategy returns are centered near zero with a heavy left tail
- Performance is strongly eroded by transaction costs and turnover
- Conditioning on high-volatility regimes changes trade frequency but does     not generate a persistent edge

This outcome is consistent with the broader empirical difficulty of extracting robust alpha from noisy short-horizon signals in liquid equity indices.

How to Run (End-to-End)
1) Setup
pip install numpy pandas matplotlib

2) Run the backtest

From repo root:

python -m src.backtest

Notes on Design Choices
- ATR is implemented as a rolling mean of daily range (High - Low) for         simplicity and transparency.
-Signals are directionally determined using the sign of the open–close move   on breakout days.
- Overlapping signals are aggregated linearly to reflect repeated exposure     during clustered breakouts.
- Transaction costs are modeled as proportional to turnover (|Δposition|).

Disclaimer
This project is for research and educational purposes only.
It is not investment advice and is not intended for live trading.

Author
Built by Nathrah as part of a personal quant research portfolio.

