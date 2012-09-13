import json
import urllib2
from BeautifulSoup import BeautifulSoup
data={}
oops=[]
kw={}
kwNb=0
f=open("movieIds.txt","r")
l=f.readlines()
for i in range(len(l)):
    x=l[i][:-1]
    plotKW=[]
    urlKW="http://www.imdb.com/title/"+x+"/keywords"
    filehandle=urllib2.urlopen(urlKW)
    html=filehandle.read()
    filehandle.close()
    soup=BeautifulSoup(html)
    for k in soup.findAll("ul")[8].findAll("li"):
        myKW=k.findAll("b")[0].findAll("a")[0].contents[0]
        if myKW not in kw.keys():
            kw[myKW]=kwNb
            kwNb+=1
            print "New keyword: "+myKW+" - total keywords: "+str(kwNb)
        plotKW.append(kw[myKW])
    data[x]=plotKW    
    print " "+x, 
f=open("keywords2.txt","wb")
f.write(json.dumps(kw))
f.close()
f=open("dataKW2.txt","wb")
f.write(json.dumps(data))
f.close()


