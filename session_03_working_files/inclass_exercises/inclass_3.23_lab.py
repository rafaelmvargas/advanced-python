# 3.23:  In test_scrape.html, scrape the page title (the title
# within the <title> tags) and print it.

import runreport

from bs4 import BeautifulSoup

fname = '../test_scrape.html'

fh = open(fname)
text = fh.read()

soup = BeautifulSoup(text, 'html.parser')

# Expected output:

import runreport

This is a page title.

# Note that you may occasionally encounter a
# UnicodeDecodeError when you attempt to read a file from the
# internet.  In these cases you should tell Python which
# encoding to use:

import runreport

text = open(scrapee, encoding='utf-8')

