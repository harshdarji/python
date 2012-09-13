import json
import urllib2
from BeautifulSoup import BeautifulSoup
data=[]
oops=[]
kw={}
kwNb=0
f=open("movies.txt","r")
l=f.readlines()
for i in range(len(l)):
    x=l[i].split('\t')
    url="http://www.imdbapi.com/?t="+x[0]+"&y="+x[1]
    filehandle=urllib2.urlopen(url)
    html=filehandle.read()
    filehandle.close()
    j=json.loads(html)
    if "Title" in j.keys():
        j["i"]=i
        plotKW=[]
        urlKW="http://www.imdb.com/title/"+j["ID"]+"/keywords"
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
        j["plotKeywords"]=plotKW    
        data.append(j)
        print "added "+j["Title"]
    else:
        print "oops! problem with "+x[0]
        oops.append(x[0])
f.open("keywords.txt","wb")
f.write(json.dumps(kw))
f.close()
f.open("dataKW.txt","wb")
f.write(json.dumps(data))
f.close()


