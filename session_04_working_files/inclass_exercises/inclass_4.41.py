# 4.41:  Escape quantifier character +.

# Match on all lines with positive numbers.

import re

numbers = [
    'Amount:  -23.9',
    'Amount:  +43.8',
    'Amount:  -9.03',
    'Amount:  +99.9',
    'Amount:  +22.0'
]
for num in numbers:
    if re.search(r'', num):
        print(num)

# Expected Output:

# Amount:  +43.8
# Amount:  +99.9
# Amount:  +22.0

