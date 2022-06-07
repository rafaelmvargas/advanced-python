# 3.11:  Demo exercise:  issue a request and send parameters
# with .get().

# In the below program, add the params= argument with the dict
# 'my_params' to send key/value pairs to the http_reflect
# service as part of the query string.  In the response, find
# the parameters you sent.

import requests

my_params = {'a': 1, 'b': 'hello'}

response = requests.get('http://davidbpython.com/cgi-bin/http_reflect')

print(response.text)

