import glob, os
import nltk
import json


mydir='C:/Documents and Settings/cukier_j/My Documents/Downloads/netflix/training_set/'
files=('mv_0005317.txt', 'mv_0015124.txt', 'mv_0014313.txt', 'mv_0015205.txt', 'mv_0001905.txt', 'mv_0006287.txt', 'mv_0011283.txt', 'mv_0016377.txt', 'mv_0016242.txt', 'mv_0012470.txt', 'mv_0015582.txt', 'mv_0009340.txt', 'mv_0006972.txt', 'mv_0012317.txt', 'mv_0002152.txt')


def count_words(string, key):
    return float(len(string) - len(string.replace(key, ''))) / float(len(key))

out=open('C:/Documents and Settings/cukier_j/My Documents/Downloads/netflix/results.txt', 'w')
usersObj={}
usersArr=[]
lastUserArr=0

finalUsersArr=[]

for file in files:
    f=open(mydir + '/' + file, 'r')
    lines=f.readlines()
    f.close()
    for l in lines[1:]:
        user=l.split(',')[0]
        try:
            usersObj[user]["nb"]=usersObj[user]["nb"]+1
            usersObj[user][file]=l.split(',')[1]
        except KeyError:
            usersArr.append(user)
            usersObj[user]={"pos":lastUserArr, "nb":1, file:l.split(',')[1]}
            lastUserArr=lastUserArr+1

finalUsersNb=0
for u in usersArr:
    if usersObj[u]["nb"]==15:
        myArray=[]        
        for file in files:
            try:
                myArray.append(usersObj[u][file])
            except KeyError:
                myArray.append('..')
        finalUsersArr.append(myArray)

out.write(json.dumps(finalUsersArr).replace('"','').replace(' ',''))
out.close()
            
    
