# -*- encoding: utf-8 -*-
# trinary cipher
# by: nuit
from collections import OrderedDict
import sys

d=OrderedDict()
d={'a':'.⋅....⋅','b':'.⋅....˙','c':'.⋅...⋅.','d':'.⋅...⋅⋅','e':'.⋅...⋅˙','f':'.⋅...˙.','g':'.⋅...˙⋅',
   'h':'.⋅...˙˙','i':'.⋅..⋅..','j':'.⋅..⋅.⋅','k':'.⋅..⋅.˙','l':'.⋅..⋅⋅.','m':'.⋅..⋅⋅⋅','n':'.⋅..⋅⋅˙',
   'o':'.⋅..⋅˙.','p':'.⋅..⋅˙⋅','q':'.⋅..⋅˙˙','r':'.⋅..˙..','s':'.⋅..˙.⋅','t':'.⋅..˙.˙','u':'.⋅..˙⋅.',
   'v':'.⋅..˙⋅⋅','w':'.⋅..˙⋅˙','x':'.⋅..˙˙.','y':'.⋅..˙˙⋅','z':'.⋅..˙˙˙','0':'.......','1':'......⋅',
   'A':'.˙....⋅','B':'.˙....˙','C':'.˙...⋅.','D':'.˙...⋅⋅','E':'.˙...⋅˙','F':'.˙...˙.','G':'.˙...˙⋅',
   'H':'.˙...˙˙','I':'.˙..⋅..','J':'.˙..⋅.⋅','K':'.˙..⋅.˙','L':'.˙..⋅⋅.','M':'.˙..⋅⋅⋅','N':'.˙..⋅⋅˙',
   'O':'.˙..⋅˙.','P':'.˙..⋅˙⋅','Q':'.˙..⋅˙˙','R':'.˙..˙..','S':'.˙..˙.⋅','T':'.˙..˙.˙','U':'.˙..˙⋅.',
   'V':'.˙..˙⋅⋅','W':'.˙..˙⋅˙','X':'.˙..˙˙.','Y':'.˙..˙˙⋅','Z':'.˙..˙˙˙','\n':'.⋅.⋅..⋅',' ':'.⋅.⋅...'}

def szyfr(s):
  for i in s:
    for x,y in d.items():
      if i==x:
        print d[i],

def decipher(c):
  print '\n[+] Plain Text:'
  for i in c:
    for x,y in d.items():
      if i.encode('utf8', 'replace')==y:
	      sys.stdout.write(x),
  sys.stdout.write('\n\n')
  

for arg in sys.argv:
  if arg == '-c':
    s=raw_input('>> text: ')
    szyfr(s)

  if arg == '-d':
    c=unicode(raw_input('>> cipher: '), 'utf8').split()
    decipher(c)
