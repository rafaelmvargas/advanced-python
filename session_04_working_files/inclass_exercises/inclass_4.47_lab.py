# 4.47:  Without using a character class, match on each string
# that ends in .jpg or .JPG (try this another way).

# (hint: use the flag argument (the optional 3rd argument) to
# re.search())

import runreport

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

# myfile.jpg
# yourfile.JPG
# count: 2

