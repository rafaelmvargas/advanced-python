# 4.33:  Quantifiers with anchors (3).  Match on each string
# that consists only of non-spaces.

import re

match_strings = [
    'hello world 00',
    'goodbye world    ',
    ' 23 bonjour',
    'wilkommen23  ',
    'aloha',
    '99',
    '00',
    '88557799',
    'Que 3 Tal!',
    'myfile.jpg',
    'yourfile.JPG'
]

count = 0
for string in match_strings:
    if re.search(r'', string):
        print(string)
        count += 1
print(f'count:  {count}')

# Expected Output:

# aloha
# 99
# 00
# 88557799
# myfile.jpg
# yourfile.JPG
# count: 6

