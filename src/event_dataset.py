import pandas as pd
from fredapi import Fred
import os

fred = Fred(api_key=os.getenv("FRED_API_KEY"))

def get_cpi_events():
    cpi = fred.get_series("CPIAUCSL")
    df = cpi.to_frame(name="cpi")

    df["event"] = "CPI"
    df["date"] = df.index

    return df.reset_index(drop=True)


def get_gdp_events():
    gdp = fred.get_series("GDP")
    df = gdp.to_frame(name="gdp")

    df["event"] = "GDP"
    df["date"] = df.index

    return df.reset_index(drop=True)


def build_event_dataset():
    cpi = get_cpi_events()
    gdp = get_gdp_events()

    events = pd.concat([cpi, gdp])
    events = events.sort_values("date")

    return events