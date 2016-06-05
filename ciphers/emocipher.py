#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#-*- coding: latin-1 -*-
#
# Emocipher - Random Emoji Keyed Caesar
# by: nuit
from collections import OrderedDict
import random
import sys

#colors
R='\033[91m'
G='\033[92m'
B='\033[94m'
ENDC='\033[0m'

demo={'a':'😈','b':'😀','c':'😎','d':'😱','e':'⚤','f':'╋','g':'🔫','h':'ᐁ','i':'😃',
      'j':'😘','k':'🌠','l':'🃏','m':'🐙','n':'🐲','o':'💀','p':'💣','q':'😌','r':'🐻',
      's':'⬛','t':'👻','u':'🚬','v':'🐍','w':'🔒','x':'💉','y':'🐰','z':'👽'}
      
d=OrderedDict()
def keyed_alpha(kw):
  global d
  print B+'\n[!] Making Keyed Alphabet...'+ENDC
  nkw=list(set(kw[::-1]))
  for i in nkw:
    if i in demo:
      del demo[i]
  n=0
  for k in nkw:
    demo[k]=n
    n+=1

lv=[]
def rot(kw,k,s):
  print B+'[!] RANDOM KEY:',str(k)+ENDC
  keyed_alpha(kw)
  ndemo=list(demo)
  print G+'\n[+] CIPHER:'+ENDC
  for j in s:
    for i in xrange(0,26):
      if ndemo[i]==j:
        x=i+k 
        y=x%26
        lv.append(ndemo[y])  
  for i in lv:
    print demo[i],

ld=[]
def tor(kw,k,s):
  keyed_alpha(kw)
  ndemo=list(demo.values()) 
  for j in s:
    for i in xrange(0,26):
      if str(ndemo[i]).decode('utf8')==j:
        x=i-int(k)
        y=x%26
        ld.append(ndemo[y])
  plaintext=[]
  for i in ld:
    for x,y in demo.items():
      if i==y:
        plaintext.append(x)
  print G+'\n[+] TEXT:',''.join(plaintext),'\n'+ENDC

kw=raw_input('>> Keyword: ').lower()
for arg in sys.argv:
  if arg == '-c':   
    k=random.randrange(0,26)
    s=raw_input('>> Text: ').lower().strip()
    rot(kw,k,s)
  if arg == '-d':    
    k=raw_input('>> Num: ')
    s=raw_input('>> Cipher: ').decode('utf8')
    tor(kw,k,s)
