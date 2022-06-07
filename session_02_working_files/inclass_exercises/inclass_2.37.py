# 2.37:  Print value from list of dicts.  Again open the file
# weather_newyork_lod.json in Python and load the JSON into a
# Python object with json.load().

# Loop through each dict in the list of dicts and print just
# the 'date' column.

import json

fh = open('../weather_newyork_lod.json')
lod = json.load(fh)


