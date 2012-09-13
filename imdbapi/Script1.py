import json
import urllib2
data=[]
oops=[]
f=open("movies.txt","r")
l=f.readlines()
for i in range(len(l)):
    x=l[i].split('\t')
    url="http://www.imdbapi.com/?t="+x[0]+"&y="+x[1]
    filehandle=urllib2.urlopen(url)
    html=filehandle.read()
    j=json.loads(html)
    if "Title" in j.keys():
        j["i"]=i
        data.append(j)
        print "added "+j["Title"]
    else:
        print "oops! problem with "+x[0]
        oops.append(x[0])
        

