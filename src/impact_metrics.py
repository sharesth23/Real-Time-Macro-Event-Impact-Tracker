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

def event_volume_spike(volume_series: pd.Series):
    """
    Measures volume spike relative to baseline
    """
    if len(volume_series) < 10:
        return np.nan

    baseline = volume_series.iloc[:len(volume_series)//2].mean()
    spike = volume_series.iloc[len(volume_series)//2:].max()

    return spike / baseline if baseline != 0 else np.nan


def build_event_features(price_series: pd.Series, volume_series=None, actual=None, forecast=None):
    """
    Master feature builder (used for ML training)
    """

    features = {
        "return": event_return(price_series),
        "volatility": event_volatility(price_series),
        "drawdown": event_drawdown(price_series),
        "surprise": macro_surprise(actual, forecast)
    }

    if volume_series is not None:
        features["volume_spike"] = event_volume_spike(volume_series)

    return features