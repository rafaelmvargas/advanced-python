# 3.25:  Scrape and print the <div> text as well as the
# "content" parameter value.

import runreport

from bs4 import BeautifulSoup

fname = '../test_scrape.html'

fh = open(fname)
text = fh.read()

soup = BeautifulSoup(text, 'html.parser')

# Expected Output:

# Some div parameter content we want!
# 
#     Some div text!

