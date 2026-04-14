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
def macro_surprise(actual, forecast , normalise = True):
    """
    Computes macro surprise index
    """
    if  forecast == 0:
        return np.nan
    raw = actual- forecast 

    if normalise :
        return raw / abs(forecast)
    
    return raw 

def event_drawdown(series: pd.Series):
    """
    Computes max drawdown during event window
    """
    returns = series.pct_change().dropna()
    cum = (1 + returns).cumprod()

    peak = cum.cummax()
    drawdown = (cum - peak) / peak

    return drawdown.min()
