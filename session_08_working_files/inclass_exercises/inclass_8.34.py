# 8.34:  Slice the first 3 rows of the FF DataFrame using
# standard slice syntax with integers (i.e., 0:3.

import pandas as pd

df = pd.read_csv('../F-F_Research_Data_Factors_daily.txt', sep='\s+',
                    header=3, skipfooter=2, engine='python')


# This type of slicing is done for read-only purposes (use
# .loc[] if you intend to write to the slice).

