"""
Event-driven correlation breakdown analysis.
"""

import pandas as pd
import matplotlib.pyplot as plt

from data.assets import ASSETS
from src.data_loader import load_intraday_prices
from src.event_correlation import correlation_shift_around_event

# Example CPI event
event_time = pd.Timestamp("2023-06-13 13:30:00", tz="UTC")

# Load intraday returns
prices = {}
for k, v in ASSETS.items():
    p = load_intraday_prices(
        v,
        event_time.date(),
        (event_time + pd.Timedelta(days=1)).date()
    )
    prices[k] = p

prices = pd.DataFrame(prices).dropna()
returns = prices.pct_change().dropna()

shift = correlation_shift_around_event(returns, event_time)

print(shift)

plt.bar(
    ["Pre-event", "Post-event"],
    [shift["avg_corr_pre"], shift["avg_corr_post"]]
)
plt.title("Average Cross-Asset Correlation Around CPI")
plt.savefig("paper/figures/fig_event_corr_shift.png", dpi=300)
plt.show()
