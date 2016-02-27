# Fritz Nebel's Cipher
# by: nuit 
#
#   A D F G V X
# A g f 6 a z e
# D 4 c t 5 i 7
# F y 3 h 2 q v
# G l r u d o 1
# V k m x s 9 w
# X p 8 j 0 b n


from collections import OrderedDict
import sys

d=OrderedDict()
d={'a':'GA','b':'VX','c':'DD','d':'GG','e':'XA','f':'DA','g':'AA',
   'h':'FF','i':'VD','j':'FX','k':'AV','l':'AG','m':'DV','n':'XX',
   'o':'VG','p':'AX','q':'VF','r':'DG','s':'GV','t':'FD','u':'FG',
   'v':'XF','w':'XV','x':'FV','y':'AF','z':'VA','0':'GX','1':'XG',
   '2':'GF','3':'DF','4':'AD','5':'GD','6':'FA','7':'XD','8':'DX',
   '9':'VV'}

x=list()
def cipher(s):
  for i in s:
    for j in d:
      if i.upper():
        i=i.lower()
      if i==j:
        x.append(d[i])
  k=''.join(x)
  sys.stdout.write(k+'\n') 
  
def decipher(c):
  x=[c[n:n+2] for n in range(0,len(c),2)]
  for i in x:
    for k,v in d.items():
      if i==v:
        sys.stdout.write(k)    
  sys.stdout.write('\n')   

for arg in sys.argv:
  if arg == '-c':
    s=raw_input('>> text: ')
    cipher(s)

  if arg == '-d':
    c=raw_input('>> cipher: ')
    decipher(c)
