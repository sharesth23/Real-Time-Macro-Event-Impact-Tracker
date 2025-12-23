import yfinance as yf
import pandas as pd

def load_intraday_prices(ticker, start, end, interval="5m"):
    df = yf.download(
        ticker,
        start=start,
        end=end,
        interval=interval,
        progress=False
    )
    return df["Close"].dropna()
