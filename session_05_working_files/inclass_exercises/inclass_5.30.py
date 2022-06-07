# 5.30:  Same decorator function as last time --
# this_function() has been defined to take two positional
# arguments and two keyword arguments, printing these
# arguments inside this_function()).  Inside wrapper(), we
# accept these arguments and pass them to myfunc() (which is
# this_function().  Run this program to see that it works.
# Now replace the positional arguments with *args and the
# keyword arguments with **kwargs and see that it works in the
# same way.

def my_decorator(func):             # func:  function, 'whoop'

    def wrapper(*args, **kwargs):   # args: tuple, (5, 10); kwargs: dict, {'x': 99, 'y': 'hey!'}
        print("Something is happening before whoop() is called.")

        func(*args, **kwargs)       # calling whoop(5, 10, x=99, y='hey!')

        print("Something is happening after whoop() is called.")

    return wrapper                  # return function 'wrapper'

@my_decorator                       # replacing whoop with wrapper
def whoop(a, b, x=None, y=None):
    print(f"Wheee!:  {a}, {b}, {x}, {y}")


# calling the replacement function
whoop(5, 10, x=99, y='hey!')        # calling wrapper(5, 10, x=99, y='hey!')

