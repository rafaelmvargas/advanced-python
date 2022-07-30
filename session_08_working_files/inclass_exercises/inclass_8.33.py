# 8.33:  Slice the 'Mkt-RF' and 'SMB' columns of the FF
# DataFrame using subscript syntax with a list of column
# names.

import pandas as pd

df = pd.read_csv(
    "../F-F_Research_Data_Factors_daily.txt",
    sep="\s+",
    header=3,
    skipfooter=2,
    engine="python",
)


# This type of slicing is done for read-only purposes (use
# .loc[] if you intend to write to the slice).

dfs = df.loc[(df["Mkt-RF"] > 0) | (df.SMB > 0)]



dfs = df.loc[df.SMB.isin([0.0, 1])]

print(dfs)