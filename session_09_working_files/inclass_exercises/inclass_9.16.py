# 9.16:  pd.pivot_table() specifying a summary function.
# Perform the same pivot as previous, but use the aggfunc=
# parameter to specify a sum (use np.sum).

import pandas as pd
import numpy as np

df = pd.read_excel("../sales-funnel.xlsx")

print(pd.pivot_table(df, index='SalesRep' # your code here))

