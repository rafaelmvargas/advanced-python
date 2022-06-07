# 4.48:  Print only those files that start with 'image#'
# ('image' plus a possible number) and end in any of these
# image extensions:  '.jpg', '.png', '.gif'

import runreport

import re

filenames = ['image2.jpg', 'image.png', 'file.txt', 'file2.doc',
             'file3.pdf', 'image2.gif', 'image3.jpg', 'image4.jpg',
             'advert.jpg', 'advert.png']

for name in filenames:
    if re.search(r'', name):
        print(name)

# Expected Output:

# image2.jpg
# image.png
# image2.gif
# image3.jpg
# image4.jpg

