# 1.11:  Use a 'for' loop to print first word from each line
# in a file.  Loop through and print just the first word from
# the file pyku.txt.

import runreport

fname = "../pyku.txt"

fh = open(fname)


for line in fh:
    line_words = line.rstrip().split()
    first_word = line_words[0].rstrip(",")
    print(first_word)


# Expected Output:

# We're
# This
# Spam

# Please note that there is no comma after the word 'Spam'
