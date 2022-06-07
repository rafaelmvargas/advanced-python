# 3.12:  Issue a request and send parameters with .post().

# In the below program, add the data= argument with the dict
# 'my_data' to send key/value pairs to the http_reflect
# service as part of the body of the request.  In the
# response, find the parameters you sent.

import requests

my_data = {'a': 1, 'b': 'hello'}

response = requests.post('http://davidbpython.com/cgi-bin/http_reflect')

print(response.text)

