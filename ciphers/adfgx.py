# ADFGX Cipher
# by: nuit
#
#  A D F G X
#A b t a l p
#D d h o z k
#F q f v s n
#G g j c u x
#X m r e w y

from collections import OrderedDict
import sys

d=OrderedDict()
d={'a':'AA','b':'AD','c':'AF','d':'AG','e':'AX',
   'f':'DA','g':'DD','h':'DF','i':'DG','j':'Dg','k':'DX',
   'l':'FA','m':'FD','n':'FF','o':'FG','p':'FX',
   'q':'GA','r':'GD','s':'GF','t':'GG','u':'GX',
   'v':'XA','w':'XD','x':'XF','y':'XG','z':'XX'}

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
