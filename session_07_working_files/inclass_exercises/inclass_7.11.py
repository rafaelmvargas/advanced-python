# 7.11:  Compare dir() of Do to dir() of object.  Is one a
# subset of the other?

"""
    if a class does not inherit from any class explicitly,
    then it *implicitly* inhereits from class 'object'
"""


class Do:
    pass


print(dir(Do))

print(dir(object))