# 5.12:  Given your understanding that the key= argument to
# sorted() will in a sense process each element through
# whatever function we pass to it, sort these strings by their
# length, and print the sorted list.

mystrs = ['I', 'was', 'hanging', 'on', 'a', 'rock']

# your code here


# Expected Output:

# ['I', 'a', 'on', 'was', 'rock', 'hanging']

# If you see this message:

# TypeError: len() takes exactly one argument (0 given)

# it means that you added parentheses and thus attempted to
# call the len function.  Keep in mind that we don't call this
# method -- we give it to the sorted() function to call.
# We're doing this because sorted() will use whatever function
# we wish, to modify each element for the purposes of sorting.
# If we give it len it will sort 'I' as 1, 'was' as 3,
# 'hanging' as 7, etc -- perfect for our purposes.

