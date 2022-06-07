# 8.8:  Use simple numeric slicing to see the 50th through
# 53rd rows from this large DataFrame.

import pandas as pd

df = pd.read_csv('../F-F_Research_Data_Factors_daily.txt', sep='\s+',
                 header=3, skipfooter=2, engine='python')



