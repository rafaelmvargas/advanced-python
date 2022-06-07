# 3.24:  Scrape and print the <h3> tag in the middle of the
# page (not the first <h3> tag)

import runreport

from bs4 import BeautifulSoup

fname = '../test_scrape.html'

fh = open(fname)
text = fh.read()

soup = BeautifulSoup(text, 'html.parser')

# Expected Output:

# This is a midpage heading.

