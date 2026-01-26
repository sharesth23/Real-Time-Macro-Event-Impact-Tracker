 import pandas as pd

def load_event_data(event, asset, window):

    path = f"data/{event}_{asset.replace(' ', '_')}.csv"
    df = pd.read_csv(path)
    df = df[df["minutes_from_event"].abs() <= window]
    return df
