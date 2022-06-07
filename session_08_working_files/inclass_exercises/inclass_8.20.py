# 8.20:  Read a DataFrame from a json file.  The weather data
# has been saved as a list of dicts and a dict of dicts.  Read
# each file using .read_json() and the correct orient
# parameter.

# For a list of dicts, correct orient= parameter is 'records'.
# 
# For a dict of dicts, correct orient= parameter is 'index'.
# 
# List of dicts (weather_newyork_lod.json):

import pandas as pd

fh = open('../weather_newyork_lod.json')


# Dict of dicts (weather_newyork_dod.json):

import pandas as pd

fh = open('../weather_newyork_dod.json')


