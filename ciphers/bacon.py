# Sir Francis Bacon Cipher
# by: nuit

from collections import OrderedDict
import sys

d=OrderedDict()
d={'a':'aaaaa','b':'aaaab','c':'aaaba','d':'aaabb','e':'aabaa',
   'f':'aabab','g':'aabba','h':'aabbb','i':'abaaa','j':'Abaaa',
   'k':'abaab','l':'ababa','m':'ababb','n':'abbaa','o':'abbab',
   'p':'abbba','q':'abbbb','r':'baaaa','s':'baaab','t':'baaba',
   'u':'baabb','v':'baabb','w':'babaa','x':'babab','y':'babba',
   'z':'babbb'}

x=list()
def cipher(s):
  for i in s:
    for j in d:
      if i.isupper():
        i=i.lower()
      if i==j:
        x.append(d[i])
  k=''.join(x)
  sys.stdout.write(k+'\n')      

def decipher(c):
  x=[c[n:n+5] for n in range(0,len(c),5)]
  for i in x:
    for k,v in d.items():
      if i==v:
        sys.stdout.write(k)    
  sys.stdout.write('\n')   

for arg in sys.argv:
  if arg == '-c':
    s=raw_input('>> Text: ')
    cipher(s)

  if arg == '-d':
    c=raw_input('>> Cipher: ')
    decipher(c)
