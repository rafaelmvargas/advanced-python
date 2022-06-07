# 3.41:  Read the caption and mood field values and include
# them in the goodbye.html template.

# The form sends field values for "caption" and "mood" to the
# app when it calls the goodbye/ URL; retrieve these values
# using flask.request.args.get('caption') and
# flask.request.args.get('mood').
# 
# Use the {{ [token name] }} token (where [token_name] is the
# token name) to insert a value into the template.  Add
# parameter arguments (for example caption=[caption variable],
# where [caption variable] is whatever variable you used to
# retrieve the value from the form) to render_template() to
# insert the value.
# 
# Expected Output:

# Goodbye, now! Come on back, y'hear?!
# 
# caption: Hi there (or whatever you typed into form)
# mood: happy (or whichever mood you chose)
# say hello

# Note that Hi there and happy are values that I entered into
# the form when I submitted it.

