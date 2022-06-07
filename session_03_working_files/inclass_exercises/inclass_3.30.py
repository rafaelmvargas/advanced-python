# 3.30:  Encode a latin-1 string to bytes and back to string,
# then try to encode as ascii

# The below string contains a non-ascii character.  Encode
# into the following encodings:  'latin-1', 'utf-8' and
# 'ascii'.

string = 'voilà'

bytestr = string.encode(# add encoding here)

print(bytestr)

