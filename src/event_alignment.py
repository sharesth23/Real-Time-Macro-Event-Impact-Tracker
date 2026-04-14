import pandas as pd

def align_event(data: pd.DataFrame, event_time: str, window: int = 60):
    """
    Align data around event timestamp

    event_time format: '2024-01-10 14:30:00'
    window: minutes before/after
    """

    time_col = data.columns[0]
    data[time_col] = pd.to_datetime(data[time_col])

    event_time = pd.to_datetime(event_time)

    start = event_time - pd.Timedelta(minutes=window)
    end = event_time + pd.Timedelta(minutes=window)

    return data[(data[time_col] >= start) & (data[time_col] <= end)]