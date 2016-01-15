# ADFGVX Cipher
# by: nuit 
#
#  A D F G V X
#A N A 1 C 3 H 
#D 8 T B 2 O M
#F E 5 W R P D
#G 4 F 6 G 7 I
#V 9 J 0 K L Q
#X S U V X Y Z

from collections import OrderedDict
import sys

d=OrderedDict()
d={'q':'AA','w':'AD','e':'AF','r':'AG','t':'AV','y':'AX','u':'DA',
   'i':'DD','p':'DF','a':'DG','s':'DX','d':'FA','f':'FD','g':'FF',
   'h':'FG','j':'FV','k':'FX','l':'GA','1':'GD','2':'GF','3':'GG',
   '4':'GV','5':'GX','7':'VA','8':'VD','6':'VF','9':'VG','0':'VV',
   'z'='VX','x':'XA','c':'XD','v':'XF','b':'XG','n':'XV','m':'XX'}

x=list()
def cifrar(s):
  for i in s:
    for j in d:
      if i.upper():
        i=i.lower()
      if i==j:
        x.append(d[i])
  k=''.join(x)
  sys.stdout.write(k+'\n') 
  
def decifrar(c):
  x=[c[n:n+2] for n in range(0,len(c),2)]
  for i in x:
    for k,v in d.items():
      if i==v:
        sys.stdout.write(k)    
  sys.stdout.write('\n')   

for arg in sys.argv:
  if arg == '-c':
    s=raw_input('texto: ')
    cifrar(s)

  if arg == '-d':
    c=raw_input('cifra: ')
    decifrar(c)
