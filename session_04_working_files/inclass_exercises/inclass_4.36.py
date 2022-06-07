# 4.36:  Custom quantifier.

# Print those numbers that are in the millions (i.e., 7 or
# more digits).

import re

nums = [
  '1',
  '10',
  '100',
  '1000',
  '10000',
  '100000',
  '1000000',
  '10000000'
]

for num in nums:
    if re.search(r'', num):
        print(num)

# Expected Output:

# 1000000
# 10000000

