# 5.21:  Use a lambda to sort a dict by value.

# As you know, sorting a dict means sorting its keys.  Write a
# lambda that expects a dict key as argument, and returns the
# value for that key as return value.

d = {'a': 10, 'b': 2, 'c': 5}

skeys = sorted(d, key=# your lambda function here)

print(skeys)        # ['b', 'c', 'a'] (in order of value, low-to-high)


