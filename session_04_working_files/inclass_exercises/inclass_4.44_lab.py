# 4.44:  Ignore comment lines:  print only those lines that
# don't start with a comment (the first non-space character is
# a hash mark).

import runreport

import re

text = """
# this is a program to do stuff
a = 5
b = 10              # an int
if True:
    # multiply them
    c = a * b
"""

for line in text.splitlines():
    if not re.search(r'', line):
        print(line)


# Expected Output:

# a = 5
# b = 10              # an int
# if True:
#     c = a * b

