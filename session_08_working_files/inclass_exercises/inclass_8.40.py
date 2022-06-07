# 8.40:  Use .loc[] indexing with a conditional (boolean test)
# to select only those rows with a 0.0 value in the Mkt-RF
# column.  Use .head() on the resulting DataFrame slice to see
# its first rows.

import pandas as pd

df = pd.read_csv('../F-F_Research_Data_Factors_daily.txt', sep='\s+',
                    header=3, skipfooter=2, engine='python')


