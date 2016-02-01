# Frequency Analysis
# by: nuit

text=raw_input('[!] text: ')
letters=' '.join(text).split()        
            
d=dict()
def count_letters(letters):
	j=0
	for l in letters:
		d[l]=letters.count(l) 
	t=len(letters)
	print '[+] total letters:',str(t)
	for i in sorted(d, key=d.get, reverse=True): 
		p=round(float(d[i])/float(t)*100,2)
		print '['+str(j)+'] '+(i+': '+str(d[i]))+' - '+str(p)+'%'
		j+=1

count_letters(letters)		