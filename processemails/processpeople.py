"""
import nltk
import datetime
"""
from nltk.corpus import stopwords
stopwords=stopwords.words('french')+stopwords.words('english')+["-",":",".","/","\xa9","--",",",'"',"'","?","(",")","<",">","..."]
bigram_measures = nltk.collocations.BigramAssocMeasures()

p=open("c://messages//people.txt","r")
people=p.readlines()
p.close()
"""
m=open("c://messages//messages.txt","r")
messages={}
for mLine in m.readlines():
    msg=mLine[:-1].split("\t")
    msg[0]=int(msg[0])
    if len(msg)>3:
        msg[1]=msg[1]+" "+msg[2]
        msg[2]=msg[3]
    messages[msg[0]]=[msg[1],msg[2]]

m.close()


myPeople=[]
myNames={}
myAddresses={}
idPerson=0
for p in people:
    (ID,address,name)=p[:-1].split("\t")
    ID=int(ID)
    nameRaw=name
    name=name.split(",")
    affiliation=""
    if len(name)>1:
        name[1]=name[1].strip()
        affiliation=name[1]
    if len(name)>2:
        for n in name[2:]:
            name[1]=name[1]+","+n
        affiliation=name[1]
    name=name[0]
    degree=0
    if address[:7]=='/O=OECD':
        degree=1
    if affiliation[:3]=="PAC":
        degree=2
    if affiliation in ["PAC/PUB","PAC/MKT","PAC/PLAN","PAC/PROD","PAC/RD","PAC/PP","PAC/PO","PAC/PS"]:
        degree=3
    if affiliation in ["PAC/ED","PAC/PM","PAC/CEU"]:
        degree=4
        
    if (name in myNames.keys()):
        if(address not in myAddresses.keys()):
            myAddresses[address]=myNames[name]
    else:
        if(address in myAddresses.keys()):
            myNames[name]=myAddresses[address]
        else:
            myAddresses[address]=idPerson
            myNames[name]=idPerson
            idPerson=idPerson+1
            myPeople.append(str(idPerson)+","+name+","+address+","+affiliation+","+str(degree))

a=open("c://messages//myAddresses.txt","w")
for add in myAddresses.keys():
    a.write(add+"\t"+str(myAddresses[add])+"\n")
a.close()
                            
a=open("c://messages//myNames.txt","w")
for name in myNames.keys():
    a.write(name+"\t"+str(myNames[name])+"\n")
a.close()

p=open("c://messages//myPeople.txt","w")
for people in myPeople:
    p.write(people+"\n")
p.close()
"""
"""
myMsgId=0
myRecipients=[]
myLinks={}

for p in people:
    (ID,address,name)=p[:-1].split("\t")
    if (int(ID)==int(myMsgId)):
        myRecipients.append(myAddresses[address])
    else:
        myRecipients.sort()
        for i in range(len(myRecipients)-1):
            for j in range(len(myRecipients)-i-1):
                if i in myLinks.keys():
                    if j in myLinks[i].keys():
                        myLinks[i][j]=myLinks[i][j]+1
                    else:
                        myLinks[i][j]=1
                else:
                    myLinks[i]={}
                    myLinks[i][j]=1

        myMsgId=int(ID)
        myRecipients=[]
        myRecipients.append(myAddresses[address])
l=open("c://messages//myLinks.txt","w")
for links in myLinks.keys():
    for link in myLinks[links].keys():
        l.write(str(links)+","+str(link)+","+str(myLinks[links][link])+"\n")
l.close()
"""
"""
msgInPeople={}
for p in people:
    (ID,address,name)=p[:-1].split("\t")
    ID=int(ID)
    address=myAddresses[address]
    if address in msgInPeople.keys():
        if ID not in msgInPeople[address]:
            msgInPeople[address].append(ID)
    else:
        msgInPeople[address]=[ID]

mip=open("c://messages//msgInPeople.txt","w")
for mipK in msgInPeople.keys():
    for msg in msgInPeople[mipK]:
        mip.write(str(mipK)+","+str(msg)+"\n")

mip.close()
"""

personInfo={}
for personID in msgInPeople.keys():
    personInfo[personID]={}
    personInfo[personID]["ID"]=personID
    thisPerson=myPeople[personID].split(",")
    personInfo[personID]["name"]=thisPerson[1]
    if len(thisPerson)>2:
        personInfo[personID]["address"]=thisPerson[2]
    else:
        personInfo[personID]["address"]=""
    if len(thisPerson)>3:
        personInfo[personID]["affiliation"]=thisPerson[3]
    else:
        personInfo[personID]["affilitation"]=""
    if len(thisPerson)>4:
        personInfo[personID]["degree"]=thisPerson[4]
    else:
        personInfo[personID]["degree"]="0"
    personInfo[personID]["years"]=[0,0,0,0,0,0,0,0,0]
    hisMessages=msgInPeople[personID]
    personInfo[personID]["msg"]=len(hisMessages)
    earlyDate=datetime.datetime(2012,12,31,23,59,59)
    lateDate=datetime.datetime(1960,1,1,0,0,0)
    userCorpora=""
    bigrammer=""
    for m in hisMessages:
        ID=m
        subject=messages[m][0]
        date=messages[m][1]
        if len(date)==15:
            date=datetime.datetime(int(date[:4]),int(date[4:6]),int(date[6:8]),int(date[9:11]),int(date[11:13]),int(date[13:15]))
            year=date.year
            personInfo[personID]["years"][year-2004]=personInfo[personID]["years"][year-2004]+1
            if earlyDate>date:
                earlyDate=date
            if lateDate<date:
                lateDate=date
        userCorpora=userCorpora+unicode(subject,"utf8","ignore")+"\n"
        #bigrammer=bigrammer+subject+"\n"
    personInfo[personID]["start"]=str(earlyDate)
    personInfo[personID]["end"]=str(lateDate)
    t=nltk.wordpunct_tokenize(userCorpora)
    f=nltk.FreqDist(t)
    mf=[]
    for k in f.keys():
        if k.lower() not in stopwords:
            if len(k)>1:
                mf.append({"word":k,"freq":f[k]})
    mf=mf[:20]

    tx=nltk.Text(nltk.wordpunct_tokenize(bigrammer))
    finder=nltk.collocations.BigramCollocationFinder.from_words(tx)
    
    finder.apply_word_filter(lambda w: (w.lower() in stopwords or len(w)==1))
    bigrams=finder.nbest(bigram_measures.raw_freq,10)
    b=[]
    for big in bigrams:
        b.append(big[0]+' '+big[1])

    #personInfo[personID]["corpora"]=userCorpora
    personInfo[personID]["mf"]=mf
    #personInfo[personID]["bigrams"]=b

pi=codecs.open("c://messages//personInfo.txt","w","utf8","ignore")
pi.write(json.dumps(personInfo))

pi.close()
