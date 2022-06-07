# 4.2:  'not' to negate a search.  Execute previous pattern
# with 'not' in front of re.search()

import re

lines = [
  'Acme Corporation is heded by CEO Joseph Benter, and ',
  'President Maria Velas.  Mr. Benter focuses on R&D ',
  'while Ms. Velas provides vision and major deals for ',
  'Acme.  ']

for line in lines:
    if re.search(r'Benter', line):
        print(line)

# Expected Output (for Benter):

# while Ms. Velas provides vision and major deals for
# Acme.

