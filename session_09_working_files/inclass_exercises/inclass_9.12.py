# 9.12:  .groupby():  custom 'summary' function using
# .apply().  Group rows by 'SalesRep' and use .apply() with a
# function that expects a DataFrame of grouped rows and
# returns the sum of 'SaleAmount' from the DataFrame.  (In
# other words, this replicates what .groupby().sum() does).

import pandas as pd

def price_sum(this_df):
    return # your code here

df = pd.read_excel("../sales-funnel.xlsx")

print(df.groupby('SalesRep').apply(price_sum))


