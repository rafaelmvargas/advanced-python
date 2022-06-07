# 8.38:  Use .iloc[] indexing to select the 1st 5 rows and 1st
# 2 columns of the DataFrame.

import pandas as pd

df = pd.read_csv('../F-F_Research_Data_Factors_daily.txt', sep='\s+',
                    header=3, skipfooter=2, engine='python')


