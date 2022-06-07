# 8.32:  Subscript the 19260701 row of the DataFrame using
# .loc[]. If you need to see the other row labels, use
# df.index or df.head()  (Note that the index values have been
# read as integers, not strings, so your index must be an
# integer.)

import pandas as pd

df = pd.read_csv('../F-F_Research_Data_Factors_daily.txt', sep='\s+',
                    header=3, skipfooter=2, engine='python')



