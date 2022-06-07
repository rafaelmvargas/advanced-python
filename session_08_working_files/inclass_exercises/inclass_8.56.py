# 8.56:  First view, then concatenate the two DataFrames
# horizontally.

import pandas as pd

df = pd.DataFrame({ 'a': [1, 2, 3],
                    'b': [2.9, 3.5, 4.9],
                    'c': ['yourstr', 'mystr', 'theirstr']  },
                    index=['r1', 'r2', 'r3'])

df2 = pd.DataFrame({ 'd': ['xylo', 'yellow', 'zello'],
                     'e': [0, 0, 0],
                     'f': [1.1, 1.1, 1.2]  },
                     index=['r1', 'r2', 'r3'])


