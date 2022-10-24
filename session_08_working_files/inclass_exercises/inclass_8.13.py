# 8.13:  View the 'y' row using .loc[] and do the same with
# .iloc[] indexing.  Print the type of this object.

import pandas as pd

dol = {  'a': [1, 2, 3],
         'b': [2.9, 3.5, 4.9],
         'c': ['yourstr', 'mystr', 'theirstr']  }

df = pd.DataFrame(dol, index=['x', 'y', 'z'])


print(df)

print()


# David recommends .loc[] for most if not all of
# your dataframe slicing needs
# there are multiple ways to slice with .loc[]
# a string: retrieve a series
# a list of labels: retrive specified rows
# dfs = df.loc[['x','z']]

# a range of labels: df.loc['x':'z']

dfs = df.loc['y':'z', 'a':'b']
dfs = df.loc['y':'z', ['a','c']]
dfs = df.loc['y':'z', 'a']

# how would i select all rows, but only some columns
dfs = df.loc[:,['a','c']]

print(dfs)