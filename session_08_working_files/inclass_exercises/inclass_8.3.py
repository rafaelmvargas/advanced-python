# 8.3:  Use this dict of lists to build a DataFrame.  Add a
# keyword argument index=[] to the call to DataFrame() to
# populate the list with row labels 'x', 'y' and 'z'.  Print
# the DataFrame.

import pandas as pd

dol = {  'a': [1, 2, 3],
         'b': [2.9, 3.5, 4.9],
         'c': ['yourstr', 'mystr', 'theirstr']  }

df = pd.DataFrame(dol, index=['x','y','z'])

print(df)