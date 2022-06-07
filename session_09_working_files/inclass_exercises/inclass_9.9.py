# 9.9:  Apply a function to each Series row in a DataFrame.
# Call .apply() on the DataFrame with axis=1, which will pass
# each row Series to the function in turn.  Sum up the row
# values and create a new 'd' row with the sum of values.

import pandas as pd

def sum_row(series_row):
    # set new 'd' column value in this series row
    # to the sum of the values in the row

dol = {  'a': [1, 2, 3],
         'b': [290.0, 350.0, 490.0],
         'c': [0.1, 0.2, 0.3]  }

df = pd.DataFrame(dol, index=['w', 'x', 'y'])

df = df.apply(sum_row, axis=1)

print(df)

