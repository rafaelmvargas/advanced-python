# 4.60:  Quantify for an optional group.

# Pull out all the info about each person (Favorite Color may
# not be there).

import re

results = [ 'Name: Joe;  Favorite Color:  Blue;  Employee ID: 2395',
            'Name:  Marie;  Employee ID: 2321',
            'Name:  Teneski; Favorite Color: Green;  Employee ID:  1913' ]

for row in results:
    matchobj = re.search(r'', row)
    print(matchobj.groups())

# Expected Output:

# ('Joe', 'Favorite Color:  Blue;  ', 'Blue', '2395')
# ('Marie', None, None, '2321')
# ('Teneski', 'Favorite Color: Green;  ', 'Green', '1913')

# Note that if you see the message AttributeError: 'NoneType'
# object has no attribute 'group', this means that the search
# did not find a match and returned None, and the code
# attempted to call .group() on None.  Check the string and
# pattern to determine why it did not match.

