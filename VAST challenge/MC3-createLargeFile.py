import glob, os
import nltk
import json


rootdir='C:/Documents and Settings/cukier_j.OECDMAIN/My Documents/vastChallenge/mc3/MC_3_Materials_4_4_2011'
def count_words(string, key):
    return float(len(string) - len(string.replace(key, ''))) / float(len(key))

def contains(theString, theQueryValue):
  return theString.find(theQueryValue) > -1

placesW=(
    #"Vastopolis",
            "Cornertown", "Westside", "Villa", "Smogtown", "Plainville", "Southville", "Downtown", "Riverside", "Suburbia", "Eastside", "Uptown", "Lakeside",
             "Vastopolis Armed Forces","Vastopolis Dome", "Courthouse", "Capital Building", "Convention Center", "Vastopolis Airport","Westside Stadium", 
             "Vastopolis City Hospital","St. Georges Hospital","Corner Hospital", "Westside Hospital", "Northside Hospital", "River Hospital", "Villa Hospital", "Smogtown Hospital",             
             "Interstate 610", "Interstate 67", "Interstate 435", "Interstate 494", "Interstate 269", "Interstate 270","Interstate 124", "Interstate 905",
             "Vast River")

threatW=("threat", "menace", "terror", "hack", "security")

bioW=("bioterrorism", "microbe")
airW=("hijack", "crash", "flight 256")
fireW=("arson", "bomb", "explosive", "explosion", "arson", "fire")
hackW=("hack", "virus")


out=open('C:/Documents and Settings/cukier_j.OECDMAIN/My Documents/vastChallenge/largeTaggedFile.js', 'w')
scores=[]



for n in range(1,4475):
    file="0"*(5-len(str(n)))+str(n)+".txt"
    f=open(rootdir + '/' + file, 'r')
    lines=f.readlines()
    f.close()
    t=''
    for l in lines:
        l=l.decode('iso-8859-1')
        t=t+l
    thisScore={"name":file[:5], "values":[0,0], "size":len(t)}
    type='none'
    typeMax=0
    for word in placesW:
        thisScore["values"][0]=thisScore["values"][0]+count_words(t,word)
        lines[2]=lines[2].replace(word, '<span class="place">'+word+'</span>')
    for word in threatW:
        thisScore["values"][1]=thisScore["values"][1]+count_words(t,word)
        lines[2]=lines[2].replace(word, '<span class="threat">'+word+'</span>')
    if thisScore["values"][1]>typeMax:
        type='threat'
        typeMax=thisScore["values"][1]
    for word in bioW:
        thisScore["values"][2]=thisScore["values"][1]+count_words(t,word)
        lines[2]=lines[2].replace(word, '<span class="bio">'+word+'</span>')
    if thisScore["values"][2]>typeMax:
        type='bio'
        typeMax=thisScore["values"][2]
    for word in airW:
        thisScore["values"][3]=thisScore["values"][1]+count_words(t,word)
        lines[2]=lines[2].replace(word, '<span class="air">'+word+'</span>')
    if thisScore["values"][3]>typeMax:
        type='air'
        typeMax=thisScore["values"][3]
    for word in fireW:
        thisScore["values"][4]=thisScore["values"][1]+count_words(t,word)
        lines[2]=lines[2].replace(word, '<span class="fire">'+word+'</span>')
    if thisScore["values"][4]>typeMax:
        type='fire'
        typeMax=thisScore["values"][4]
    for word in hackW:
        thisScore["values"][5]=thisScore["values"][1]+count_words(t,word)
        lines[2]=lines[2].replace(word, '<span class="hack">'+word+'</span>')
    if thisScore["values"][5]>typeMax:
        type='hack'
        
    thisScore["title"]=lines[0][:-1].decode('iso-8859-1')
    thisScore["text"]=lines[2][:-1].decode('iso-8859-1')
    date=lines[1][:-1].replace(',','').split(' ')
    if(date[0]=='May'):
        thisScore["day"]=date[1]
    else:
        thisScore["day"]=0
    thisScore["date"]=lines[1][:-1]
    thisScore["type"]=type
    scores.append(thisScore)

out.write(json.dumps(scores))
out.close()