# 7.19:  Allow an object to respond to subscripting.  Define a
# __setitem__(self) method that takes two arguments (besides
# self) and prints the two arguments.  Now attempt to
# subscript the object.


class Value:
    def __init__(self, val):
        self.aaa = val

    def __setitem__(self, key, val):
        print(f"key: {key}, value: {val}")

    def __getitem__(self, key):
        print(f'key: {key}')


mynum = Value(10)

mynum["a"] = 55  # prints "called __setitem__(a, 55)"
