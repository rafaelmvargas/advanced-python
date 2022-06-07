# 9.15:  pd.pivot_table():  single-column aggregation.  First,
# view the DataFrame above.  Then use .pivot_table(df) to
# aggregate by 'SalesRep', using the index= parameter.

import pandas as pd
import numpy as np

df = pd.read_excel("../sales-funnel.xlsx")

print(pd.pivot_table(df, # your code here))

# The default summary method is average (i.e., .mean())

