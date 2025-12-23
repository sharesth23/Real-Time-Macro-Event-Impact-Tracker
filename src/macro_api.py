import requests
import pandas as pd

def fetch_macro_events(api_key, indicator, start_date, end_date):
    """
    Fetch macroeconomic releases with timestamps.
    """
    url = "https://api.tradingeconomics.com/calendar"
    params = {
        "c": api_key,
        "indicator": indicator,
        "start": start_date,
        "end": end_date,
        "format": "json"
    }

    r = requests.get(url, params=params)
    data = r.json()

    df = pd.DataFrame(data)
    df["Date"] = pd.to_datetime(df["Date"])
    return df[["Date", "Actual", "Forecast", "Previous"]]
