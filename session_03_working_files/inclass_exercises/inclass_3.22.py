# 3.22:  Find all parameter values:  for those tags that have
# them, use .find_all() to access multiple tags with the same
# criteria.

from bs4 import BeautifulSoup

scrapee = '../dormouse.html'

text = open(scrapee).read()

soup = BeautifulSoup(text, 'html.parser')

