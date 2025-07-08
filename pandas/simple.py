import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2, 3]})
print("## Data Frame")
print(df, "\n")

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print("## Series")
print(s, "\n")

dates = pd.date_range("20130101", periods=6)
print("## Date Range")
print(dates, "\n")

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print("## Data Frame")
print(df2)
print("--")
print(df2.dtypes, "\n")

