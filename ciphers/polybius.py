# Polybius Square
# by: nuit
#
#  1 2 3 4 5
#1 A B C D E
#2 F G H I/J K
#3 L M N O P
#4 Q R S T U
#5 V W X Y Z


from collections import OrderedDict
import sys

d=OrderedDict()
d={'a':'11','b':'12','c':'13','d':'14','e':'15','f':'21',
   'g':'22','h':'23','i':'24','k':'25','l':'31','m':'32',
   'n':'33','o':'34','p':'35','q':'41','r':'42','s':'43',
   't':'44','u':'45','v':'51','w':'52','x':'53','y':'54',
   'z':'55'}

x=list()
def cifrar(s):
  for i in s:
    for j in d:
      if i.upper():
        i=i.lower()
      if i==j:
        x.append(d[i])
  k=''.join(x)
  sys.stdout.write(k+'\n')      
  
def decifrar(c):
  x=[c[n:n+2] for n in range(0,len(c),2)]
  for i in x:
    for k,v in d.items():
      if i==v:
        sys.stdout.write(k)    
  sys.stdout.write('\n')   

for arg in sys.argv:
  if arg == '-c':
    s=raw_input('texto: ')
    cifrar(s)

  if arg == '-d':
    c=raw_input('cifra: ')
    decifrar(c)
    