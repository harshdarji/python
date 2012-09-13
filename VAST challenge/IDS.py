import glob, os,re
import json


rootdir='C:/Documents and Settings/cukier_j.OECDMAIN/My Documents/MiniChallenge2 Core Data/'
out=open('C:/Documents and Settings/cukier_j.OECDMAIN/My Documents/MiniChallenge2 Core Data/ids.js', 'w')


files=['20110413/IDS/20110413_VAST11MC2_IDS.txt',
       '20110414/IDS/20110414_VAST11MC2_IDS.txt',
       '20110415/IDS/20110415_VAST11MC2_IDS.txt']

alerts=[]
rules=[]
classifications=[]

for file in files:
    f=open(rootdir + file, 'r')
    lines=f.readlines()
    f.close()

    i=0

    for l in lines:
        if l[0:4]=="[**]":
            i=0
        else:
            i=i+1
        if i==0:
            alert=[-1,-1,0,0,0,0,0,0]
            l=l.replace('[**]','').strip()
            ruleNb=0
            
            for rule in rules:
                if rule==l:
                    alert[0]=ruleNb
                else:
                    ruleNb=ruleNb+1
            if alert[0]==-1:
                rules.append(l)
                alert[0]=len(rules)-1
                
        if i==1:
            line1=l.strip().split('] [')
            if(len(line1)>1):
                line1[0]=line1[0].replace('[Classification: ','')

                classNb=0
                for classification in classifications:
                    if classification==line1[0]:
                        alert[1]=classNb
                    else:
                        classNb=classNb+1
                if alert[1]==-1:
                    classifications.append(line1[0])
                    alert[1]=len(classifications)-1

                line1[1]=line1[1].replace('Priority: ','').replace(']','')
                alert[2]=line1[1]
            else:
                alert[2]=l.replace('[Priority: ','').replace(']','')

        if i==2:
            line2=l.strip().replace(' ->','').split(' ')
            line2[1]=line2[1].split(':')
            line2[2]=line2[2].split(':')

            alert[3]=line2[0]
            alert[4]=line2[1][0]
            if len(line2[1])>1:
                alert[5]=line2[1][1]
            alert[6]=line2[2][0]
            if len(line2[2])>1:
                alert[7]=line2[2][1]
            alerts.append(alert)
        
out.write('var classifications=')
out.write(json.dumps(classifications))
out.write(';\n')

out.write('var rules=')
out.write(json.dumps(rules))
out.write(';\n')

out.write('var alerts=')
out.write(json.dumps(alerts))
out.write(';\n')

out.close()