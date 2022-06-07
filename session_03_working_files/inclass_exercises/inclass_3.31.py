# 3.31:  Open a file in various encodings.  The text of the
# following file is French, and we are opening it in utf-8
# (Python's default).  Try to open the file with
# encoding='latin-1' and encoding='ascii'.

filename = '../la_vie.txt'

fh = open(filename, encoding='utf-8')

print(fh.read())

