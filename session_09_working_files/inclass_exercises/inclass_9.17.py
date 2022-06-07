# 9.17:  pd.pivot_table():  dual-column aggregation.  Perform
# the same pivot as previous, but group by by both 'SalesRep'
# and 'Product'.

import pandas as pd
import numpy as np

df = pd.read_excel("../sales-funnel.xlsx")

print(pd.pivot_table(df, index='SalesRep', aggfunc=np.sum))

