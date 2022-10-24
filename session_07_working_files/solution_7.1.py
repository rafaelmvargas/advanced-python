"""
 solution_7.1.py -- Load and save config to file via a class
 
 Author: Rafael Vargas (rmv235@stern.nyu.edu)
 Last Revised: 8/5/2022 -- Fourth revision


"""
import csv


class Config:
    """class for producing config instances, pass a filename and use .get() and set() functions"""

    def __init__(self, filename: str):
        """
        Constructor that takes a csv filename as an argument
        """
        self.params = {}
        self.filename = filename
        self.format = filename.split(".")[1]

        self.read_csv_file()

    def __str__(self):
        return f"Config('{self.filename}')"

    def get(self, key):
        """
        used to get a value from a key, if it exists
        """
        try:
            return self.params[key]
        except KeyError:
            raise KeyError(f"key '{key}' not in config")

    def read_csv_file(self):
        fh = open(self.filename, "r")
        config_file = csv.reader(fh)

        # check for corruption
        for line in config_file:
            if len(line) != 2:
                raise ValueError(f"not enough values to unpack")
            self.params[line[0]] = line[1]

        fh.close()

    def set(self, key, value):
        """
        used to set a key with a value
        """
        if key in self.params:
            raise KeyError(f"'{key}' already in config")
        else:
            self.params[key] = value

        self.write_csv_file()

    def write_csv_file(self):
        with open(self.filename, "w") as csv_file:
            writer = csv.writer(csv_file)
            for key, value in self.params.items():
                writer.writerow([key, value])


conf = Config("pconfig copy.csv")

# .get()  RETRIEVES A VALUE BASED ON A KEY (check these against CSV above)

print(conf.get("db_uname"))  # george
print(conf.get("db_password"))  # password1
print(conf.get("data_query"))  # SELECT this, that FROM ...


# .set() ADDS A NEW PAIR TO INSTANCE, AND WRITES IT TO THE FILE
# (note that writing to the file will initially blank out the file, which
# may cause it to be empty the next time it is read (which may be
# "ValueError:  not enough values to unpack"); see read_csv_file(self) below

# conf.set("db_uname2", "gladys")

print(conf.get("db_uname2"))  # gladys

# WE CAN CONFIRM THE NEW PAIR HAS BEEN WRITTEN TO FILE, BY INSTANTIATING
# A NEW INSTANCE FROM THE SAME FILE AND CHECKING FOR THE KEY

newconf = Config("pconfig copy.csv")

print(
    newconf.get("db_uname2")
)  # gladys  (confirms that the file has the new value)


# FILENAME AND FILE EXTENSION ARE ALSO STORED IN THE INSTANCE

print(conf.filename)  # pconfig.csv
print(conf.format)  # csv


# EXTRA CREDIT:  PRINTING THE INSTANCE CALLS THE __str__()  METHOD
# THE STRING RETURNED FROM THIS METHOD IS PRINTED

print(conf)  # this prints the string Config('pconfig.csv')

x = conf.get("xxy")  # raises KeyError:  key "xxy" not in config
