# 8.42:  Use ~ (the tilde character) to reverse the above test
# so that we show only rows that are NOT 'yourstr' or 'mystr'.

import pandas as pd

df = pd.DataFrame({ 'a': [1, 2, 3],
                    'b': [2.9, 3.5, 4.9],
                    'c': ['yourstr', 'mystr', 'theirstr']  },
                    index=['r1', 'r2', 'r3'])

df2 = df.loc[ df.c.isin(['yourstr', 'mystr']) ]
print(df2)

