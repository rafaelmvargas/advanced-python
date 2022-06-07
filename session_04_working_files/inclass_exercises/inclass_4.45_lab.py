# 4.45:  Match those lines that contain a 7-digit hex number
# (a-fA-F0-9).

import runreport

import re

lines = [
    'The color code is #ABF2307.',
    'Mr. Mxyzptlk is 999 years old today.',
    'The memory address is fc9d223.'
]

for line in lines:
    if re.search(r'', line):
        print(line)

# Expected Output:

# The color code is #ABF2307.
# The memory address is fc9d223.

