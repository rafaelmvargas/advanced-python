# 3.1:  Issue a GET request, view response text with .text.
# Use requests.get() with a url to retrieve a response from
# the weather service.  Print the .text attribute to see the
# body of the response.

import requests

url = 'https://forecast.weather.gov/product.php?site=NWS&issuedby=CTP&product=AFD'

response = requests.get()


