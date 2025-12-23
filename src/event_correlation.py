import pandas as pd
from src.correlation import rolling_correlation
from src.systemic_metrics import average_correlation


def correlation_shift_around_event(
    returns,
    event_time,
    pre_window=60,
    post_window=60
):
    """
    Computes average correlation shift around a macro event.
    Windows are in minutes (assuming intraday data).
    """

    pre_end = event_time
    pre_start = event_time - pd.Timedelta(minutes=pre_window)

    post_start = event_time
    post_end = event_time + pd.Timedelta(minutes=post_window)

    pre_returns = returns.loc[pre_start:pre_end]
    post_returns = returns.loc[post_start:post_end]

    if len(pre_returns) < 5 or len(post_returns) < 5:
        return None

    pre_corr = pre_returns.corr()
    post_corr = post_returns.corr()

    return {
        "avg_corr_pre": average_correlation(pre_corr),
        "avg_corr_post": average_correlation(post_corr),
        "delta_corr": average_correlation(post_corr) - average_correlation(pre_corr)
    }
