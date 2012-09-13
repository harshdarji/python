from json import *
paths=open("outputPaths.txt","r")
lines=paths.readlines()
output=open("pathJSON.js","w")
output.write("var paths=\n")
depts=[]
myDept={}
circos=[]
circoIndex=0
id=""
for line in lines:
    if line[0].upper()!="M":
        if len(circos)>0:
            myDept["circos"]=circos
            print "appending ... "
            print "id - "+myDept['id']
            depts.append(myDept)
            print "len(depts) " + str(len(depts))
            
            print "depts[len(depts)-1]['id'] " + depts[len(depts)-1]['id']
            print "depts[0]['id'] " + depts[0]['id']
            
            
            print
        myDept={}   
        id=line.split("\t")[0]
        myDept["id"]=id
        name=line.split("\t")[1][:-1]
        myDept["name"]=name
        print("now dealing with "+name+" ("+id+")")
        circos=[]
        circoIndex=0
    else:
        myPath={}
        circoIndex=circoIndex+1
        myPath["dept"]=id
        myPath["index"]=circoIndex
        myPath["path"]=line[:-1]
        circos.append(myPath)
        print circoIndex,
        
myDept["circos"]=circos
depts.append(myDept)

output.write(dumps(depts))
        
        
            



output.close()
