# 7.24:  (Review) Trap the exception.  First, run the script
# to see what exception is raised.  Then, use a try/except
# statement to trap the error.  In the except block, set xi to
# 1.

x = input('please enter an integer: ')

xi = int(x)

print(f'{xi} * 2 = {xi * 2}')

# PLEASE DO NOT USE except: BY ITSELF!  This works, but we
# must always specify the exception we are expecting.
# 
# To test, run the program once with "correct" input (i.e.,
# numbers only) and then run it again with "bad" input (i.e.,
# letters) to trigger the exception.

