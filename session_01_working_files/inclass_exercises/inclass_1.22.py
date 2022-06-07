# 1.22:  Selectively write rows to a CSV.  Loop through the
# list of lists and write only the US rows to the file.  Also
# write the header as the first row.  Close the file, then
# look for newfile3.csv in the session directory.

rows = [
         [ 'company', 'state/province', 'country' ],
         [ 'Acme', 'Caliornia', 'US' ],
         [ 'Bento', 'Toledo', 'SP' ],
         [ 'OuiOui', 'Bourges', 'FR' ],
         [ 'Beta', 'New York', 'US' ]
       ]

fname = '../newfile3.csv'

wfh = open(fname, 'w', newline='')
writer = csv.writer(wfh)



