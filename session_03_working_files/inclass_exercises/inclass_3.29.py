# 3.29:  Use str.encode() and bytes.decode() to convert a
# string to a bytestring and back to string.

# greet.encode() should include an encoding ('ascii',
# 'latin-1' or 'utf-8'):

greet = 'Hello, world!'

bytestr = greet.encode(# add encoding here)
print(bytestr)

# subscript the bytestring to see individual characters



# now call bytestr.decode() with the same encoding to see the string again


