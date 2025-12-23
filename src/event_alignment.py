import pandas as pd

def align_event(prices, event_time, window_minutes=120):
    """
    Extract price window around macro event.
    """
    start = event_time - pd.Timedelta(minutes=window_minutes)
    end = event_time + pd.Timedelta(minutes=window_minutes)

    return prices.loc[start:end]
