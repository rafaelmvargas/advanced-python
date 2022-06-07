# 8.27:  Reorder the columns on the DataFrame to 'b', 'a', 'c'
# using .reindex().  (Hint:  use axis=1 to reorder columns.)

import pandas as pd

df = pd.DataFrame({ 'a': [1, 2, 3],
                    'b': [2.9, 3.5, 4.9],
                    'c': ['yourstr', 'mystr', 'theirstr']  },
                    index=['r1', 'r2', 'r3'])


