# 2.3:  Open a database file, then immediately check to see
# that there are tables.

# From the sqlite prompt:

# sqlite> .open session_2.db
# sqlite> .tables
# ad_buys              revenue              students
# ad_companies         student_status       user
# companyrev           student_status_orig  user_classes

# If you don't see any tables listed, then you have either
# misspelled the name of the .db file, or you're in the wrong
# directory.  First, delete the empty file that you created so
# you don't get confused.

# See the present working directory on Windows:

# sqlite> .shell cd

# See the present working directory on Mac:

# sqlite> .shell pwd

# You can use .shell commands to move into the directory where
# the .db file can be found.
# <BR>
# 
# Please note that SQL queries end in a semicolon (;) and
# SQLite3 commands such as .tables and .schema do not:
# 
# adding a semicolon to a "dot" command (e.g. .schema;) causes
# SQLite to ignore the command;
# 
# omitting a semicolon from a query causes SQLite to allow
# "multi-line" queries, which means it will wait until it sees
# the semicolon.

