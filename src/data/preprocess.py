import pandas as pd
from src.utils.paths import SPY_2024_PRESENT

df = pd.read_csv(SPY_2024_PRESENT, header=[0,1], skiprows=[2])
df = df.rename(columns={df.columns[0]: "Date"})
print(df)
df["Date"] = pd.to_datetime(df["Date"])
df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]
print(df.columns)