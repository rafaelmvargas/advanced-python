# 4.55:  Demonstration:  "minimal" match.

# The below regex grabs the word Python from the text.  Run
# the code once to observe this.
# 
# Now add a question mark ? as the character directly after
# the "one or more" plus sign and run again - you should see
# that the "one or more word characters" pattern is now
# matching on as few characters as possible.

import re

text = 'My language is Python'

matchobj = re.search(r'', text)

print(matchobj.group(1))

# Expected Output:

# P

# Note that if you see the message AttributeError: 'NoneType'
# object has no attribute 'group', this means that the search
# did not find a match and returned None, and the code
# attempted to call .group() on None.  Check the string and
# pattern to determine why it did not match.

