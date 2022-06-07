# 5.20:  Use a lambda to sort strings as floats.

# Given the below list of strings that have float values,
# write a lambda to sort these values by their float
# equivalents.
# 
# (Although this is possible without using a custom function
# or lambda, we would like to practice lambdas here.)

fvals = ['39.5', '3.0', '300.3', '2.002', '20.95',
         '200.1', '21.3', '20.03']


svals = sorted(fvals, # your lambda here)

print(svals)     # ['2.002', '20.03', '29.95', '21.3',
                 #  '200.1', '3.0', '39.5', '300.3']

