# 8.16:  Use pd.read_csv() to read a DataFrame from
# FF_abbreviated.txt.  Note that the separator is whitespace
# -- separator (sep= argument) must be '\s+' (a regex for "one
# or more spaces").  After creating the DataFrame, use the
# .columns attribute to set column labels:  date, Mkt-RF, SMB,
# HML, RF.

import pandas as pd

df = pd.read_csv('../FF_abbreviated.txt')


