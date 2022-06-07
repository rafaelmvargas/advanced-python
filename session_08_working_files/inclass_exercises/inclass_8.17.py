# 8.17:  Now use read_csv() to read
# F-F_Research_Data_Factors_daily.txt, using the skiprows= and
# skipfooter= arguments to omit the 4 header lines and 2
# footer lines.  (Note that using these latter arguments
# require you also add engine='python' to suppress a warning.)

import pandas as pd

df = pd.read_csv('../FF_Research_Data_Factors_daily.txt', sep='\s+')


# Note that skipping 4 lines asks pandas to start reading on
# the 5th line, where the table headers are -- these are
# automatically set as the headers for the table.  The date is
# set as the index.

