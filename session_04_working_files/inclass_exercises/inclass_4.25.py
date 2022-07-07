# 4.25:  "One or more" quantifier.  Match on each string that
# has one or more letters in it.

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
    if re.search(r'[a-zA-Z]+', string):
        print(string)
        count += 1
print(f'count:  {count}')

# Expected Output:

# hello world 00
# goodbye world
#  23 bonjour
# wilkommen23
# aloha
# Que 3 Tal!
# myfile.jpg
# yourfile.JPG
# count: 8

