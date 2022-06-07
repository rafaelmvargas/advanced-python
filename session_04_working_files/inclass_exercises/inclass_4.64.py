# 4.64:  DOTALL wildcard match.

# Extract everything between =code start= and = code end =.
# Use the re.DOTALL switch to use the wildcard (.) to match on
# a newline.

import re

text = """Title of This Text

This is some description...

=code start=
a = 5
b = 5.0
if a == b:
    print('yes')
=code end=

This is some discussion...
"""

matchobj = re.search(r'', text)

print(matchobj.group(1))

# Expected Output:

# a = 5
# b = 5.0
# if a == b:
#     print('yes')

