# 8.9:  Use the .dtypes attribute to see what types pandas has
# assigned to each column.

import pandas as pd

dol = {  'a': [1, 2, 3],
         'b': [2.9, 3.5, 4.9],
         'c': ['yourstr', 'mystr', 'theirstr']  }

df = pd.DataFrame(dol, index=['x', 'y', 'z'])

