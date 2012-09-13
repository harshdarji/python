import nltk
# c'est dit!
import re
# ça aussi!
c=corpora["Hollande"]
cl=""
for l in c.splitlines():
	l=re.sub('(http://[^\s]+)','[link]',l)
	l=re.sub('[,?.;:!()"#]','',l)
	l=re.sub('\s+',' ',l)
	cl+=l+"\n"

print cl

