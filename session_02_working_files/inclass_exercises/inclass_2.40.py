# 2.40:  Travel to an inner structure.  Open the file
# ip_routes.json in a text editor and examine the structure.
# Scroll down until you see a repeating dict of dicts nested
# within the structure.

# Now open the file in your Python code and load it into an
# object with json.load().  See if you can reach the repeating
# dict of dicts using a single statement of chained dict
# and/or list subscripts.
# Print this 'inner' structure (dict of dicts) using
# json.dumps() with the indent=4 parameter argument.

import json

fh = open('../ip_routes.json')
struct = json.load(fh)


