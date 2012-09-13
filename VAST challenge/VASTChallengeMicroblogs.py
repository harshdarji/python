import csv
import json
import string
ifile  = open("C:\\Documents and Settings\\cukier_j\\My Documents\\vast challenge\\MC_1_Materials_3-30-2011\\Microblogs.csv", "rb")
reader = csv.reader(ifile)
out=open("C:\\Documents and Settings\\cukier_j\\My Documents\\vast challenge\\MC_1_Materials_3-30-2011\\allTweets.js",'a')
rownum = 0
interestingTweets=[]
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
                    
        for element in row:
            out.write(element)
            out.write(", ")
            out.write(str(score))
            out.write("\n")
          
ifile.close()
out.close
