# 3.19:  "first tag" attribute access; .text attribute:
# access the object for soup.title, soup.body, soup.p,
# soup.meta.

# Print the type of 1 of these objects.
# 
# Print the .text attribute of each of these objects.

from bs4 import BeautifulSoup

scrapee = '../dormouse.html'

text = open(scrapee).read()

soup = BeautifulSoup(text, 'html.parser')

