# 1.3:  Loop through a file, split out a column and add to a
# sum.  Take the following steps, running the program and
# verifying the result after each step:

#   1. Loop through the file revenue.csv and print each line.
# Note that there is an extra blank line after each printed
# line (this is the newline character)
#   2. Before printing, use .rstrip() to strip the line of its
# newline character. Print the line to see that the blank line
# has been omitted.
#   3. Split each line on a comma, and print the resulting
# list.
#   4. Subscript each list for the float value, and print the
# value from each line.
#   5. Set a float variable to 0 before the loop begins, and
# add each split value to the float variable (make sure to
# convert to float first).
#   6. Print the resulting sum.
# 
# 
# 
# The result should be 662.0100000000001 --
# your remainder may be slightly different.

fname = '../revenue.csv'

fh = open(fname)

for line in fh:
    line = line.rstrip()
    # your loop code here



# (Note:  use the next() function with the filehandle to
# advance the file pointer past the first row, which are
# headers)

