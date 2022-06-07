# 3.32:  Use the chardet library to "sniff" an encoding.
# Given the below strings, use chardet.detect() with each of
# the two bytestring to get Python's best guess as to its
# encoding.  Print the resulting dict from .detect().

import chardet

bytestr1 = 'voilà'.encode('utf-8')

bytestr2 = 'hello'.encode('utf-8')



