# 4.46:  Show those lines that contain two capitalized words
# (as in a name).

import runreport

import re

lines = [
    'The owner is Gwen Harstridge.',
    "There aren't a lot of stores like this one.",
    'Paris is not a lot like Rome.',
    'I hail from Los Angeles, California.'
]

for line in lines:
    if re.search(r'', line):
        print(line)

# Expected Output:

#     The owner is Gwen Harstridge.
#     I hail from Los Angeles, California.

