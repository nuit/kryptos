from collections import OrderedDict
import sys

d=OrderedDict()
d={'a':'2','b':'22','c':'222','d':'3','e':'33','f':'333','g':'4','h':'44', 
   'i':'444','j':'5','k':'55','l':'555','m':'6','n':'66','o':'666','p':'7',
   'q':'777','r':'77','s':'7777','t':'8','u':'88','v':'888','w':'9','x':'99',
   'y':'999','z':'9999'}

def cifrar(s):
	for i in s:
		for x,y in d.items():
			if i==x:
				print y,

def decifrar(c):
	for i in c:
		for x,y in d.items():
			if i==y:
				sys.stdout.write(x)    
	sys.stdout.write('\n')		

for arg in sys.argv:
  if arg == '-c':
    s=raw_input('texto: ')
    cifrar(s)

  if arg == '-d':
    c=raw_input('cifra: ').split()
    decifrar(c)			