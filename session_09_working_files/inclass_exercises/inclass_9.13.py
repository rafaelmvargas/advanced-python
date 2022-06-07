# 9.13:  .groupby():  custom 'summary' function using
# .apply().  Building on the previous solution, customize the
# function to sum SaleAmount but reduce 'CPU' values by 20% in
# the sum (because of the overhead cost of CPU handling).

import pandas as pd

def price_sum(this_df):
    return # your code here

df = pd.read_excel("../sales-funnel.xlsx")

# Expected Output:
# <PRE>SalesRep
# Cedric Moss       91000
# Craig Booker      67000
# Daniel Hilton     94000
# John Smith        33000
# Wendy Yule       143000
# dtype: int64</PRE>

