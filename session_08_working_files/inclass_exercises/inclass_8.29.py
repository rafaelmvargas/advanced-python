# 8.29:  Use .set_index() to set the a column for the student
# DataFrame as the index for the DataFrame.   (This method
# returns the new, modified DataFrame.)

import pandas as pd

df = pd.DataFrame({ 'a': [1, 2, 3],
                    'b': [2.9, 3.5, 4.9],
                    'c': ['yourstr', 'mystr', 'theirstr']  },
                    index=['r1', 'r2', 'r3'])


