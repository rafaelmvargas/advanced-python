# 7.12:  Cause class Do to inherit from the builtin class
# list.  See if the list .append attribute is available in the
# instance.


class Do(list):
    def append(self,val):
        list.append(self, str(val))


x = Do()
x.append(5)
x.append(10)
print(x)
