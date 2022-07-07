# 4.27:  "Zero or more" quantifier, quantifiers with anchor.

# Match on all strings that consist only of a 1 followed by
# zero or more digits.

import re

numbers = [
  '100',
  '135',
  '31',
  '1',
  '1 think',
]

for val in numbers:
    if re.search(r'1\d+', val):
        print(val)

# Expected Output:

# 100
# 135
# 1
# 1 think

