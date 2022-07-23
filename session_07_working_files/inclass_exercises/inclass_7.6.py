# 7.6:  Do is a class object; the class has a cval attribute
# assigned as a class variable.  Investigate the class'
# attributes with the following tools:

#   1. regular attribute lookup (i.e., .cval)
#   2. dir()
#   3. Do.__dict__.keys()
#
#


class Do:

    cval = 5  # class variables / class attributes

    def dothis(self):  # class variables / class attributes
        self.a = [1, 2, 3]
        print("done!")


x = Do()
x.dothis()
x.var = 500
print(x.__dict__)
