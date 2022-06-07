# 5.14:  Experiential exercise.  Please run the following
# code:

def my_element_modifier(arg):
    lower_arg = arg.lower()
    print(f'sorting element "{arg}" by value "{lower_arg}"')
    return lower_arg

sorted_list = sorted(['e', 'c', 'D', 'B', 'a'],
                     key=my_element_modifier)
print(sorted_list)

# Note the output:

# sorting element "e" by value "e"
# sorting element "c" by value "c"
# sorting element "D" by value "d"
# sorting element "B" by value "b"
# sorting element "a" by value "a"
# 
# ['a', 'B', 'c', 'D', 'e']

# This exercise demonstrates that my_element_modifier() was
# called once for every element, in this case 5 times.  arg is
# assigned each element in turn.  And the value returned from
# my_element_modifier() is the value by which each element is
# sorted -- so 'a' is sorted by the value 'a', 'B' is sorted
# by the value 'b', 'c' by 'c', 'D' by 'd'.  This facilitates
# the alphabetic sorting of these values.  The values
# themselves don't change, but Python sorts according to the
# value returned from the function.
# 
# If this makes sense to you, please go back to the previous
# examples and link this understanding to the other functions
# and methods we've used before -- using int, len, str.upper,
# etc.  They are all passing a function to be applied to each
# element, and Python is sorting by the value returned from
# the function or method.

