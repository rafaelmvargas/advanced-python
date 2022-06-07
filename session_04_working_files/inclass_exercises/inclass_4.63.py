# 4.63:  Regex split.  Split the user-input comma-separated
# values string into separate digit values.

import re

ui = '23, 14, 7,3,9'
numbers = re.split(r'', ui)
print(numbers)

# Expected Output:

# ['23', '14', '7', '3', '9']

