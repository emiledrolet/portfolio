import pandas as pd
import numpy as np
import pyfolio as pf
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from datetime import date


# import statsmodels.api as sm
# from pypfopt.efficient_frontier import EfficientFrontier
# from pypfopt import risk_models, expected_returns

start = date(2015, 1, 1)
end = date(2016, 1, 1)

ticker = "GOOG"

# Convert dates to string format for yfinance
start_str = start.strftime('%Y-%m-%d')
end_str = end.strftime('%Y-%m-%d')

# Fetch data using yfinance
stock_data = yf.download(ticker, start=start_str, end=end_str)

stock_data_close = stock_data["Close"]
print(stock_data_close.pct_change())