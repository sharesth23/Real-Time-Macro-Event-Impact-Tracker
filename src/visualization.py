import matplotlib.pyplot as plt

def plot_event_reaction(price_series, title):
    normalized = price_series / price_series.iloc[0]

    plt.figure(figsize=(9, 5))
    normalized.plot()
    plt.axvline(normalized.index[len(normalized)//2], color="red", linestyle="--")
    plt.title(title)
    plt.ylabel("Normalized Price")
    plt.show()
