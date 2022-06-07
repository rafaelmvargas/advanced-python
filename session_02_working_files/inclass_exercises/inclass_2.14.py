# 2.14:  Note that you can't drop a nonexistent table.
# Attempt to drop the 'test' table again, and note that this
# fails.  Add an IF EXISTS so that if the table exists, it
# will be dropped; if it does not exist, it will return an
# error.  This is especially useful for the "wipe and reload"
# best practice.

# Next, use the up arrow to recover and re-execute the CREATE
# TABLE and follow it up imediately with the DROP TABLE IF
# EXISTS -- to see how easy it is to create and drop tables.

# sqlite> DROP TABLE IF EXISTS test;
# sqlite> CREATE TABLE test (name TEXT, years INT, revenue FLOAT);
# sqlite> DROP TABLE IF EXISTS test;
# sqlite> CREATE TABLE test (name TEXT, years INT, revenue FLOAT);

# Remember, you don't have to retype an old command!  Just use
# up arrow and down arrow to recall previously executed
# commands.

