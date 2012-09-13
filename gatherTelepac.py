import os
path='C:\\Documents and Settings\\cukier_j\\My Documents\\Downloads'
myFile=open(path+'\\coucoulechat.txt','ab')
nbf=0
nbl=0
dirList=os.listdir(path)
for fname in dirList:
    if fname[:7]=='Telepac':
        nbf +=1
        f=open(path+'\\'+fname,'r')
        for line in f:
            if line[:20]<>'Nom / Raison sociale':
                myFile.write(line)
                nbl +=1
        f.close()
        myFile.write("\n")
myFile.close()

print (str(nbf)+' files open')
print (str(nbl)+' lines written')

