# 9.7:  Apply a function to each item in a Series row.  Create
# new row 'xc' that is the value of 'x' * 100, by using
# .apply() with the centify function (defined below).  'xc'
# row values should be 20.0, 35000.0, 200.  When correct,
# replace the function with a lambda.

import pandas as pd

def centify(arg):
    return arg * 100

dol = {  'a': [1, 2, 3],
         'b': [290.0, 350.0, 490.0],
         'c': [0.1, 0.2, 0.3]  }

df = pd.DataFrame(dol, index=['w', 'x', 'y'])

df.loc['xc'] = df.loc['x'].apply(# your code here)

print(df)

