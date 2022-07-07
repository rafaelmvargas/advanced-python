# 4.17:  Loop through and print only lines with some text (not
# including spaces).

import runreport

import re

text = """line 1
line 2,

line 3...

line4!"""

lines = text.splitlines()

for line in lines:
    if re.search(r'\S', line):
        print(line)

# Expected Output:

# line 1
# line 2,
# line 3...
# line4!

