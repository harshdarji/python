# -*- coding: utf-8 -*-
from codecs import *
from douglaspeucker import *
from json import *
input=codecs.open("C:\Documents and Settings\cukier_j\My Documents\python\parsingHTML\circogeo\depts.txt","r","utf-8")
depts=input.readlines()
output=codecs.open("C:\Documents and Settings\cukier_j\My Documents\python\parsingHTML\circogeo\simple.txt","w","utf-8")
#prefiy="http://www.elections-legislatives.fr/circonscriptions/"
simplePaths=[]
for i in range(len(depts)):
    dept=depts[i].split("\t");
    myPath={}
    myPath["dept"]=dept[0]
    myPath["path"]=[]
    minX=999
    minY=999
    maxX=0
    maxY=0
    simplePath=[]
    for c in dept[1].split(";"):
        coords=c.split(",")
        simplePath.append((float(coords[0]),float(coords[1])))
    simplePath=simplify_points (simplePath, 1.0)
    for c in simplePath:
        x=int(round(c[0],0))
        y=int(round(c[1],0))
        if x<minX:
            minX=x
        if x>maxX:
            maxX=x
        if y<minY:
            minY=y
        if y>maxY:
            maxY=y
        myPath["path"].append([x,y])
    myPath["x"]=minX
    myPath["y"]=minY
    myPath["width"]=maxX-minX
    myPath["height"]=maxY-minY
    simplePaths.append(myPath)


    
input.close()
output.write(dumps(simplePaths))
output.close()


input=codecs.open("C:\Documents and Settings\cukier_j\My Documents\python\parsingHTML\circogeo\circos.txt","r","utf-8")
circos=input.readlines()
output=codecs.open("C:\Documents and Settings\cukier_j\My Documents\python\parsingHTML\circogeo\deptpaths.txt","w","utf-8")
prefix="http://www.elections-legislatives.fr/circonscriptions/"
paths=[]
mypaths=[]
for i in range(len(circos)):
    output.write(circos[i].split("\t")[2]+"\n")
    js=prefix+circos[i].split("\t")[1]
    html=htmlify(js).splitlines()
    for j in html:
        if "path" in j:
            
            mypath=j.split("\"")[1]
            
            mym=[]
            for m in mypath.split("m"):
                myc=[]
                for c in m.split("c"):
                    myl=[]
                    for l in c.split("l"):
                        simple=""
                        for x in l.split(" "):
                            if "," in x:
                                y=x.split(",")
                                simple=simple+str(round(float(y[0]),2))+","+str(round(float(y[1]),2))+" "
                            else:
                                simple=simple+x+" "
                        myl.append(simple)
                    myl="l".join(myl)
                    myc.append(myl)
                myc="c".join(myc)
                mym.append(myc)
            mym="m".join(mym)
            #print mym
            paths.append(mypath)
            mypaths.append(mym)
            output.write(mym+"\n")
input.close()
output.close()

