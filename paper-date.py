#!/usr/bin/env python
# ever wonder what the date on a research paper was? yes, me too.
# usage: python paper-date.py [pdf] 

import sys
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from time import mktime, strptime
from datetime import datetime

class x:
    r = '\033[91m'
    b = '\033[0m'

if len(sys.argv) != 2:
    print 'Usage: python %s [pdf file]' % sys.argv[0]
    exit()

paper = sys.argv[1]
rp = open(paper, 'rb')
parse = PDFParser(rp)
paper = PDFDocument(parse)
origdate = paper.info[0]['CreationDate'][2:-7]
conv = strptime(origdate, "%Y%m%d%H%M%S")
newdate = datetime.fromtimestamp(mktime(conv))
print "Research for " + x.r + sys.argv[1] + x.b + " was probably conducted around " + x.r + str(newdate) + x.b + " according to PDF creation time."
