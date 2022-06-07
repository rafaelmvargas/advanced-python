# 4.3:  Anchors - start of string.

# Print only those lines that have 'TEL' at the start:

import re

for text_line in ['AURORA HOTEL',
                  'OPEN12:00 AM - 11:59 PM',
                  '14200 E ALAMEDA AVE AURORA, CO 80012',
                  'TEL (303) 344-9901']:
    if re.search(r'', text_line):
        print(text_line)

# Expected Output:

# TEL (303) 344-9901

