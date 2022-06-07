# 3.26:  Scrape and print each of the <p> tag texts.

import runreport

from bs4 import BeautifulSoup

fname = '../test_scrape.html'

fh = open(fname)
text = fh.read()

soup = BeautifulSoup(text, 'html.parser')

# Expected Output:

# This is some text.
# This is some more text.
# This is even more text.

