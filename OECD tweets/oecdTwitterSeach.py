proxies = {'http': 'http://wsg-proxy.oecd.org:80'}
import urllib2
import json
import csv
urlStart="http://search.twitter.com/search.json?q=oecd&rpp=100&page="
tweets = []

for i in range(1,16):
    filehandle=urllib2.urlopen(urlStart+str(i))
    print "loading page "+str(i)
    results=json.loads(filehandle.read())["results"]
    tweets += results

users=[]
for tweet in tweets:
    isIn=0
    user={"user":tweet["from_user"], "id":tweet["from_user_id_str"]}
    for u in users:
        if(u["id"]==user["id"]):
            isIn=1
            break
    if (isIn==0):
        users.append(user)
tweetFile=open('tweets.csv', 'wb')

for tweet in tweets:
    row=u''.encode("utf-8")
    for k in x.keys():
        myk=tweet[k]
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
    tweetFile.write(row)

tweetFile.close()

usersFile=open('users.csv','wb')
for user in users:
    row=u''.encode("utf-8")
    for k in x.keys():
        myk=tweet[k]
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
    usersFile.write(row)
usersFile.close()

