# 4.38:  Custom Quantifier.

# A password must be 3-8 characters in length (letters,
# numbers and underscores are permitted).  Validate the below
# password attempts.

import re

attempts = ["1234", "hello_there", "password", "ok", "what?", "supercalifrag"]


# + one or more {1,}
# * zero or more {0,}
# ? zero or one {0,1 }
# \w leters, nums, underscore [a-zA-Z0-9_]
# \d digits [0-9]
# \s space characters [ \n\t]
for password in attempts:
    if re.search(r"\w{3,8}", password):
        print(f"{password}:  validated")

# Expected Output:

# 1234:  validated
# password:  validated
