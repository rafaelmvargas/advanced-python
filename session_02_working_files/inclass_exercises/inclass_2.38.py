# 2.38:  View and loop through a dict of dicts.  Open
# weather_newyork_dod.json in a text editor or PyCharm.  This
# is a dict of dicts -- a dict where each key in the dict is a
# string, and each value in the dict is a dict.

# Now open this file in Python and load the JSON into a Python
# object with json.load().
# 
# Loop through the dict of dicts and print each key and
# associated value in the dict.

import json

fh = open('../weather_newyork_dod.json')
dod = json.load(fh)


