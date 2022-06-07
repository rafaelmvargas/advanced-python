# 6.12:  Create a class method.

# Add a class method classincrement(cls) that uses its cls
# argument to increment the cattr class variable (cattr will
# be found to be an attribute of cls.
# 
# Call classincrement() through the instance obj as well as
# through the class MyClass.
# 
# The values printed below should both be 1.
# 
# Before this can work as shown, however, you must decorate
# classincrement() with @classmethod.

class MyClass:
    cattr = 0

    # your classincrement(cls) method here


obj = MyClass()


obj.classincrement()

print(obj.cattr)          # should be 1
print(MyClass.cattr)      # should be 1

# Expected Output:

# 1
# 1

