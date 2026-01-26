import streamlit as st 
from data_loader import load_event_data
from plots import plot_price_impact, plot_volatility
from metrics import compute_metrics