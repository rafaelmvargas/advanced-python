# 4.51:  Quantifying a Group (2).  Write a single regex that
# matches on q, Q, quit, Quit, QUIT.  Do this without a
# character class and without the alternate vertical bar.

import re

x = input('Do you want to quit? ')     # str, 'QuIt' (sample input)

if re.search(r'', x):
    print("you're quitting!")
else:
    print("you failed to quit.")

# Expected Output:

# Do you want to quit? QuIt
# you're quitting!

