# 4.23:  Match on date format MM/DD/YY (and not 4-digit year).

import runreport

import re

dates = ['Jan. 3, 2018', '23-Mar-17', '12/02/98', '12/03/1998', '23.17.2018']
for date in dates:
    if re.search(r'', date):
        print(date)

# Expected Output:

# 12/02/98

