# 8.28:  Reorder the columns on the DataFrame to 'a', 'b', 'x'
# using .reindex().  Note that the 'x' column springs into
# existence with empty values.

import pandas as pd

df = pd.DataFrame({ 'a': [1, 2, 3],
                    'b': [2.9, 3.5, 4.9],
                    'c': ['yourstr', 'mystr', 'theirstr']  },
                    index=['r1', 'r2', 'r3'])


