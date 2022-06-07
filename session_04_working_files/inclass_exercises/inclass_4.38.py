# 4.38:  Custom Quantifier.

# A password must be 3-8 characters in length (letters,
# numbers and underscores are permitted).  Validate the below
# password attempts.

import re

attempts = [
    '1234',
    'hello_there',
    'password',
    'ok',
    'what?',
    'supercalifrag']

for password in attempts:
    if re.search(r'', password):
        print(f'{password}:  validated')

# Expected Output:

# 1234:  validated
# password:  validated

