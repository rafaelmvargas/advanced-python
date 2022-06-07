# 8.5:  Use len() with the DataFrame and len() with .columns
# to see how many rows and columns are in the DataFrame.

import pandas as pd

dol = {  'a': [1, 2, 3, 4],
         'b': [2.9, 3.5, 4.9, 5.3],
         'c': ['yourstr', 'mystr', 'theirstr', 'ourstr']  }

df = pd.DataFrame(dol, index=['w', 'x', 'y', 'z'])

