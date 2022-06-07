# 4.4:  Anchors - end of string.

# Print only those files that end in .jpg

import re

filenames = ['image.jpg', 'image.png', 'filejpg.txt', 'file2.doc',
             'file3.pdf', 'image2.gif', 'image3.jpg', 'image4.jpg']

for name in filenames:
    if re.search(r'', name):
        print(name)

# Expected Output:

# image.jpg
# image3.jpg
# image4.jpg

