import pandas as pd
import numpy as np

def correlation(df, x, y):
    x = df[x].to_numpy()
    y = df[y].to_numpy()
    cov = np.cov(x,y)
    return cov