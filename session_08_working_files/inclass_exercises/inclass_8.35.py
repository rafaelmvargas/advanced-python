# 8.35:  Use .loc[] indexing with a list to select the first 3
# rows (19270701, 19270702 and 19270706) of the DataFrame.
# (Note that these have been read into the DataFrame as
# integers.)  Do this first by passing a list of the 3 index
# values, then by passing a slice starting with 19270701 and
# ending with 19270706.

import pandas as pd

df = pd.read_csv('../F-F_Research_Data_Factors_daily.txt', sep='\s+',
                    header=3, skipfooter=2, engine='python')


