# 8.39:  Use a conditional (boolean test) in a subscript to
# select only those rows in the FF DataFrame that have a Mkt-
# RF value > 0.  Use .head() on the resulting DataFrame slice
# to see its first rows.

import pandas as pd

df = pd.read_csv('../F-F_Research_Data_Factors_daily.txt', sep='\s+',
                    header=3, skipfooter=2, engine='python')


# This type of slicing is done for read-only purposes (use
# .loc[] if you intend to write to the slice).

