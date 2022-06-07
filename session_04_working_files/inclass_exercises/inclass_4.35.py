# 4.35:  Custom quantifier.

# Match on strings that have a capital letter followed by two
# or more lowercase letters.

import re

match_strings = [
    'hello World 00',
    'goodbye As world    ',
    'To 23 bonjour',
    'wilkommen23  ',
    'Aloha',
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

# hello World 00
# Aloha
# Que 3 Tal!
# count: 3

