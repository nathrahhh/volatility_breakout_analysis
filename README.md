Volatility Breakout Strategy — ATR-Based Backtest (Python)
Overview

This repository contains a Python implementation and analysis of a simple ATR-based volatility breakout strategy using daily OHLCV data.

The goal of this project is not to “find alpha”, but to demonstrate a clean research workflow including:

- Feature engineering (ATR)
- Signal construction
- Position management
- Transaction cost modelling
- Performance evaluation and diagnostics
- Regime-based robustness checks

The strategy is intentionally simple and is used as a case study for understanding why many intuitive strategies fail after costs.

Strategy Summary:
The strategy uses Average True Range (ATR) as a volatility benchmark.

Core logic:
- Compute rolling ATR.
- Detect breakout days when the daily range exceeds a multiple of ATR.
- Enter a position (long/short) based on the breakout direction.
- Hold for a fixed number of days.
- Apply transaction costs and evaluate net performance.

Repository Structure
  
  volatility_breakout.ipynb
  Main notebook containing the full pipeline:
  
  Data loading
  
  ATR calculation
  
  Signal generation
  
  Position construction

Backtest returns + transaction costs

Diagnostics and robustness checks

data/
Contains CSV price data used for backtesting (e.g. SPY daily OHLCV).

Key Components
1) Feature Engineering
    ATR (rolling)
    Daily range and returns

2) Signal Generation
    Signals are generated when volatility exceeds a threshold:
    range > k × ATR

3) Backtest & Execution Assumptions
    Positions are lagged to avoid lookahead bias.
    Fixed holding period.
    Transaction costs included (configurable).

4) Diagnostics
The notebook includes:
- Equity curve
- Return distribution
- Drawdowns
- Trade frequency
- Performance breakdown by volatility regime
- Results (Summary)

In the tested configuration, the strategy demonstrates a common research outcome:
- Sparse large gains occur occasionally.
- However, frequent small losses and transaction costs dominate.
- Conditioning on high-volatility regimes increases activity but does not reliably improve expectancy.

This reinforces the importance of:
- realistic costs,
- avoiding overfitting,
- and testing across regimes.

Notes / Limitations
This project is intended as a research demonstration and not a deployable trading system.

Possible extensions:
- parameter sweeps (k, ATR window, holding period)
- risk targeting / volatility scaling
- alternative breakout definitions
- multi-asset testing
- event filtering (earnings, macro releases)

How to Run

Clone the repository

Install dependencies (typical stack: pandas, numpy, matplotlib)

Run the notebook

Author

Nathrah Sharul Nizam
(Quant research + structured backtesting focus)
\
