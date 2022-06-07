# 8.55:  First view, then concatenate the two DataFrames
# vertically.

import pandas as pd

df = pd.DataFrame({ 'a': [1, 2, 3],
                    'b': [2.9, 3.5, 4.9],
                    'c': ['yourstr', 'mystr', 'theirstr']  },
                    index=['r1', 'r2', 'r3'])

df2 = pd.DataFrame({ 'b': [4, 5, 6],
                     'c': [7.8, 8.2, 9.1],
                     'd': ['thingy', 'thatty', 'flunky']  },
                     index=['r2', 'r3', 'r4'])




# Note that the indices are repeated - this can be changed
# using index manipulation (.rename(), .reindex(),
# .set_index().

