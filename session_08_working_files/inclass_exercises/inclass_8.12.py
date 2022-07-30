# 8.12:  View the 'a' column using subscript syntax (df['a']),
# and the same column using attribute syntax (df.a).  Print
# the type of this object.

from socket import SO_J1939_PROMISC
import pandas as pd

dol = {  'a': [1, 2, 3],
         'b': [2.9, 3.5, 4.9],
         'c': ['yourstr', 'mystr', 'theirstr']  }

df = pd.DataFrame(dol, index=['x', 'y', 'z'])


print(df)

s1 = df['x']    # Series object representing the 'a' column

s1 = df.loc['x']    # Series object representing the 'x' row

s1 = df.a       # Series objecting representing the 'a' column

print(s1)

print(type(s1))

# DataFrame 2D struct, with colum/row labels
# Series    1D struct, with index labels
# Index


# a "copy of a slice" warning may be issued
# when you try to slice a dataframe, and 
# then modify the slice