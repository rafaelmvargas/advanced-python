# 6.18:  Create a module that holds a function.

# Create a new file, temputils.py, that has the below
# functions def ctof() and def ftoc().  Place this file in the
# same folder as this exercise file (inclass_exercises if this
# is a .py file; notebooks_inclass_challege if this is a
# Jupyter notebook).

# Contents of temputils.py:

# def ctof(temp):
#     """ function to convert celsius to fahrenheit """
#     if not isinstance(temp, (int,float)):
#         raise TypeError('must be an int or float')
#     return (temp * 9 / 5) + 32
# 
# 
# def ftoc(temp):
#     """ function to convert fahrenheit to celsius """
#     if not isinstance(temp, (int,float)):
#         raise TypeError('must be an int or float')
#     return (temp - 32) * 5 / 9

import temputils as tu

val = tu.ftoc(212)
print(val)             # 100.0

val2 = tu.ctof(0)
print(val2)            # 32.0


# Expected Output:

# 100.0
# 32.0

