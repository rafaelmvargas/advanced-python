# 9.14:  .groupby():  custom 'grouping' function.  Pass a
# function to groupby() that identifies 2 groups using the
# 'Product' column:  if the value is 'CPU' or 'Monitor',
# return 'hardware'; otherwise, return 'software'.  Count the
# number of rows in each group with .count().

import pandas as pd

def grouper(row_idx):
    row = df.loc[row_idx]
    # your code here - identify the 'Product' value in the row and return 'software' or 'hardware'

df = pd.read_excel("../sales-funnel.xlsx")

print(df.groupby(grouper).count())

# The function receives a row index which you can use with
# .loc[] to find the row being grouped.  Have the function
# return 'Software' if the 'Product' value is 'Software' or
# 'Maintenance', and 'Hardware' if the Product is 'CPU'.

