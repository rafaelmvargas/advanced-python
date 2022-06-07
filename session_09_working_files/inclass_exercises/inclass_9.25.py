# 9.25:  MultiIndex:  use .loc[] with a 1- or 2-item tuple to
# select rows.  Keep in mind that a 1-item tuple must have a
# comma after the item, for example ('Manager',)

import pandas as pd
import numpy as np

df = pd.read_excel("../sales-funnel.xlsx")

table = pd.pivot_table(df, index=['Manager', 'SalesRep'],
                           aggfunc=np.sum)

print(table)

