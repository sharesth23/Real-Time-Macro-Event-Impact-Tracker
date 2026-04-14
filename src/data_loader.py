import yfinance as yf
import pandas as pd

def load_data(asset: str, interval="1m", period="5d"):
    """
    Fetch real market data using yfinance

    Args:
        asset: ticker (SPY, BTC-USD, EURUSD=X)
        interval: 1m, 5m, 1h, 1d
        period: 1d, 5d, 1mo, etc.
    """
