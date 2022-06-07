# 8.53:  Use .sort_values() to sort the DataFrame by the 'x'
# value.  Use ascending=False to reverse the sort.

import pandas as pd

df = pd.DataFrame({ 'g': [7, 5, 1, 8],
                    'x': [2.9, 4.9, 3.5, 0],
                    'b': ['yourstr', 'mystr', 'theirstr', 'mystr']  },
                    index=['r9', 'r5', 'r1', 'r3'])


