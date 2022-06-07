# 2.41:  Build a dict from a CSV file with CSV header keys.
# Use csv to open revenue.csv in a Python file and select out:
# the header row and the first data row (hint:  use next() on
# the reader object to get one line at a time from the file).

# Now build a dict from the header row and first data row with
# keys that match the header line.
# 
# Tip:  use dict(zip(headers, data_row)) to build the dict:
# zip() takes two lists and "zips" them together like a zipper
# to pair up the first items in each list, the second items in
# each list, etc.  zip(headers, data_row) will pair up the
# column heads with data from the row, and passing this to
# dict() will transform to a dictionary.

import csv

fh = open('../revenue.csv')
reader = csv.reader(fh)


