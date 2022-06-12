# 1.13:  Use a 'for' loop to collect a value from each line in
# a file.  Collect a list of states from ad_companies.csv.

import runreport

fname = "../ad_companies.csv"
fh = open(fname)
next(fh)

list_of_states = []

for line in fh:
    state = line.rstrip().split(",")[3]
    list_of_states.append(state)

print(list_of_states)


# Keep in mind that since the state value is the last on each
# line, we must .rstrip() the line the remove the newline so
# that it doesn't remain attached to the state value.

# Expected Output:

# ['OR', 'OR', 'AZ', 'PA', 'AZ']
