# 9.18:  pd.pivot_table():  specifying values to summarize.
# Perform the same pivot as previous, but use values= with a
# list to specify 'SaleAmount' and 'Quantity'.

import pandas as pd
import numpy as np

df = pd.read_excel("../sales-funnel.xlsx")

print(pd.pivot_table(df, index=['SalesRep', 'Product'], aggfunc=np.sum # your code here))

