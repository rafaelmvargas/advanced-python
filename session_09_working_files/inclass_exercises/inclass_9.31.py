# 9.31:  Select rows based on partial date.  Given the below
# DataFrame, select rows with a straight subscript for the
# following:

#   * single date (put the date in any format)
#   * single year-month (for example, '2016-03')
#   * single year
#   * date range as a slice (for example, '2016-03-03':
# '2016-05-02')
# 

import pandas as pd

df = pd.read_csv('../weather_newyork_2016_2018.csv')

df.EST = pd.to_datetime(df.EST)

df = df.set_index('EST', drop=True)


