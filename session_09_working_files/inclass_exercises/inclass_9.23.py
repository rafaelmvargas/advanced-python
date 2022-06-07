# 9.23:  MultiIndex:  use .query('Manager == "Debra Henley"')
# to select rows.

import pandas as pd
import numpy as np

df = pd.read_excel("../sales-funnel.xlsx")

table = pd.pivot_table(df, index=['Manager', 'SalesRep'],
                           aggfunc=np.sum)

print(table.query(# your code here))

