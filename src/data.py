import pandas as pd
from urllib.parse import urlparse
from sklearn.model_selection import GroupShuffleSplit

def _domaine(url):
    try:
        if not isinstance(url, str): return "inconnu"
        if not url.startswith("http"): url = "http://" + url
        return urlparse(url).netloc
    except Exception:
        return "inconnu"

def load_split(path="../data/archive (2)/new_data_urls.csv"):
    df = pd.read_csv(path).drop_duplicates(subset=["url"]).copy()
    df["domaine"] = df["url"].apply(_domaine)
    gss = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    tr, te = next(gss.split(df, groups=df["domaine"]))
    return df.iloc[tr].copy(), df.iloc[te].copy()