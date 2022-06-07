# 5.18:  Convert a function to lambda.

# The following function takes one argument and returns the
# value doubled.  Convert to lambda and use in the map()
# function.

def doubleit(arg):
    return arg * 2

seq = [1, 2, 3, 4]

seq2 = map(doubleit, seq)   # replace doubleit with a lambda here

print(list(seq2))           # [2, 4, 6, 8]

