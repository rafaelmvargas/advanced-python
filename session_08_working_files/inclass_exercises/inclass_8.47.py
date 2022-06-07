# 8.47:  Set new column 'd' to a + b for all non-'CA' rows;
# for 'CA' rows, 'd' should be 0.

# To do this, first establish column 'd' with 0 for all rows,
# then apply the conditional.

import pandas as pd

df = pd.DataFrame({ 'a': [1, 2, 3, 4, 5, 6, 7],
                    'b': [1.0, 2.9, 3.5, 4.9, 5.6, 6.8, 7.1],
                    'c': ['CA', 'CA', 'NY', 'NY', 'NJ', 'NJ', 'NV'] },
                    index=['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7'])


