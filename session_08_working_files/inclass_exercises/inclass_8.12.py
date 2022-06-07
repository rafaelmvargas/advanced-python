# 8.12:  View the 'a' column using subscript syntax (df['a']),
# and the same column using attribute syntax (df.a).  Print
# the type of this object.

import pandas as pd

dol = {  'a': [1, 2, 3],
         'b': [2.9, 3.5, 4.9],
         'c': ['yourstr', 'mystr', 'theirstr']  }

df = pd.DataFrame(dol, index=['x', 'y', 'z'])


