import pandas as pd

def compute_atr(df, window=20):
    df = df.copy()
    df["Range"] = df["High"] - df["Low"]
    df["ATR"] = df["Range"].rolling(window).mean()
    return df
