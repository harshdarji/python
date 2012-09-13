input=open("savedO.txt","r")
complexPaths=[]
lines=input.readlines()
myDept={}
circInd=0
for i in range(len(lines)):
    line=lines[i]
    if line[0] not in ("m","M"):
        if myDept!={}:
            myDept["x"]=minX
            myDept["y"]=minY
            myDept["width"]=maxX-minX
            myDept["height"]=maxY-minY
            complexPaths.append(myDept)            
        myDept={}
        myDept["dept"]=line.split("\t")[0]
        myDept["name"]=line.split("\t")[1][:-1]
        circInd=0
        maxX=0
        minX=999999
        maxY=0
        minY=999999
        myDept["circos"]=[]
    else:
        coords=line.split(" ")
        x=0
        y=0
        absCoords=[]
        mode=0
        for c in coords:
            if "," in c:
                xy=c.split(",")
                if mode==0:
                    x=x+float(xy[0])
                    y=y+float(xy[1])
                else:
                    x=float(xy[0])
                    y=float(xy[1])
                    
                if x>maxX:
                    maxX=x
                if x<minX:
                    minX=x
                if y>maxY:
                    maxY=y
                if y<minY:
                    minY=y
                absCoords.append((x,y))
            else:
                if c.islower():
                    mode=0
                else:
                    mode=1
        simpleCoords=simplify_points (absCoords, 1.0)
        simplerCoords=[]
        for c in absCoords:
            simplerCoords.append([(int(round(c[0]))),(int(round(c[1])))])
        myCirco={}
        myCirco['index']=circInd
        circInd=circInd+1
        myCirco['path']=simplerCoords
        #myCirco['absCoords']=absCoords
        myDept["circos"].append(myCirco)

