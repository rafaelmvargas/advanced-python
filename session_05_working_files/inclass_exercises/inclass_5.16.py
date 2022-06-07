# 5.16:  Sort the lines of the file pyku.txt by the number of
# words on each line.  (Hint:  write a custom sort function
# that takes a single line of text, splits the line into a
# list, and returns the length of the list.  Pass the
# readlines() of the file to the sorted() function.)  Also
# here I am using rstrip() to strip each line before printing.

fh = open('../pyku.txt')

lines = fh.readlines()

# your code here


# Expected Output:

# We're out of gouda.
# Spam, spam, spam, spam, spam.
# This parrot has ceased to be.

