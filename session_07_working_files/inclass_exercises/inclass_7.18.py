# 7.18:  Allow a class to "print" itself.  Define a
# __str__(self) method that returns a string.  Now print the
# object.

class Value:
    def __init__(self, val):
        self.aaa = val

    def getval(self):
        return self.aaa

mynum = Value(10)



