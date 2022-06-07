# 4.42:  Escape quantifier character *.

# Match on all lines with asterisked footnotes.

import re

numbers = [
    'As Ibid* said,',
    'there should be no greater good ',
    'than compassion*, love, ',
    'mutual benefit*',
    'and the profit-making motive.',
]
for num in numbers:
    if re.search(r'', num):
        print(num)

# Expected Output:

# As Ibid* said,
# than compasssion*, love,
# mutual benefit*

