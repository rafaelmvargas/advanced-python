# 8.11:  Explore the .index and .columns attributes of a
# DataFrame.  Print the resulting objects.

import pandas as pd

dol = {  'a': [1, 2, 3],
         'b': [2.9, 3.5, 4.9],
         'c': ['yourstr', 'mystr', 'theirstr']  }

df = pd.DataFrame(dol, index=['x', 'y', 'z'])


