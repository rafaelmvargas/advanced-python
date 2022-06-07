# 5.29:  Understanding *args and **kwargs:  the below function
# has 2 positional arguments and 2 keyword arguments, and
# prints the arguments inside the function.  Call the function
# as shown, and see the the arguments printed.  Now replace
# the arguments in the signature with *args and **kwargs and
# print the variables args and kwargs inside the function.

def printargs(w, x, y=0, z=None):

    print(w, x, y, z)


printargs(5, 10, y=100, z='Hello!')

