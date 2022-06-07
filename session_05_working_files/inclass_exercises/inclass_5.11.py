# 5.11:  Given your understanding that the key= argument to
# sorted() will in a sense process each element through
# whatever function we pass to it, sort the below list in
# alphabetical order and print it.

# (Hint:  this list will not sort alphabetically by default.
# We need a key= function that can modify each element in the
# list, and make them all the same case.  The string upper()
# method or lower() method can do the job.  To refer to this
# method, you can say str.upper or str.lower.  However, make
# sure not to actually call the method (which is done with the
# parentheses).  Instead, you simply refer to the method,
# i.e., mention the method without using the parentheses.)

charlist = ['F', 'e', 'c', 'a', 'B', 'D']

# your code here


# Expected Output:

# ['a', 'B', 'c', 'D', 'e', 'F']

# If you see this message:

# TypeError: descriptor 'upper' of 'str' object needs an argument

# it means that you added parentheses and attempted to call
# the str.upper or str.lower method.  Keep in mind that we
# don't call this method -- we give it to the sorted()
# function to call.  We're doing this because sorted() will
# use whatever function we wish, to modify each element for
# the purposes of sorting.  If we give it str.upper it will
# sort 'a' as 'A' and 'B' as 'B' and 'c' as 'C' -- this should
# indicate to you how we are able to use it for alphabetic
# sorting with mixed-case strings.

