# Ternary cipher
# by: Nuit 
from collections import OrderedDict
import sys

# colors:
G='\033[92m'
B='\033[94m'
ENDC='\033[0m'

d=OrderedDict()
A=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
d={'A':'001','B':'002','C':'010','D':'011','E':'012','F':'020','G':'021',
   'H':'022','I':'100','J':'101','K':'102','L':'110','M':'111','N':'112',
   'O':'120','P':'121','Q':'122','R':'200','S':'201','T':'202','U':'210',
   'V':'211','W':'212','X':'220','Y':'221','Z':'222', ' ':'000'}

dl=OrderedDict()
def alfa():
  i=1
  for l in A:
    dl[i]=l
    i+=1

lc=list()
def cipher(t):
  print B+'\n[!] Converting to ternary...'+ENDC
  print G+'\n[+] Ternary:'+ENDC
  for i in t:
    if i=='':
      i=' '
    for x,y in d.items():
      if x==i:
        sys.stdout.write(y)
  print '\n'

l=list()
ld=list()
def decipher(s):
  c=[s[n:n+3] for n in range(0,len(s),3)]
  print B+'\n[!] Converting ternary to decimal...'+ENDC
  for i in c:
    l.append(9*int(i[0])+3*int(i[1])+int(i[2]))
  print G+'\n[+] Decimal:'+ENDC
  for j in l:
    if j!=0:
      for x,y in dl.items():
        if j==x:
          print j,
          ld.append(y)
    else:
      print j,
      ld.append(' ') 
  print G+'\n\n[+] Letters:'+ENDC
  print ''.join(ld),'\n'


for arg in sys.argv:
  if arg == '-c':
    t=raw_input('>> text: ')
    cipher(t.upper())
  
  if arg == '-d':
    s=raw_input('>> cipher: ')
    alfa()
    decipher(s)
