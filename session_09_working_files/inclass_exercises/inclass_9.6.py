# 9.6:  Apply a function to each item in a Series column.
# Create new column 'd' that is the value of 'b' * 100, by
# using .apply() with the centify function (defined below).
# 'd' column values should be 290.0, 350.0, 490.0.  When
# correct, replace the function with a lambda.

import pandas as pd

def centify(arg):
    return arg * 100

dol = {  'a': [1, 2, 3],
         'b': [2.9, 3.5, 4.9],
         'c': [0.1, 0.2, 0.3]  }

df = pd.DataFrame(dol, index=['w', 'x', 'y'])

df['d'] = df.b.apply(# your code here)

print(df)

