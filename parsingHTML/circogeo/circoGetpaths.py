from codecs import *
input=codecs.open("C:\Documents and Settings\cukier_j\My Documents\python\parsingHTML\circogeo\circos.txt","r","utf-8")
circos=input.readlines()
outputS=codecs.open("C:\Documents and Settings\cukier_j\My Documents\python\parsingHTML\circogeo\output.txt","w","utf-8")
outputP=codecs.open("C:\Documents and Settings\cukier_j\My Documents\python\parsingHTML\circogeo\outputPaths.txt","w","utf-8")
prefix="http://www.elections-legislatives.fr/circonscriptions/"
paths=[]
mypaths=[]
for i in range(len(circos)):
    outputP.write(circos[i].split("\t")[2])
    outputS.write(circos[i].split("\t")[2])
    js=prefix+circos[i].split("\t")[1]
    html=htmlify(js).splitlines()
    for j in html:
        if "path" in j:
            
            mypath=j.split("\"")[1]
            coordString=""
            x=0
            y=0
            mode=1
            for token in mypath.split(" "):
                if not "," in token:
                    coordString=coordString+token.upper()+" "
                    if token.isupper():
                        mode=0
                    else:
                        mode=1
                else:
                    xy=token.split(",")
                    x=mode*x+float(xy[0])
                    y=mode*y+float(xy[1])
                    coords.append([x,y])
                    coordString=coordString+str(x)+","+str(y)+" "

            
            paths.append(mypath)
            mypaths.append(coordString)
            outputP.write(mypath+"\n")
            outputS.write(coordString+"\n")
input.close()
output.close()

    


