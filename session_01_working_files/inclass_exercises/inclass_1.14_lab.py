# 1.14:  Evaluate each word in a file.  Split pyku.txt into
# words, then use a 'for' loop to print each word that has
# more than 4 letters (after stripping punctuation).

import runreport

fname = "../pyku.txt"
fh = open(fname)

text = fh.read().split()

for word in text:
    clean_word = word.rstrip(".,")
    if len(clean_word) > 4:
        print(clean_word)


# Expected Output:

# We're
# gouda
# parrot
# ceased
