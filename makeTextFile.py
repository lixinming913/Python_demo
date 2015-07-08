'create text file'

import os
ls = os.linesep #give line end charactor on current platform

#input file  name
while True:
    fname = raw_input('enter file name:')
    if os.path.exists(fname):
        print "error: '%s' already exists" % fname
    else:
        break
#get the content
all = []
print "\n enter lines('.' by itself to quit).\n"

#loop until user teminates input
while True:
    entry = raw_input('>')
    if( entry == '.' ):
        break
    else:
        all.append(entry)
#write file
fobj = open(fname, 'w')
fobj.writelines(['%s%s'% (x,ls) for x in all])
fobj.close()
print 'done'
