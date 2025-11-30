import pandas as pd
from src.utils.paths import SPY_2024_PRESENT, SPY_DIR

df = pd.read_csv(SPY_2024_PRESENT, parse_dates=["Date"])
df = df.sort_values("Date")
df = df.drop_duplicates(subset=["Date"])
df = df.ffill()
df.to_csv(SPY_DIR/"cleaned/spy_clean.csv")