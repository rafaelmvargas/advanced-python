# 9.2:  Use Series .astype().  Change the 'a' column to
# np.float64, and 'b' column to str; check dtypes before and
# after the operation.

import pandas as pd
import numpy as np

dol = {  'a': [1, 2, 3],
         'b': [2.9, 3.5, 4.9],
         'c': ['yourstr', 'mystr', 'theirstr']  }

df = pd.DataFrame(dol, index=['w', 'x', 'y'])



