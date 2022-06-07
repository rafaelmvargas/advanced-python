# 7.23:  Call list.append() from within the inheriting class.
# From inside the IntList .append() method, call the append()
# method on the object by calling it on the parent class.
# (Don't call it on self or you will set up an endless loop.)

class IntList(list):
    def append(self, item):
        print(f'now appending {5}!')

x = IntList()

x.append(5)       # now appending 5!
x.append(3)       # now appending 3!

print(x)          # []

