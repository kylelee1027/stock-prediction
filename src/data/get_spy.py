"""
This script is to download SPY (SPDR S&P 500 ETF Trust) historical data from Yahoo Finance.
"""
import yfinance as yf
import os

# Make folder if it doesn't exist
folder_path = "data/spy"
os.makedirs(folder_path, exist_ok=True)

# Download SPY data to file path
spy = yf.download("SPY", start="2024-01-01", end="2025-11-24")
file_path = os.path.join(folder_path, "spy.csv")
spy.to_csv(file_path)
print(f"File saved to: {file_path}")