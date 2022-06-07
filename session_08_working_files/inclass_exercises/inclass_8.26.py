# 8.26:  Reorder the index on the DataFrame to 'r2', 'r1',
# 'r3' using .reindex().  (This method also returns the new,
# modified DataFrame.)

import pandas as pd

df = pd.DataFrame({ 'a': [1, 2, 3],
                    'b': [2.9, 3.5, 4.9],
                    'c': ['yourstr', 'mystr', 'theirstr']  },
                    index=['r1', 'r2', 'r3'])


