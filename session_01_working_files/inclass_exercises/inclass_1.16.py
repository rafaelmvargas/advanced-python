# 1.16:  Evaluate objects in a boolean context.

# First, run the below code to see how each of the below
# variables converts to bool(), a function for converting to
# boolean (True/False) value.
# 
# Then, uncomment the code to see how each of the variables
# behaves in an if statement (boolean context, i.e. evaluating
# as True/False)

list_empty = []
list_full = [0, 0, 0]

dict_empty = {}
dict_full = {'a': None, 'b': None}

int_empty = 0
int_full = -1

str_empty = ""
str_full = '   '      # 3 spaces

for item in [list_empty, list_full, dict_empty, dict_full,
             int_empty, int_full, str_empty, str_full]:

    print(f'{item} in boolean context:  {bool(item)}')
    #if item:
    #    print(f'{item} resolves to True in an if test')
    #else:
    #    print(f'{item} resolves to False in an if test')
    print()

