# bash$ at - aleph <-> beth
# by: nuit

import sys
s=list('abcdefghijklmnopqrstuvwxyz0123456789')
z=s[::-1]
d=dict(zip(s,z))
nc=list()

def cifrar(c):
  for i in c:
    for v,k in d.items():
      if i==v:
        nc.append(k)
  print "".join(nc)

nk=list()
def decifrar(a):
  for i in a:
    for k,v in d.items():
      if i==k:
	nk.append(v)
  print "".join(nk)			

for arg in sys.argv:
  if arg == '-c':
    c=raw_input('texto: ')
    cifrar(c)
  if arg == '-d':
    a=raw_input('cifra: ')
    decifrar(a)
