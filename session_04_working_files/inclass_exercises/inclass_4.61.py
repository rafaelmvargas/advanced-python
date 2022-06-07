# 4.61:  Group and extract with findall().

# Extract email addresses only for nyu.edu.

import re

text = """There are many ways to contact us.  Use the
general email contact@nyu.edu, or email our public
liason at help@nyu.edu.  If you need tech support you
can reach us at askits@nyu.edu.
Author:  Joe Wilson joe@wilson.com"""

emails = re.findall(r'', text)
print(emails)

# Expected Output:

# ['contact@nyu.edu', 'help@nyu.edu', 'askits@nyu.edu']

