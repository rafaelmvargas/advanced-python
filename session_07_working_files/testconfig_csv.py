
from mylib import Config             # class Config is located in a file called mylib.py

conf = Config('pconfig.csv')        # constructor opens and reads this file according to its format
                                     # (file may also be pconfig.json or pconfig.ini)

                                     # the constructor reads config values from the file
                                     # and stores them in the object's attributes

                                     # program also sets the filename in self.filename and
                                     # the file type ('csv', 'json' or 'ini') in self.format

                                     # note that these attributes match the config file data above
print(conf.db_uname)                 # george
print(conf.db_password)              # password1
print(conf.data_query)               # SELECT this, that FROM mytable WHERE col = 5
print(conf.filename)                 # pconfig.json

conf.email_from = 'joe@wilson.com'   # setting a new attribute in the object

conf.write()                         # writes all attributes back to file
print()
newconf = Config('pconfig.csv')

print(newconf.email_from)            # 'joe@wilson.com' (shows file has been written)

print(newconf)                       # uses the __str__() method to return a string of the config's contents

# the above prints
# db_uname=george
# db_password=password1
# data_query=SELECT this, that FROM mytable WHERE col = 5
# email_from=joe@wilson.com


