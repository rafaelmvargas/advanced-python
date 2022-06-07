# 1.19:  Use csv module to read a file.  Take the following
# steps, testing as you go:

#   1. Open a file and pass the file object to csv.reader()
#   2. Loop through the reader object line by line, printing
# each line. Note the type of the object representing each
# row.
#   3. Subscript the float value from each list and convert to
# float.
#   4. Initialize a float variable 0.0 at the top and add each
# float value to it inside the loop, producing a sum.
# 

import csv

fh = open('../revenue.csv')


