# 8.41:  Use .isin() (with the Series as argument) in a filter
# to show only those rows where the 'c' value is 'yourstr' or
# 'mystr'.

import pandas as pd

df = pd.DataFrame({ 'a': [1, 2, 3],
                    'b': [2.9, 3.5, 4.9],
                    'c': ['yourstr', 'mystr', 'theirstr']  },
                    index=['r1', 'r2', 'r3'])


