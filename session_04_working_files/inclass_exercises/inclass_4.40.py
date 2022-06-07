# 4.40:  Escape end anchor (aka dollar sign).

# Match on strings that have a dollar amount, including two
# decimal places ($23.53).

import re

lines = [
    'The coat cost $239.50.',
    'The candy cost $1.93',
    "I didn't buy anything today.",
    '$1 sale',
    'I dream of $$$'
]

for line in lines:
    if re.search(r'', line):
        print(line)


# Expected Output:

# The coat cost $239.50.
# The candy cost $1.93

