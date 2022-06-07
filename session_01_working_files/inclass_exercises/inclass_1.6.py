# 1.6:  Use a dict to build a lookup table.  Perform the
# following steps, testing as you go:

#   1. split the line on a comma
#   2. from the split list, retrieve the 1st (student id) and
# 4th (state) values
#   3. initialize a dict before the loop begins
#   4. subscript the line for student id and state
#   5. add student id and state to dict as key/value pair
#   6. when the loop is complete, print the completed dict
#   7. take user input for an id (for example, ap172); use the
# in operator to test to see if the id is a key in the dict;
# if it is, print the value for that key
# 
# 

fh = open('../student_db.txt')
next(fh)                        # skip next (first) line in file

for line in fh:
    items = line.split(':')
    stu_id = items[0]
    state = items[3]


