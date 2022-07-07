# 4.24:  Determine whether selected word begins with a vowel.
# If so, prepend an 'an' rather an an 'a'.

import runreport

import re

words = ["apple", "pear", "orange", "kiwi", "elderberry", "carrot", "ugli fruit"]
for word in words:
    if re.search(r"^[aeiou]", word):
        prepend = "an"
    else:
        prepend = "a"
    print(f"{prepend} {word}")

# Expected Output:

# an apple
# a pear
# an orange
# a kiwi
# an elderberry
# a carrot
# an ugli fruit
