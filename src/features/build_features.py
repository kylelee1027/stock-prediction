import pandas as pd
from src.utils.paths import SPY_DIR

df = pd.read_csv(SPY_DIR/"cleaned/spy_clean.csv", parse_dates=["Date"])
df = df.set_index("Date")
print(df.columns)

# Daily Return
df["return_1d"] = df["Close"].pct_change(1)
df["return_5d"] = df["Close"].pct_change(5)
df["return_10d"] = df["Close"].pct_change(10)

# Rolling Volatility
df["volatility_5d"] = df["return_1d"].rolling(5).std()
df["volatility_10d"] = df["return_1d"].rolling(10).std()

# Simple Moving Averages
df["sma_5"] = df["Close"].rolling(5).mean()
df["sma_10"] = df["Close"].rolling(10).mean()

# Target Variable (whether tomorrow's close is higher than today's)
df["target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)
df = df.dropna()
df.to_csv(SPY_DIR/"spy_features.csv")