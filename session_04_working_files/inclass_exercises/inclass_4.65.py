# 4.65:  Multiline anchors.

# Use findall() to extra numbers from only the start of each
# line of the text.  Use re.MULTILINE to allow the carrot (^)
# to match at the start of any line.

import re

text = """Title of This Text

23 we want to grab some 99 numbers
12 but not others, 17 and then some
5  so we just get 1 the ones
on the left side

93 and me and 23 too

"""

matches = re.findall(r'', text)

print(matches)

# Expected Output:

# ['23', '12', '5', '93']

