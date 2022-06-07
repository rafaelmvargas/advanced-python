# 9.19:  pd.pivot_table():  further agg by secondary value.
# Perform the above pivot on just 'SalesRep', but use columns=
# with a list to show the results broken down by 'Product'.

import pandas as pd
import numpy as np

df = pd.read_excel("../sales-funnel.xlsx")

print(pd.pivot_table(df, index='SalesRep',
                         aggfunc=np.sum,
                         values=['SaleAmount', 'Quantity']
                         # your code here))


