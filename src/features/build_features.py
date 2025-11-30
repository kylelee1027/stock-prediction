import pandas as pd
from src.utils.paths import SPY_2024_PRESENT

df = pd.read_csv(SPY_2024_PRESENT)
print(df.columns)