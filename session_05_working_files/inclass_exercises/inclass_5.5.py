# 5.5:  One list or two?  Is the list in appendme() a new
# list?  How can we test?

def appendme(arg):
    arg.append('d')

x = ['a', 'b', 'c']

appendme(x)


