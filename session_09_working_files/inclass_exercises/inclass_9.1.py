# 9.1:  Review:  check the .dtypes of a DataFrame and .dtype
# of a Series.

import pandas as pd

dol = {  'a': [1, 2, 3],
         'b': [2.9, 3.5, 4.9],
         'c': ['yourstr', 'mystr', 'theirstr']  }

df = pd.DataFrame(dol, index=['w', 'x', 'y'])


