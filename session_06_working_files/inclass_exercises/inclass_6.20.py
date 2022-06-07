# 6.20:  Create a module that holds a class.

# Add the below class to temputils.py.

# class TempConvert:
# 
#     def __init__(self, temp, scale='F'):
#         self.itemp = temp
#         self.scale = scale
# 
#     def as_fahrenheit(self):
#         """ function to convert celsius to fahrenheit """
#         if self.scale == 'F':
#             return self.itemp
#         return (self.itemp * 9 / 5) + 32
# 
#     def as_celsius(self):
#         """ function to convert fahrenheit to celsius """
#         if self.scale == 'C':
#             return self.itemp
#         return (self.itemp - 32) * 5 / 9

# Then import the class and use it as indicated below.

import temputils as tu


# construct a TempConvert object as 32 degrees Fahrenheit

# call .as_celsius() to see the value 0


# construct a Tempconvert object as 100 degrees Celsius

# call .as_fahrenheit() to see the value 212


# Expected Output:

# 0.0
# 212.0

