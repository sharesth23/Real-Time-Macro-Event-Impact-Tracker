import pandas as pd
import numpy as np

def average_event_response(windows):
    aligned = pd.concat(
        [w.reset_index(drop=True) for w in windows],
        axis=1
    )
    return aligned.mean(axis=1)
