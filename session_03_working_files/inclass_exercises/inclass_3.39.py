# 3.39:  Add a link on the hello/ page that calls the goodbye/
# page, and one on the goodbye/ page that calls the hello/
# page.

# However, don't use the <A HREF= URL as was done in the
# launch page.  Instead, use the flask.url_for() function and
# allow Flask to build the URL for you:

# <A HREF="{{ url_for('hello_world') }}">say goodbye</A>

# Also make special note that the argument to url_for() is the
# name of the function, not the @app.route() URL string.
# 
# Expected output:
# You should be able to click back and forth between one page
# and another by clicking the link on each page.

