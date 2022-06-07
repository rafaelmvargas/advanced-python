# 4.56:  Work with wildcard and minimal match.

# Use the wildcard to match everything between the first two
# brackets.  Note carefully what was printed.  (Don't forget
# that square brackets must be escaped with a backslash, and
# that extraction requires grouping parentheses.)

import re

text = 'Discussion of terms <TO COME> after something <PLEASE REVIEW>.'

matchobj = re.search(r'', text)

print(matchobj.group(1))

# Expected Output:

# TO COME

# Note that if you see the message AttributeError: 'NoneType'
# object has no attribute 'group', this means that the search
# did not find a match and returned None, and the code
# attempted to call .group() on None.  Check the string and
# pattern to determine why it did not match.

