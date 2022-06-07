# 4.16:  Match on each string that starts with a space.

import runreport

import re

lines = [  'this is the first line,',
           ' and this is the second line and',
           ' this is the third line.  '     ]

for line in lines:
    if re.search(r'', line):
        print(line)

# Expected Output:

#  and this is the second line and',
#  this is the third line.  '     ]

