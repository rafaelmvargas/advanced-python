# 4.26:  "Zero or one" quantifier.

# Without using a character class (or grouped alternates), use
# a single regex that matches on each string that has 'a' or
# 'an' followed by a space.

import re

lines = [
    'This is a wonderful thing. ',
    "I haven't seen anything like it. ",
    "Isn't it an exceptional experience? "]

for line in lines:
    if re.search(r'', line):
        print(line)

# Expected Output:

# This is a wonderful thing.
# Isn't it an exceptional experience?

