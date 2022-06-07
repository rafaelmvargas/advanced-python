# 4.52:  Group for extraction.

# Use a parenthetical grouping to extract the number from this
# text.

import re

line = '34:  this is a line of text'

matchobj = re.search(r'', line)
print(matchobj.group(1))

# Expected Output:

# 34

# Note that if you see the message AttributeError: 'NoneType'
# object has no attribute 'group', this means that the search
# did not find a match and returned None, and the code
# attempted to call .group() on None.  Check the string and
# pattern to determine why it did not match.

