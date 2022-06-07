# 5.26:  greet has been returned from returnit.  Call greet
# outside the function.

def returnit():
    def greet():
        print('hello, world')
    return greet

x = returnit()

