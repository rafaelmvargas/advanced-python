# 9.3:  use pd.to_numeric.  Change the 'a' and 'b' columns to
# a numeric type, and show dtypes afterwards.

import pandas as pd

dol = {  'a': ['1', '2', '3'],
         'b': ['2.9', '3.5', '4.9'],
         'c': ['yourstr', 'mystr', 'theirstr']  }

df = pd.DataFrame(dol, index=['w', 'x', 'y'])



