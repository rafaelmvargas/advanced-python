# 5.15:  Given the below list, sort line_list by the number at
# the end of each line.  Loop through and print the sorted
# list.  (Hint:  call sorted() on line_list, and make your
# key= value the name of a custom function that takes the line
# as an argument and returns the value of the number at the
# end of the line.  Your custom function will simply take an
# arg (that will be a string, the line from the file), split
# the line into elements, and return the last element as an
# integer.

line_list = [
   'the value 3',
   'this value 1',
   'that value is 4',
   'the value here is 2'
]

# your code here


# Expected Output:

# line_list = [
#    'this value 1',
#    'the value here is 2',
#    'the value 3',
#    'that value is 4'
# ]

