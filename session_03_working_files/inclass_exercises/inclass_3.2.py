# 3.2:  Issue a GET request, view headers.  Print the .headers
# attribute of the response to see the headers sent back by
# the weather server.

# You can also loop through the dict-like response.headers to
# see each key/value pair clearly.

import requests

url = 'https://forecast.weather.gov/product.php?site=NWS&issuedby=CTP&product=AFD'

response = requests.get(url)


