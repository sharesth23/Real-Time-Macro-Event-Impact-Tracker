import streamlit as st 
from data_loader import load_event_data
from plots import plot_price_impact, plot_volatility
from metrics import compute_metrics

st.set_page_config(page_title="Macro Event Impact Tracker", layout="wide")

st.title("📊 Real-Time Macro Event Impact Tracker")
st.caption("Visualizing market reactions to CPI, NFP, FOMC, PMI releases")


event = st.sidebar.selectbox(
    "Select Macro Event",
    ["CPI", "NFP", "FOMC", "PMI"]
)

asset = st.sidebar.selectbox(
    "Select Asset",
    ["S&P 500", "EUR/USD", "US 10Y", "VIX"]
)

window = st.sidebar.slider(
    "Event Window (minutes)",
    min_value=5,
    max_value=240,
    value=60
)

df = load_event_data(event, asset , window )
metrics = compute_metrics(df)

col1 , col2 , col3 = st.columns(3)
col1.metric("Mean Return", f"{metrics['mean_return']:.2f}%")
col2.metric("Max Drawdown", f"{metrics['max_drawdown']:.2f}%")
col3.metric("Volatility Change", f"{metrics['vol_change']:.2f}%")

st.subheader("📈 Price Impact")
st.plotly_chart(plot_price_impact(df), use_container_width=True)

st.subheader("📉 Volatility Reaction")
st.plotly_chart(plot_volatility(df), use_container_width=True)
