# 4.53:  Group for extraction.  Extract the Catalog ID and
# Publication Date from the text line.

import re

rs_row = 'Catalog ID: 2839-587    Pub. Date: 2019-09-03'

matchobj = re.search(r'', rs_row)

if matchobj:
    print(matchobj.group(1))
    print(matchobj.group(2))

# Expected Output:

# 2839-587
# 2019-09-03

# Note that if you see the message AttributeError: 'NoneType'
# object has no attribute 'group', this means that the search
# did not find a match and returned None, and the code
# attempted to call .group() on None.  Check the string and
# pattern to determine why it did not match.

