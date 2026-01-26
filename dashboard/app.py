import streamlit as st 
from data_loader import load_event_data
from plots import plot_price_impact, plot_volatility
from metrics import compute_metrics

st.set_page_config(page_title="Macro Event Impact Tracker", layout="wide")

st.title("📊 Real-Time Macro Event Impact Tracker")
st.caption("Visualizing market reactions to CPI, NFP, FOMC, PMI releases")

# Sidebar controls
event = st.sidebar.selectbox(
    "Select Macro Event",
    ["CPI", "NFP", "FOMC", "PMI"]
)