# M. E. Ohaver mutilation cipher
# by: nuit 

from collections import OrderedDict
import sys

G='\033[92m'
B='\033[94m'
ENDC='\033[0m'

m=OrderedDict()
m={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....',
   'I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.',
   'Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
   'Y':'-.--','Z':'--..'}


n,l,x=[],[],[]
def cipher(s,f):
  z=0
  for i in s:
    for j in m:
      if i==j: 
        l.append(m[i])
        n.append(len(m[i]))
  if f=='c': 
    print B+'\n[+] MorseCode:'+ENDC,' '.join(l)
    hack(l,n,f='c')
  else: 
    print B+'\n[+] Mutilated:'+ENDC,' '.join(l)
    hack(l,n,f='d')
  
def decipher(c,f):
  if f=='c': 
    print G+'\n[+] Cipher:'+ENDC
  else: 
    print G+'\n[+] Original word:'+ENDC
  for i in c:
    for k,v in m.items():
      if i==v:
        sys.stdout.write(k)    
  sys.stdout.write('\n\n')  

def hack(l,n,f): 
  y=0
  u=n[::-1]
  h=''.join(l)
  for v in u:
    x.append(h[y:y+v])
    y+=v
  if f=='c': 
  	print B+'[+] Mutilated:'+ENDC,' '.join(x)
  	decipher(x,f='c')
  else: 
    print B+'[+] MorseCode:'+ENDC,' '.join(x)
    decipher(x,f='d')
  

for arg in sys.argv:
  if arg == '-c':
    s=raw_input('>> Word: ').upper()
    cipher(s,f='c')
  if arg == '-d':
    c=raw_input('>> Cipher: ')
    cipher(c,f='d')
   
