# 4.19:  Match on each line that ends with a space.

import runreport

import re

lines = [  'this is the first line, ',
           'this is the second line and',
           'this is the third line.  '     ]

for line in lines:
    if re.search(r'', line):
        print(line)

# Expected Output:

# this is the first line,
# this is the third line.

