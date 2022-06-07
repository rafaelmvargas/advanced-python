# 7.25:  (Review) Trap the exception.  Again, determine the
# exception type that will occur if the user types in a key
# that doesn't exist in the dict.  Then use the try/except to
# trap the exception (PLEASE DO NOT USE except: BY ITSELF).
# If the exception is raised, assign None to val.

keydict = {'a': 1, 'b': 2, 'c': 3}

x = input('please enter a key for this dict: ')

val = keydict[x]

print(f'the value for {x} is {val}.')

