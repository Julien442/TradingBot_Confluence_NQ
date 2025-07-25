
import pandas as pd

def load_csv(path):
    try:
        return pd.read_csv(path)
    except:
        return pd.DataFrame()

def detect_confluences(dom, tas):
    return pd.merge_asof(
        tas.sort_values("Timestamp"),
        dom.sort_values("Timestamp"),
        on="Timestamp",
        direction="nearest",
        tolerance=1000
    )
