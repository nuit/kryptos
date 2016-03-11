# Frequency Analysis
# by: nuit

import sys

G='\033[92m'
B='\033[94m'
ENDC='\033[0m'
            
d,b={},{}
def countchars(filename):
  f=open(filename, "r").read()
  f=''.join(f.split())
  chars=' '.join(f).split()
  t=len(f)

  for c in chars:
    d[c]=chars.count(c) 

  print G+'\n[+] Total chars:',str(t)+ENDC
	
  print B+'\n','*'*6,'Characters:','*'*6+ENDC
  j=0
  for i in sorted(d, key=d.get, reverse=True): 
    p=round(float(d[i])/float(t)*100,2)
    print '['+str(j)+'] '+(i+': '+str(d[i]))+' - '+str(p)+'%'
    j+=1

  for x in range(t):
    n=f[x:x+2]
    b[n]=f.count(n)

  z=0
  print B+'\n\n','*'*6,'Bigrams:','*'*6+ENDC
  for key, value in sorted(b.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    p=round(float(b[key])/float(t)*100,2)
    print '['+str(z)+'] '+(key+': '+str(b[key]))+' - '+str(p)+'%'
    z+=1

if len(sys.argv)>=3:
  if sys.argv[1]=='-f':
    filename=sys.argv[2]
    countchars(filename)
else:
  print '\nUsage: python analysis.py -f <filename>\n'
	
