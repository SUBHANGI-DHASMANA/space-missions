import numpy as np

def preprocess(df):
    df.drop(df.columns[[0, 1]], axis=1, inplace=True)
    return df

def RA(df):
    df_ = df.dropna(subset=[" Rocket"], axis="rows")
    df_.loc[:, " Rocket"] = df_.loc[:, " Rocket"].fillna(0.0).str.replace(",", "")
    df_.loc[:, " Rocket"] = df_.loc[:, " Rocket"].astype(np.float64).fillna(0.0)
    return df_