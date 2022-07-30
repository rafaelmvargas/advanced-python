# 8.7:  Use the .head() and .tail() methods to examine the
# DataFrame rows at the top and bottom of this DataFrame.

import pandas as pd

df = pd.read_csv('../FF_abbreviated.txt', sep='\s+')



print(df.head(3))