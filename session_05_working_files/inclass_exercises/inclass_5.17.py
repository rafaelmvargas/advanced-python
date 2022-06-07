# 5.17:  Sort the lines of revenue.csv by the numeric value in
# the last field by passing the list of lines returned from
# readlines() of the file to sorted() and using a custom sort
# sub similar to an earlier exercise.  (I am also rstrip()ping
# each line before printing it.)

fh = open('../revenue.csv')

lines = fh.readlines()


# your code here


# Expected Output:

# Dothraki Fashions,NY,5.98
# Hipster's,NY,11.98
# Awful's,PA,23.95
# Westfield,NJ,53.90
# The Clothiers,NY,115.20
# The Store,NJ,211.50
# Haddad's,PA,239.50

