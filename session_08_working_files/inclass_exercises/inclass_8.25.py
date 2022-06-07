# 8.25:  Using .rename(), rename column label 'a' to 'A' and
# row label 'r1' to 'R1'.  (.rename() returns the new,
# modified DataFrame)

import pandas as pd

dol = {  'a': [1, 2, 3],
         'b': [2.9, 3.5, 4.9],
         'c': ['yourstr', 'mystr', 'theirstr']  }

df = pd.DataFrame(dol, index=['r1', 'r2', 'r3'])


