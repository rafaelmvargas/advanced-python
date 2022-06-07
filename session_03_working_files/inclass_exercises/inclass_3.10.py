# 3.10:  Demo exercise:  issue a request and view elements of
# the request.

# First, issue the following request and view the headers
# reflected back.
# 
# Next, uncomment the 'headers' lines to see how http_reflect
# "sees" you (i.e., what browser and platform it thinks you
# are requesting from).
# 
# Finally, change 'text/plain' to 'text/html' and see
# http_reflect respond with HTML instead of plain text.

import requests

spoof_android = "Mozilla/5.0 (Linux; U; Android 2.3.5; en-in; HTC_DesireS_S510e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"

response = requests.get('http://davidbpython.com/cgi-bin/http_reflect'
                        #, headers={
                        #         'User-Agent':  spoof_android,
                        #         'Accept':      'text/plain',
                        #         }
                        )

print(response.text)

