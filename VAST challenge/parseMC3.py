import glob, os
import nltk
import json


rootdir='C:/Documents and Settings/cukier_j/My Documents/vast challenge/MC_3_Materials_4_4_2011'
def count_words(string, key):
    return float(len(string) - len(string.replace(key, ''))) / float(len(key))

placesW=("Vastopolis", "Cornertown", "Westside", "Villa", "Smogtown", "Plainville", "Southville", "Downtown", "Riverside", "Suburbia", "Eastside", "Uptown", "Lakeside",
             "Vastopolis Armed Forces","Vastopolis Dome", "Courthouse", "Capital Building", "Convention Center", "Vastopolis Airport","Westside Stadium", 
             "Vastopolis City Hospital","St. Georges Hospital","Corner Hospital", "Westside Hospital", "Northside Hospital", "River Hospital", "Villa Hospital", "Smogtown Hospital",             
             "Interstate 610", "Interstate 67", "Interstate 435", "Interstate 494", "Interstate 269", "Interstate 270","Interstate 124", "Interstate 905",
             "Vast River")

threatW=("threat", "bomb", "explosive", "arson", "hijack", "explosion", "terror", "hack", "security")

out=open('C:/Documents and Settings/cukier_j/My Documents/vast challenge/scores.txt', 'w')
scores=[]



for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        
        
        f=open(rootdir + '/' + file, 'r')
        lines=f.readlines()
        f.close()
        t=''
        for l in lines:
            t=t+l
        thisScore={"name":file[:5], "values":[0,0], "size":len(t)}
        for word in placesW:
            thisScore["values"][0]=thisScore["values"][0]+count_words(t,word)

        for word in threatW:
            thisScore["values"][1]=thisScore["values"][1]+count_words(t,word)

        scores.append(thisScore)

out.write(json.dumps(scores))
out.close()