# 4.50:  Quantifying a group.  Match on a number with two
# decimal places and possible thousandths separator (3.95,
# 3,200.95, etc.)

# First create a pattern that is 1 or more digits with comma
# separator (i.e. matching on 0,, 00, 000,) and group the
# number with parentheses; quantify the group to say that
# there is zero or more of these, followed by one or more
# digits, a period and 2 digits.  (Do not use a custom
# character class for this purpose.)

import re

values = ['23.9', '18.2', '23.95', '2,238,000.00', '15,382.92', 'joe', '6.05']  # list of str
for value in values:
    matchobj = re.search(r'', value)
    if matchobj:
        print(value)

# Expected Output:

# 23.95
# 2,238,000.00
# 15,382.92

# Note that if you see the message AttributeError: 'NoneType'
# object has no attribute 'group', this means that the search
# did not find a match and returned None, and the code
# attempted to call .group() on None.  Check the string and
# pattern to determine why it did not match.

