# -*- coding: utf-8 -*-
text="En cette journée mondiale de lutte contre le sida, rappelons qu'il est l'affaire de TS & TTES, un combat qui doit continuer ici et là-bas".decode("utf8")

pat1=re.compile(r'(http|https)://[^\s]*',re.IGNORECASE | re.DOTALL)
pat2=re.compile(r"[',;\.:/!?()\"#*%]",re.IGNORECASE | re.DOTALL)
pat3=re.compile(r" +",re.IGNORECASE | re.DOTALL)

textwords=pat1.sub('',text)
textwords=pat2.sub('',textwords)
textwords=pat3.sub(' ',textwords).split(" ")
tw=""
for w in textwords:
	tw+=stemmer.stem(w)+" "
print tw

textwords=tw[:-1].split(" ")
for t in textwords:
    print t
    
print ("tokenized and stemmed - done")

for j in range(len(textwords)):
    print "Checking for similarities for " + textwords[j]
    print "======================================================================================="
    print
    isscored=0
    for kw in keywords:
        kws=kw[1].split(' ')
        l=len(kws)
        if textwords[j]==kws[0] and j+l<len(textwords):
            print "tweet may contain "+kw[1]
            foundword=1
            for k in range(l):
                if textwords[j+k]<>kws[k]:
                    print "but "+textwords[j+k]+" is not like "+kws[k]
                    foundword=0
                    break
            else:
                print textwords[j+k]+" is indeed like "+kws[k]
            if foundword==1:
                iscored=1
                print
                print "one point in "+kw[0]
                print
        else:
            print textwords[j] + " is not like "+kws[0]+". No need to check for "+kw[1]+"."
    if isscored==0:
        print "Pas de correspondance trouvée pour " + textwords[j]
        print
    else:
        print "Correspondance trouvée pour " + textwords[j]
        