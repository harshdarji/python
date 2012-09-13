proxies = {'http': 'http://wsg-proxy.oecd.org:80'}
import urllib2
import json
import csv
urlStart="http://search.twitter.com/search.json?q=oecd&rpp=100&page="
dir="C:\\Documents and Settings\\cukier_j\\My Documents\\python\\OECD tweets\\"
tweets = []
cfgFile=open(dir+'cfgFile.txt','r')
lastId=cfgFile.read()[7:]
cfgFile.close()
print lastId

users=[]
userFile=open(dir+'users.csv','r')
for line in userFile.readlines():
    users.append({"user": line.split('\t')[0], "id": line.split('\t')[1]})
userFile.close()

goAhead=1
newLines=0
newTweets=[]
for i in range(1,16):
    filehandle=urllib2.urlopen(urlStart+str(i))
    print "loading page "+str(i)
    results=json.loads(filehandle.read())["results"]
    for result in results:
        if result["id_str"]==lastId:
            goAhead=0
            break
        else:
            newTweets.append(result)
            newLines +=1
    if goAhead==0:
        break

print "got "+str(newLines)+" new tweets."

newUsers=[]
for tweet in newTweets:
    isIn=0
    user={"user":tweet["from_user"], "id":tweet["from_user_id_str"]}
    for u in users:
        if(u["id"]==user["id"]):
            isIn=1
            break
    if (isIn==0):
        newUsers.append(user)

print "from "+str(len(newUsers))+" new users."

tweetFile=open(dir+'tweetsen.csv', 'ab')
for tweet in reversed(newTweets):
    tweetA=[]    
    for k in tweet.keys():
        tweetA.append(tweet[k])
    tweetFile.write(json.dumps(tweetA))
    tweetFile.write('\n')
tweetFile.close()

usersFile=open(dir+'users.csv','ab')
for user in newUsers:
    row=u''.encode("utf-8")
    for k in user.keys():
        myk=user[k]
        myType=type(myk).__name__
        if myType=='str':
            row+= myk.encode("utf-8")
        else:
            if myType=='unicode':
                row += myk
            else:
                if myType!='NoneType':
                    row+=str(myk).encode("utf-8")
        row+=u'\u0009'
    usersFile.write(row.encode("utf-8")+'\n')
usersFile.close()
if(len(newTweets)>0):
    cfgFile=open('cfgFile.txt','w')
    cfgFile.write("lastId:"+newTweets[0]["id_str"])
    cfgFile.close()
    print "updating lastId to "+newTweets[0]["id_str"]

    

