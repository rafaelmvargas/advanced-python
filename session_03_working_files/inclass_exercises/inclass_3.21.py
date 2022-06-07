# 3.21:  individual parameter values:  for a tag that has
# them, use a subscript to access parameter values of a tag
# (e.g. tag['value'] for the first meta tag)

from bs4 import BeautifulSoup

scrapee = '../dormouse.html'

text = open(scrapee).read()

soup = BeautifulSoup(text, 'html.parser')

