# Bifid Cipher
# by: nuit

from collections import OrderedDict
import sys

#colors
R='\033[91m'
G='\033[92m'
B='\033[94m'
ENDC='\033[0m'

index='11 12 13 14 15 21 22 23 24 25 31 32 33 34 35 41 42 43 44 45 51 52 53 54 55'.split()
alfa='a b c d e f g h i k l m n o p q r s t u v w x y z'.split()

d=OrderedDict()
def polybius(kw,p):
  global d
  print B+'\n[!] Making Polybius Square...'+ENDC
  nk=[i for n,i in enumerate(kw) if i not in kw[:n]]

  for i,j in zip(index,nk):
    d[i]=j

  for x in nk:
    for a in alfa:
      if x==a:
        alfa.remove(a)

  for i,j in zip(index[len(d)::],alfa):
      d[i]=j

row=list()
col=list()
cipher=list()
def cypher(d,p,t):
  for i in t:
    for x,y in d.items():
      if i==y:
        row.append(x[0])
        col.append(x[1])
  print B+'\n[!] Making rows and columns...'+ENDC

  prow=[row[n:n+p] for n in range(0,len(row),p)]
  pcol=[col[n:n+p] for n in range(0,len(col),p)]
  print B+'\n[!] Dividing by',str(p),'periods...'+ENDC

  z=list()
  for x, y in zip(prow, pcol):
    z.append((x,y))
  w1=[x for y in z for x in y]
  w2=[x for y in w1 for x in y]
  w3=[i+j for i,j in zip(w2[::2], w2[1::2])]

  for i in w3:
    for k,v in d.items(): 
      if i==k:
        cipher.append(v.upper())

  nc=''.join(cipher)
  nc2=[nc[n:n+5] for n in range(0,len(nc),5)]
  print G+'\n[+] C1PH3R:'+ENDC
  for i in nc2:
    print i,
  print '\n'

ln=list()
dl=list()
text=list()
def decipher(d,p,c):
  print R+'\n[*] Breaking everything!!!'+ENDC
  t=c.lower().replace(' ','')

  for i in t:
    for k,v in d.items():
      if i==v:
        ln.append(k)
  print B+'\n[!] Dividing by',p/2,'periods...'+ENDC
  
  pt=[ln[n:n+(p/2)] for n in range(0,len(ln),(p/2))]
  pt2=''.join([x for y in pt[::2] for x in y])
  pt3=''.join([x for y in pt[1::2] for x in y])
  print B+'\n[!] Making rows and columns...'+ENDC
  
  for x, y in zip(pt2, pt3):
    z=x+y
    dl.append(z)
  
  for i in dl:
    for k,v in d.items():
      if i==k:
        text.append(v)
  
  print G+'\n[+] Original Plaintext:'+ENDC
  print ''.join(text)+'\n'
  
# cli args
p=raw_input('>> Period [num]: ')
kw=raw_input('>> Keyword: ')
for arg in sys.argv:
  if arg == '-c':
    t=raw_input('>> Text: ')
    polybius(kw.lower(),p)
    cypher(d,int(p),t.lower())    
  if arg == '-d':
    c=raw_input('>> Cipher: ')
    polybius(kw.lower(),p)
    decipher(d,int(p),c)
