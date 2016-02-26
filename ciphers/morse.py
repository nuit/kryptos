# Samuel Morse's Cipher
# by: nuit

from collections import OrderedDict
import sys

d=OrderedDict()
d={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.',
   'H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.',
   'O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-',
   'V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','0':'-----',
   '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....',
   '7':'--...','8':'---..','9':'----.','.':'.-.-.-',',':'--..--',
   ';':'---...','?':'..--..','/':'-..-.'}

def szyfr(s):
  for i in s:
    for j in d:
      if i.islower():
        i=i.upper()
      if i==j: 
  		print d[i],     
  sys.stdout.write('\n')      

def decipher(c):
  for i in c:
    for k,v in d.items():
      if i==v:
        sys.stdout.write(k)    
  sys.stdout.write('\n')   

for arg in sys.argv:
  if arg == '-c':
	s=raw_input('>> text: ')
	szyfr(s)

  if arg == '-d':
	c=raw_input('>> cipher: ').split()
	decipher(c)   