# 8.64:  Review the below baby names concatenated DataFrame,
# then group the baby names by gender, then sort the resulting
# dataframe by this value, descending.

import pandas as pd

df18 = pd.read_csv('../baby_names/yob2018.txt',
                   names=['name', 'gender', 'count'])
df18['year'] = '2018'

df17 = pd.read_csv('../baby_names/yob2017.txt',
                   names=['name', 'gender', 'count'])
df17['year'] = '2017'

df = pd.concat([df18, df17])

