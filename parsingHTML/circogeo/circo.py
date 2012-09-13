from codecs import *
input=codecs.open("C:\Documents and Settings\cukier_j\My Documents\python\parsingHTML\circogeo\circos.txt","r","utf-8")
circos=input.readlines()
output=codecs.open("C:\Documents and Settings\cukier_j\My Documents\python\parsingHTML\circogeo\output.txt","w","utf-8")
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

    


