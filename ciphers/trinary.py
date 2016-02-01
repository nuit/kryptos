from collections import OrderedDict
import sys

d=OrderedDict()
d={'a':'001','b':'002','c':'010','d':'011','e':'012','f':'020','g':'021',
   'h':'022','i':'100','j':'101','k':'102','l':'110','m':'111','n':'112',
   'o':'120','p':'121','q':'122','r':'200','s':'201','t':'202','u':'210',
   'v':'211','w':'212','x':'220','y':'221','z':'222', ' ':'000'}

def cifrar(s):
	for i in s:
		for x,y in d.items():
			if i==x:
				sys.stdout.write(y),
	sys.stdout.write('\n')

def decifrar(c):
	w=[c[n:n+3] for n in range(0,len(c),3)]
	for i in w:
	  for x,y in d.items():
	    if i==y:
			sys.stdout.write(x)    
	sys.stdout.write('\n')

for arg in sys.argv:
  if arg == '-c':
    s=raw_input('texto: ')
    cifrar(s)

  if arg == '-d':
    c=raw_input('cifra: ')
    decifrar(c)
