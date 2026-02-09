import numpy as np

def volatility_breakout_signal(df, k=1.5):
    df = df.copy()
    df["Signal"] = 0
    breakout_mask = df["Range"] > k * df["ATR"]
    df.loc[breakout_mask, "Signal"] = np.sign(df["Close"] - df["Open"])[breakout_mask]
    return df
