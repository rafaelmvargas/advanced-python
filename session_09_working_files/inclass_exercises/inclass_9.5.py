# 9.5:  Convert another function to lambda.  The following
# function takes a dict key and returns the value.  Convert to
# a lambda for use in the sorted() function.

d = {'a': 10, 'b': 2, 'c': 5}

def byvalue(arg):
    return d[arg]

skeys = sorted(d, key=byvalue)

print(skeys)        # ['b', 'c', 'a'] (in order of value, low-to-high)


