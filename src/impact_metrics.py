import numpy as np
import pandas as pd


def event_return(series: pd.Series):
    """
    Computes cumulative return over event window
    """
    if len(series) < 2:
        return np.nan

    return (series.iloc[-1] / series.iloc[0]) - 1

def event_volatility(series: pd.Series):
    """
    Computes volatility (std of returns)
    """
    returns = series.pct_change().dropna()

    if len(returns) == 0:
        return np.nan

    return returns.std()