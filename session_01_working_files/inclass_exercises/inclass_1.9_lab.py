# 1.9:  Use a 'for' loop to count lines in a file.  Using an
# integer counter with a for loop, count and print the number
# of data lines in ad_buys.csv (hint:  use next() to skip the
# header line).

import runreport

fname = "../ad_buys.csv"

fh = open(fname)
header = next(fh)

line_count = 0

for line in fh:
    line_count += 1

print(line_count)


# Expected Output:

# 15
