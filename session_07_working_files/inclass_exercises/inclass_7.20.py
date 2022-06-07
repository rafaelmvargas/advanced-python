# 7.20:  Replace getval() with __getitem__().  The method
# should take one argument (besides self) and return the .aaa
# attribute.  Now attempt to subscript the object.

class Value:
    def __init__(self, val):
        self.aaa = val

    def getval(self):
        return self.aaa

mynum = Value('10')

val = mynum.getval()      # 10

# uncomment after adding __getitem__
# val = mynum['whaeva']      # 10

