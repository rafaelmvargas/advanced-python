# 5.27:  Demo:  a "decorator" function -- a function that both
# takes a function as argument and returns a function as
# return value.  Use the prior concepts (regarding passing a
# function reference to another function and returning a
# function reference from a function) to understand what is
# happening here.

def my_decorator(func):    # func: function, 'whoop'

    def wrapper():
        print("Something is happening before whoop() is called.")

        func()             # calls 'whoop'

        print("Something is happening after whoop() is called.")

    return wrapper         # return function 'wrapper'


def whoop():
    print("Wheee!")


# now the same name points to a replacement function
whoop = my_decorator(whoop)          # function 'wrapper'

# calling the replacement function
whoop()                              # (calls function wrapper)


