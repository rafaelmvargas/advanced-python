# 3.20:  Access tag by parameter using a dict.  Use a dict
# with .find() to specify a 'class' parameter value (e.g.
# {'class': 'story_title'})

from bs4 import BeautifulSoup

scrapee = '../dormouse.html'

text = open(scrapee).read()

soup = BeautifulSoup(text, 'html.parser')

