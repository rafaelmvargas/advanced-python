# 8.18:  When read_csv() reads
# F-F_Research_Data_Factors_daily.txt, it notes that the 1st
# column of 10-digit dates are all digits, so it automatically
# makes it the index and converts the column to integer.
# After reading the CSV, check the dtype of the index with
# df.index.dtype.  Then use df.index.astype('str') to ask
# pandas to read the index as a string.

import pandas as pd

df = pd.read_csv('../F-F_Research_Data_Factors_daily.txt', sep='\s+',
                 header=3, skipfooter=2, engine='python')


