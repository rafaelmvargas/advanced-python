# 2.43:  Build a dict of dicts.  Adapting what you did in the
# prior solution, now loop through the file and build a dict
# of header keys and row values for each data row in the
# revenue.csv file.  Print each of the dicts as you build
# them.

# Now initialize a new empty dict before the loop begins.  As
# you build each dict, add the "inner" dict to the "outer"
# dict:  make the company name the key in the "outer" dict,
# and the value the "inner" dict.
# 
# Print the resulting structure once completed.
# 
# Finally, use print(json.dumps(dod, indent=4)) to print the
# structure in a friendly ("pretty") format.

import csv
import json

fh = open('../revenue.csv')
reader = csv.reader(fh)

dod = {}

header = next(reader)


