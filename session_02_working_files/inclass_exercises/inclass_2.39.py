# 2.39:  Loop through a dict of dicts and print a value from
# each.  Again open the file weather_newyork_dod.json in
# Python and load the JSON into a Python object with
# json.load().

# Loop through each key and value in the dict of dicts and
# from each dict value print the 'mean_temp' value.

import json

fh = open('../weather_newyork_dod.json')
dod = json.load(fh)


