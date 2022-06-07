# 9.21:  MultiIndex:  slicing at 2nd level.  Use a 2-item
# tuple (first-level label, second-level label) to slice for
# just 'Debra Henley' at the first level and 'Craig Booker' at
# the 2nd level.

import pandas as pd
import numpy as np

df = pd.read_excel("../sales-funnel.xlsx")

table = pd.pivot_table(df, index=['Manager', 'SalesRep'],
                           aggfunc=np.sum)

print(table)

