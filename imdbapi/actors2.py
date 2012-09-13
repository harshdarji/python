# -*- coding: utf-8 -*-
f=open("movieActors.txt","wb")
for i in range(len(actors)):
    myLine=""
    myRoster=[0,0,0,0]
    myActors=actors[i][:-1].split(', ')
    for j in range(4):
        actor=myActors[j]
        if(actor[-1]=="\r"):
            actor=actor[:-1]
        myRoster[j]=actorList.index(actor)
    for j in range(len(actorList)):
        if j in myRoster:
            myLine+="1"
        else:
            myLine+="0"
        myLine+=","
    myLine=myLine[:-1]+"\n"
    f.write(myLine)

f.close




        
    