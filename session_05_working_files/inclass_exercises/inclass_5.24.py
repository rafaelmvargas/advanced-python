# 5.24:  map() and filter() functions:  call below functions
# to see result.  Play with return value of functions to see
# altered result.

def doubleit(arg):
    return arg * 2

def is_positive(arg):
    if arg > 0:
        return True
    else:
        return False

proclist = [-3, -2, -1, 0, 1, 2, 3]

transformed_list = map(doubleit, proclist)

filtered_list = filter(is_positive, proclist)

print('* mapped list *')
print(transformed_list)

print()

print('* filtered list *')
print(filtered_list)

