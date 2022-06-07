# 7.26:  Trap the exception, then raise a new one.  Inside the
# except block, raise another KeyError, or any existing
# exception that you choose.

keydict = {'a': 1, 'b': 2, 'c': 3}

x = input('please enter a key for this dict: ')

try:
    val = keydict[x]
except KeyError:
    print('uh-oh')   # replace this code

print(f'the value for {x} is {val}.')

