from data.assets import ASSETS
from src.data_loader import load_intraday_prices
from src.event_alignment import align_event
from src.visualization import plot_event_reaction
import pandas as pd

event_time = pd.Timestamp("2023-06-13 13:30:00", tz="UTC")  # CPI release

prices = load_intraday_prices(
    ASSETS["SP500"],
    event_time.date(),
    (event_time + pd.Timedelta(days=1)).date()
)

window = align_event(prices, event_time)
plot_event_reaction(window, "S&P 500 Reaction to CPI")
