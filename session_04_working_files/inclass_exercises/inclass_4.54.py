# 4.54:  Group for extraction.  In one regex match, extract
# the IP address from this log line.

import re

line = '172.26.93.208 - - [28/Jun/2012:21:00:17 -0400] "GET /~cmk380/pythondata/image2b.txt HTTP/1.1" 200 30'

matchobj = re.search(r'', line)

if matchobj:
    print(matchobj.group(1))

# Expected Output:

# 172.26.93.208

# Note that if you see the message AttributeError: 'NoneType'
# object has no attribute 'group', this means that the search
# did not find a match and returned None, and the code
# attempted to call .group() on None.  Check the string and
# pattern to determine why it did not match.

