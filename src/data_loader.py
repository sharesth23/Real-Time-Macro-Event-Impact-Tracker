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

    df = yf.download(
        tickers=asset,
        interval=interval,
        period=period,
        progress=False
    )

    if df.empty:
        raise ValueError(f"No data found for {asset}")

    df = df.reset_index()
    df.rename(columns={"Close": "price"}, inplace=True)

    return df[["Datetime" if "Datetime" in df.columns else "Date", "price"]]