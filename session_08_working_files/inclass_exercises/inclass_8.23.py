# 8.23:  Reading the below data, use df.to_clipboard() to
# write the DataFrame data to clipboard.  Open a new Excel
# file and paste the data directly into the spreadsheet.

import pandas as pd

fh = open('../weather_newyork_dod.json')

df = pd.read_json(fh, orient='index')

df = df.set_index('date')

