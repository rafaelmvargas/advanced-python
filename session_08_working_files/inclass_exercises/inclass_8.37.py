# 8.37:  Use .loc[] indexing to select a 2-dimensional slice
# of the first 3 rows (use a range between 19270701 and
# 19270706) and SMB and HML columns of the DataFrame.

import pandas as pd

df = pd.read_csv('../F-F_Research_Data_Factors_daily.txt', sep='\s+',
                    header=3, skipfooter=2, engine='python')


