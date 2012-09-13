# -*- coding: utf-8 -*-
import codecs
import json
import urllib2
from operator import itemgetter, attrgetter
from BeautifulSoup import BeautifulSoup
f=codecs.open("actors2.txt", encoding='utf-8', mode='r')
actors=f.readlines()
f.close
actorList=[]
actorNb=0
actorFreq={}
f=open("movieActors.txt","wb")
a = codecs.open("actorList.txt", encoding='utf-8', mode='wb')

for i in range(len(actors)):
    myRoster=""
    myActors=actors[i][:-1].split(', ')
    for actor in myActors:
        if(actor[-1]=="\r"):
            actor=actor[:-1]
        if actor not in actorList:
            actorList.append(actor)
            a.write(actor+"\n")
            actorFreq[actor]=0
            print("Adding "+actor+" at position "+str(actorNb))
            actorNb+=1
        myRoster=myRoster+str(actorList.index(actor))+","
        actorFreq[actor]+=1
    myRoster=myRoster[:-1]+"\n"
    f.write(myRoster)

f = codecs.open("actorFreq.txt", encoding='utf-8', mode='wb')
f.write(json.dumps(actorFreq))
f.close


        
    