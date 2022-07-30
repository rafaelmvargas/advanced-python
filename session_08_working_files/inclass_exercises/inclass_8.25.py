# 8.25:  Using .rename(), rename column label 'a' to 'A' and
# row label 'r1' to 'R1'.  (.rename() returns the new,
# modified DataFrame)

import pandas as pd

dol = {"a": [1, 2, 3], "b": [2.9, 3.5, 4.9], "c": ["yourstr", "mystr", "theirstr"]}

df = pd.DataFrame(dol, index=["r1", "r2", "r3"])


df["d"] = df.a + df.b
print(df)
print()
print(df.d.sum())


# sum up the 'd' col only for those rows with 'b' < 4
print(df.loc[df.b < 4].d.sum())


df["d"] = 0
df.loc[df.b < 4, "d"] = 100

print(df)
# Rename
# df = df.rename(columns={"a": "A"}, index={"r2": "THIS"})
