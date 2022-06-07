# 9.8:  Apply a function to each Series column in a DataFrame.
# Call .apply() on the DataFrame, which will pass each column
# Series to the function in turn.  Inside the function, sum up
# the column values and create a new 'z' row with the sum of
# values.

import pandas as pd

def sum_col(series_column):
    # set new 'z' row value in this series column
    # to the sum of the values in the column
    # make sure to return the changed series

dol = {  'a': [1, 2, 3],
         'b': [290.0, 350.0, 490.0],
         'c': [0.1, 0.2, 0.3]  }

df = pd.DataFrame(dol, index=['w', 'x', 'y'])

df = df.apply(sum_col)

print(df)

