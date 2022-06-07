# 5.19:  Convert another function to lambda.

# The below function by_last_float() takes a string argument
# and returns a portion of that string (converted to float) as
# return value.  Replace this function with a lambda.

revenue = '../revenue.csv'

def by_last_float(line):
    words = line.split(',')
    return float(words[-1])

fh = open(revenue)
lines = fh.readlines()
for line in sorted(lines, key= # your lambda function here):
    line = line.rstrip()
    print line

