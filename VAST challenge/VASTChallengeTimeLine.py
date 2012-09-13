import csv
import json
import string
ifile  = open("C:\\Documents and Settings\\cukier_j\\My Documents\\vast challenge\\MC_1_Materials_3-30-2011\\Microblogs.csv", "rb")
reader = csv.reader(ifile)
out=open("C:\\Documents and Settings\\cukier_j\\My Documents\\vast challenge\\MC_1_Materials_3-30-2011\\timeline.js",'w')
rownum = 0
interestingTweets=[]
timeLine=[]
for i in range(744):
    timeLine.append([0,0,0,0,0,0,0,0])

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
        tweetTimeIndex=(((tweetTime.tm_mon)*30+(tweetTime.tm_mday)-140)*24)+tweetTime.tm_hour
        timeLine[tweetTimeIndex][score]=timeLine[tweetTimeIndex][score]+1
index=0
for hour in timeLine:
    out.write("[")
    for bin in hour[:7]:
        out.write(str(bin))
        out.write(",")
    out.write(str(hour[7]))
    index=index+1
    out.write("]")
    if(index==len(timeLine)):
        out.write("];")
    else:
        out.write(",\n")
              
ifile.close()
out.close()
