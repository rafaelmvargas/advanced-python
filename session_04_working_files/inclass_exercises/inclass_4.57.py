# 4.57:  Match on non-search character.

# Perform the same extraction on the below text by searching
# for a bracket followed by one or more non-brackets.  Text
# extracted should be the same.

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

