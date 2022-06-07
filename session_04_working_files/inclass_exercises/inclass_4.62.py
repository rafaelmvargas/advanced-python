# 4.62:  Regex substitution.  Replace space-separated with
# comma separated

import re

args = 'this that   other  and  some  other'
args2 = re.sub(r'', ",", args)
print(args2)

# Expected Output:

# this,that,other,and,some,other

