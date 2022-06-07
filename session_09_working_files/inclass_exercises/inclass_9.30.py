# 9.30:  Converting a DataFrame column/index to Timestamp.
# View the below dataframe and note the date column EST.  Use
# pd.to_datetime() to convert the 'EST' series to Timestamps,
# then use .set_index() with the column name and drop=True to
# set the column as the index.  Check the dtype of the index.

import pandas as pd

df = pd.read_csv('../weather_newyork_2016_2018.csv')



