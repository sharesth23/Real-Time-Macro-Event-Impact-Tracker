import numpy as np

def event_return(series):
    return (series.iloc[-1] / series.iloc[0]) - 1


def event_volatility(series):
    return series.pct_change().std()


def macro_surprise(actual, forecast):
    return actual - forecast
