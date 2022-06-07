# 3.3:  Issue a GET request, view status code.  Print the
# .status_code attribute from the response,

# Next, change one of the parameters to see how the code
# changes; also, change the spelling of the word 'product'.
# 
# In addition, use
# requests.status_codes._codes[response.status_code] with the
# status code to see the meaning of the response code.

import requests

url = 'https://forecast.weather.gov/product.php?site=NWS&issuedby=CTP&product=AFD'

response = requests.get(url)


# print(response.status_codes._codes[])

