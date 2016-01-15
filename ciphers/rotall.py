# Caesar Cipher
# by: nuit

import sys

a=list('abcdefghijklmnopqrstuvwxyz')
A=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
s=raw_input('texto: ')

def rot(k):
  for j in s:
    if j==' ':
      sys.stdout.write(' ')
    if j.isupper():
      for i in xrange(0,26):
        if A[i]==j:
          x=i+k 
          y=x%26
          sys.stdout.write(A[y])    
    else:
      for i in xrange(0,26):
        if a[i]==j:
          x=i+k 
          y=x%26
          sys.stdout.write(a[y])
    
def rotall(s):
  for k in xrange(26):
    rot(k)
    print ' ['+str(k)+']'
    
rotall(s)    
