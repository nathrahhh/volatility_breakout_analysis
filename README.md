Volatility Breakout Strategy Analysis – Sisyphus Paradigm
Overview

This repository contains a Python implementation and analysis of a volatility breakout trading strategy. The work is inspired by Chapter 3 of Advances in Financial Machine Learning (AFML) and illustrates the Sisyphus paradigm: plausible trading strategies that appear promising but fail to generate persistent alpha due to noise, costs, and sparse opportunities.

The strategy uses Average True Range (ATR) to identify volatility breakouts, constructs positions, computes net strategy returns including transaction costs, and evaluates performance under different regimes.

Files

volatility_breakout.ipynb – Jupyter notebook containing:

Feature engineering (ATR calculation, daily range)

Signal generation (volatility breakout)

Position construction

Strategy returns calculation

Equity curve plotting

Histogram analysis of returns

Robustness checks (high-volatility regime)

Markdown commentary and discussion of results

data/ – CSV files with historical OHLCV (Open, High, Low, Close, Volume) data for backtesting.

Strategy Description

ATR Calculation: Compute the rolling average true range to measure volatility.

Signal Generation: Enter long/short positions when the daily range exceeds a multiple of ATR.

Position Construction: Hold positions for a fixed number of days; overlapping signals are aggregated.

Strategy Returns: Apply lagged positions to daily asset returns, accounting for transaction costs.

Robustness Checks: Examine performance in high-volatility regimes (ATR > 75th percentile).

Results

Equity Curve: Shows gradual decay with occasional spikes, indicating sparse profitable opportunities and persistent small losses.

Return Distribution: High peak at zero, negative skew, rare positive returns.

High-Volatility Regime Analysis: Trading in high-vol periods increases frequency of signals but does not eliminate losses; demonstrates the structural limitations of the strategy.

Key Insights – The Sisyphus Paradigm

Most trading days yield negligible or slightly negative returns due to sparse signals and transaction costs.

Occasional large gains appear as spikes in the equity curve, but they are insufficient to offset accumulated small losses.

Conditioning on high-volatility periods changes the number of active trades but not the underlying expectancy.

The strategy highlights the difficulty of generating persistent alpha in noisy, mean-reverting markets: no matter how much effort is invested, performance is eroded — just like Sisyphus pushing the boulder uphill.


