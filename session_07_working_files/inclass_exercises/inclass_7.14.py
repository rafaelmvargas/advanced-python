# 7.14:  Examine the return value from the following function
# calls:  vars().keys(), locals().keys() (called from inside
# the function) and dir(builtins).

import builtins

a = 5
b = [1, 2, 3]

print('== vars().keys() ==')
print(vars().keys())
print()

def do():
    lvar = 500
    print('== locals().keys() ==')
    print(locals().keys())
    print()

do()

print('== dir(builtins) ==')
print(dir(builtins))

