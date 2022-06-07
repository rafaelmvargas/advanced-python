# 8.57:  Read weather_newyork.csv into a DataFrame.  Use
# .reindex() to select just the EST, Max TemperatureF and Min
# TemperatureF columns (with all rows).  Use .rename() to
# rename these columns as 'date', 'max_temp' and 'min_temp'.
# Now add an additional column 'diff_temp' showing the
# difference between max and min.  Sort the DataFrame by this
# value, highest to lowest.

import pandas as pd

df = pd.read_csv('../weather_newyork.csv')

dfs = df.reindex(['EST', 'Max TemperatureF', 'Min TemperatureF'], axis=1)

dfs = dfs.rename(columns={ 'EST': 'date',
                            'Max TemperatureF': 'max_temp',
                            'Min TemperatureF': 'min_temp' })


