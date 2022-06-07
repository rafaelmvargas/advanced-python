# 4.1:  Match a simple character pattern.

# Search for 'Velas', then try 'Benter' and 'Acme'.

import re

lines = [
  'Acme Corporation is heded by CEO Joseph Benter, and ',
  'President Maria Velas.  Mr. Benter focuses on R&D ',
  'while Ms. Velas provides vision and major deals for ',
  'Acme.  ']

for line in lines:
    if re.search(r'', line):
        print(line)

# Expected Output (for Velas):

# President Maria Velas.  Mr. Benter focuses on R&D
# while Ms. Velas provides vision and major deals for

