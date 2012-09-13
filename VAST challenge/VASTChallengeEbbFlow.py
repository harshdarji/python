import csv
import json
import string
ifile  = open("C:\\Documents and Settings\\cukier_j\\My Documents\\vast challenge\\MC_1_Materials_3-30-2011\\Microblogs.csv", "rb")
reader = csv.reader(ifile)
out=open("C:\\Documents and Settings\\cukier_j\\My Documents\\vast challenge\\MC_1_Materials_3-30-2011\\ebbflow.js",'w')
rownum = 0
interestingTweets=[]


minLng=93.19064
maxLng=93.56733
minLat=42.16196
maxLat=42.30148

xMax=27*2
yMax=10*2

xStep=(maxLng-minLng)/xMax
yStep=(maxLat-minLat)/yMax




ebbflow=[]
for period in range(21*4):
    ebbflow.append([])
    for col in range(xMax):
        ebbflow[period].append([])
        for row in range(yMax):
            ebbflow[period][col].append([0,0])
            

out.write("var timeline=[\n")    
RkeyWords=['flu', 'pneumonia', 'hurt', 'hurts', 'cold', 'chills', 'sweats', 'ache', 'headache', 'aches', 'pains', 'pain', 'fatigue', 'on fire', 'hospital', 'medicine', 'diarrhea', 'cough', 'coughing', 'breathing', 'doctor', 'migraine', 'bedridden', 'bed ridden', 'sore throat', 'sick', 'ill']
SkeyWords=['beg', 'begs', 'hope', 'hopes', 'better', 'worse', 'bad', 'well', 'terrible', 'horrible', 'sucks', 'wish', 'crazy', 'atrocious', "can't stand", 'hate', 'hates', 'bed', 'rest', 'rests', 'laying down', 'awful', 'watery eyes', 'allergy', 'allergies', 'awful', 'temp', 'sleep', 'sleeps', '100', '101', '102']
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
        rownum=rownum+1
    else:
        score=0
        tweetWords=row[3].translate(string.maketrans("",""), string.punctuation).lower().split(' ')
        for word in tweetWords:
            for kw in RkeyWords:
                if (word==kw):
                    score=score+1
        if score>0:
            for word in tweetWords:
                for kw in SkeyWords:
                    if(word == kw):
                        score=score+1
                    
        tweetTime=time.strptime(row[1], "%m/%d/%Y %H:%M")
        tweetTimeIndex=(((tweetTime.tm_mon)*30+(tweetTime.tm_mday)-150)*4)+(tweetTime.tm_hour/6)
        tweetCoords=row[2].split(' ')
        tweetRow=int((float(tweetCoords[0])-minLat)/(xStep))
        tweetCol=int((float(tweetCoords[1])-minLng)/(yStep))
        ebbflow[tweetTimeIndex][tweetCol][tweetRow][0]=ebbflow[tweetTimeIndex][tweetCol][tweetRow][0]+1
        ebbflow[tweetTimeIndex][tweetCol][tweetRow][1]=ebbflow[tweetTimeIndex][tweetCol][tweetRow][1]+score
        
out.write(json.dumps(ebbflow))

ifile.close()
out.close()
