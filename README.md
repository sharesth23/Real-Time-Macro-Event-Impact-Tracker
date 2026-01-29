

# 📊 Real-Time Macro Event Impact Tracker

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-ff4b4b)
![Research](https://img.shields.io/badge/Use--Case-Quant%20Research-purple)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange)

A research-focused Python project to **quantify and visualize the real-time impact of macroeconomic events on financial markets**. This system aligns macro events with asset price movements, computes impact metrics, and presents insights via experiments, visualizations, and an interactive dashboard.

---

## 🚀 Project Overview

Macroeconomic events (CPI releases, rate decisions, GDP data, etc.) often cause sudden structural shifts in asset prices. This project aims to:

* Detect and align macroeconomic events with market data
* Measure short-term and cross-asset impacts
* Analyze correlations and volatility responses
* Visualize event-driven market behavior
* Support reproducible research and experimentation

This repo is designed for **quant research, financial analytics, and academic experimentation**.

---

## 🧠 Key Features

* **Event Alignment Engine** – Map macro events to price timelines
* **Impact Metrics** – Returns, volatility shifts, correlation changes
* **Cross-Asset Analysis** – Equity, FX, crypto, or multi-asset support
* **Experimental Pipelines** – Modular experiments for hypothesis testing
* **Interactive Dashboard** – Streamlit-based UI for exploration
* **Paper-Ready Outputs** – LaTeX paper + BibTeX references included

---

## 🗂️ Project Structure

```
Real-Time-Macro-Event-Impact-Tracker/
│
├── dashboard/
│   ├── app.py              # Streamlit dashboard
│   └── data_loader.py      # Dashboard-specific loaders
│
├── data/                   # Raw & processed datasets
│   ├── assets.py
│   └── events.py
│
├── experiments/             # Research experiments
│   ├── exp_01_single_event.py
│   ├── exp_02_event_study.py
│   ├── exp_03_cross_asset.py
│   └── exp_04_event_correlation.py
│
├── paper/                   # Research paper assets
│   ├── macro_event_impact.tex
│   └── references.bib
│
├── src/                     # Core logic
│   ├── data_loader.py
│   ├── event_alignment.py
│   ├── event_correlation.py
│   ├── impact_metrics.py
│   ├── macro_api.py
│   └── visualization.py
│
├── web/
│   └── api.py               # Optional API layer
│
├── assets.py                # Global asset config
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

```bash
git clone https://github.com/sharesh23/Real-Time-Macro-Event-Impact-Tracker.git
cd Real-Time-Macro-Event-Impact-Tracker
pip install -r requirements.txt
```

> Recommended: Python 3.9+

---

## ▶️ Usage

### 1️⃣ Run Experiments

```bash
python experiments/exp_01_single_event.py
```

Each experiment focuses on a specific research question (event study, correlation, cross-asset effects).

---

### 2️⃣ Launch Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard features:

* Event selection
* Asset-wise impact comparison
* Metric visualizations
* Time-window sensitivity

---

## 📈 Metrics Computed

* Abnormal returns
* Volatility spikes
* Event-window cumulative returns
* Cross-asset correlation shifts
* Pre/Post-event regime comparison

---

## 📄 Research Paper

The `paper/` directory contains a **LaTeX-ready academic paper**, suitable for:

* Conference submissions
* GSoC / research proposals
* Quant research portfolios

---

## 🧪 Extending the Project

You can easily extend this system by:

* Adding new macro data sources (FRED, ECB, RBI, etc.)
* Plugging in alternative asset classes
* Implementing ML-based event impact prediction
* Deploying the API for real-time inference

---

## 🛠️ Tech Stack

* Python
* Pandas / NumPy
* Streamlit
* Matplotlib / Plotly
* LaTeX

---

## 📜 License

This project is licensed under the MIT License.

---

## ✨ Author

**Sharesh Gulia**
Quant Research | Systems | Market Microstructure

If you find this useful, consider ⭐ starring the repo.
