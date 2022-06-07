# 4.37:  Custom quantifier.  Having split the text into words,
# show those words that are greater than 7 characters in size.

import re

text = """This is the 1000th story, regarding a duck
named Quack.  It was unlikely that Quack could have been
given a name like that by his mother, so we can only conclude
that he was named by the author, who has a cuteness problem."""


words = text.split()
stripped = [ word.rstrip('.,') for word in words ]

for word in stripped:
    if re.search(r'', word):
        print(word)

# Expected Output:

# regarding
# unlikely
# conclude
# cuteness
# problem

