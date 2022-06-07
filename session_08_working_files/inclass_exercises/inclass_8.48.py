# 8.48:  Sum up the 'a' column.

import pandas as pd

df = pd.DataFrame({ 'a': [1, 2, 3, 4, 5, 6],
                    'b': [2.9, 3.5, 4.9, 4.1, 2.1, 3.0],
                    'c': ['CA', 'CA', 'OR', 'OR', 'WA', 'WA']  },
                    index=['r1', 'r2', 'r3', 'r4', 'r5', 'r6'])

