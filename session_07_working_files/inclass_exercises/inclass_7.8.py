# 7.8:  class What inherits from class Do.  Investigate the
# What instance attributes with the following tools:

#   1. regular attribute lookup (i.e., .cval)
#   2. dir()
#   3. Do.__dict__.keys()
#


class Do:

    dovar = 5

    def dothis(self):
        print("done!")


class What(Do):

    whatvar = 10

    def __init__(self):
        self.instval = 500


z = What()

print(dir(z))

z.instval   # 500 (found in the instance)
z.whatvar   # 10 (found in the class)
z.dovar     # 5 (found in the inherited class)



# 'attribute lookup'
# when we acces an attribute from an instance,
# the instance looks for that attribute from an instance,
# the instance looks for that attribute:

# all objects have attibutes
# instances have access to:
#   - their own attibutes
#   - the attibutes defined in its class
#   - the attibutes defined in any inherited classes