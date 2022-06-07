# 8.13:  View the 'y' row using .loc[] and do the same with
# .iloc[] indexing.  Print the type of this object.

import pandas as pd

dol = {  'a': [1, 2, 3],
         'b': [2.9, 3.5, 4.9],
         'c': ['yourstr', 'mystr', 'theirstr']  }

df = pd.DataFrame(dol, index=['x', 'y', 'z'])


