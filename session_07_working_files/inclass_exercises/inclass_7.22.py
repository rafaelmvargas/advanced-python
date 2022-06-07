# 7.22:  Add an append() method to IntList to specialize the
# method.  Inside the method, only print a message; don't try
# to perform the append.

class IntList(list):
    pass

x = IntList()

x.append(5)       # now appending 5!
x.append(3)       # now appending 3!

print(x)          # [5, 3]

