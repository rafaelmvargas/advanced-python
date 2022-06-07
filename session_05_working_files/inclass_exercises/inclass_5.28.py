# 5.28:  Same function as last time -- this time use @ ("pie
# syntax") to produce a "true" Python decorator.  Place the
# decorator just above the function def for this_function, and
# remove the call to my_decorator().

def my_decorator(func):        # func:  function, 'whoop'

    def wrapper():
        print("Something is happening before whoop() is called.")

        func()                 # calls whoop()

        print("Something is happening after whoop() is called.")

    return wrapper             # return function 'wrapper'

@my_decorator
def this_function():
    print("Wheee!")


# calling the replacement function
this_function()                # (calls function wrapper)

