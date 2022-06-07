# 8.36:  Use .loc[] indexing to select the Mkt-RF and SMB
# columns of the DataFrame.  Indicate "all rows" by using the
# empty slice : in the rows position.  Use .head() on the
# resulting DataFrame slice to see its first rows.

import pandas as pd

df = pd.read_csv('../F-F_Research_Data_Factors_daily.txt', sep='\s+',
                    header=3, skipfooter=2, engine='python')


