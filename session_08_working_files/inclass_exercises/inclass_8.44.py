# 8.44:  Add a new column 'd', set to the value of column 'b'
# * 2

import pandas as pd

df = pd.DataFrame({ 'a': [1, 2, 3],
                    'b': [2.9, 3.5, 4.9],
                    'c': ['yourstr', 'mystr', 'theirstr']  },
                    index=['r1', 'r2', 'r3'])

