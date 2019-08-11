#!/usr/bin/env python

import sys
import string as s


NoFile = "Nome de arquivo nao especificado"        
NoRead = "Nao foi possível ler"

if len(sys.argv) < 2:
    sys.stderr.write(NoFile)
else:
   file = sys.argv[1]
   try:
       input = open(file, 'r')
   except IOError:
       sys.stderr.write(NoRead, "'%s'\n" % file)
       sys.exit()
       
   lines = input.readlines()
   lines.sort()
   for line in lines:
       if "@" in line:
           for data in s.split(line):
               if "@" in data:
                   print  s.lower(data)
