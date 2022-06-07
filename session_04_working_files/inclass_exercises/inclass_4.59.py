# 4.59:  Retrieve a grouping with .groups().

# Extract city, state zip from line.

import re

line = 'Los Angeles, CA  91604'
matchobj = re.search(r'', line)
print(matchobj.groups())

# Expected Output:

# ('Los Angeles', 'CA', '91604')

# Note that if you see the message AttributeError: 'NoneType'
# object has no attribute 'group', this means that the search
# did not find a match and returned None, and the code
# attempted to call .group() on None.  Check the string and
# pattern to determine why it did not match.

