# 8.54:  Use axis=1 to .sort_index() to sort the DataFrame by
# its columns.

import pandas as pd

df = pd.DataFrame({ 'g': [7, 5, 1],
                    'x': [2.9, 3.5, 4.9],
                    'b': ['yourstr', 'mystr', 'theirstr']  },
                    index=['r9', 'r5', 'r1'])


