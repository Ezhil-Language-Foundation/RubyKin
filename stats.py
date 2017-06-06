#! python
# (C) 2017 Ezhil Language Foundation
#  This code is released under public domain.
import os
import glob
import tamil
import codecs
import re
import pprint

FLIST = []

def get_words(filename):
    with codecs.open(filename,"r","UTF-8") as fp:
        data  = fp.read()
        nwords = len(re.split("\s+",data))
        ntamil = len( tamil.utf8.get_tamil_words( tamil.utf8.get_letters(data) ) )
        return (nwords,ntamil)
    return (0,0)

def process(fd):
    if os.path.isdir(fd):
        for f_or_d in glob.glob(os.path.join(fd,'*')):
            if os.path.isdir( f_or_d): 
                process( f_or_d )
            else:
                handlefile(f_or_d)
    else:
        handlefile(fd)

def handlefile(fd):
    if fd.endswith(u".md"):
        tot,tam=get_words(fd)
        a = tot-tam
        b = tam
        FLIST.append( [fd, {'lang_eng':a,'lang_tam':b,'perc':b/float(a+b)}] )
        print(u"%s => %f %%"%(fd.replace(basename,''),100.0*float(b)/(a+b)))

basename = ''
if __name__ == u"__main__":
    basename = os.getcwd()
    process(os.getcwd())
    print('completion => %f%%'%(100.0*sum([x[1]['perc'] for x in FLIST])/len(FLIST)))
