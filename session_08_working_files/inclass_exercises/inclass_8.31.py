# 8.31:  Subscript the 'HML' column of the DataFrame using
# subscript syntax (you may also try attribute syntax, i.e.
# df.HML.)  If you need to see the other column headings, use
# df.columns or df.head()

import pandas as pd

df = pd.read_csv('../F-F_Research_Data_Factors_daily.txt', sep='\s+',
                  skiprows=4, skipfooter=2, engine='python')



