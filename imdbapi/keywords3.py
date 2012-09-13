import json
import urllib2
from operator import itemgetter, attrgetter
from BeautifulSoup import BeautifulSoup
f=open("keywords2.txt","r")
kw=json.loads(f.read())
f.close

f=open("dataKW2.txt","r")
data=json.loads(f.read())
f.close

kw2=[]

for myKey in kw.keys():
               kw2.append({"id":kw[myKey],"word":myKey,"nb":0})

kw2=sorted(kw2, key=lambda keyword: keyword["id"])

for movie in data.keys():
    for id in data[movie]:
        kw2[id]["nb"]+=1

kw2=sorted(kw2, key=lambda keyword: keyword["nb"])

kw2=[elem for elem in kw2 if elem["nb"] > 5]

x=[]
for movie in data.keys():
    myX=""    
    for keyword in kw2:
        if keyword["id"] in data[movie]:
            myX+="1,"
        else:
            myX+="0,"
    myX=myX[:-1]+"\n"
    x.append(myX)

f=open("x.txt","wb")
f.writelines(x)
f.close()
