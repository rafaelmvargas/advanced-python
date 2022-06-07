# 8.52:  Use .sort_index() to sort the DataFrame by index.

import pandas as pd

df = pd.DataFrame({ 'g': [7, 5, 1],
                    'x': [2.9, 3.5, 4.9],
                    'b': ['yourstr', 'mystr', 'theirstr']  },
                    index=['r9', 'r1', 'r5'])


