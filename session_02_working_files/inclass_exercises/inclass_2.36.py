# 2.36:  View and loop through list of dicts.  Open
# weather_newyork_lod.json in a text editor or PyCharm.  This
# is a list of dicts -- a list where each item in the list is
# a dict.

# Now open this file in Python and load the JSON into a Python
# object with json.load().
# 
# Loop through the list of dicts and print each dict.

import json

fh = open('../weather_newyork_lod.json')
lod = json.load(fh)

for inner_dict in lod:
    print(inner_dict)

