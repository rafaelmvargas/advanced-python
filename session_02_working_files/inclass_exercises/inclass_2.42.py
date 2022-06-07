# 2.42:  Build a list of dicts.  Incorporating what you did in
# the previous assignment, now loop through the file and build
# a dict of header keys and row values for each data row in
# the revenue.csv file.  Print each of the dicts as you build
# them.

# Now initialize a new empty list before the loop begins.  As
# you build each dict, append the dict to the list.
# 
# Print the resulting structure once completed.
# 
# Finally, use print(json.dumps(lod, indent=4)) to print the
# structure in a friendly format.

import csv
import json

fh = open('../revenue.csv')
reader = csv.reader(fh)

lod = []

header = next(reader)


