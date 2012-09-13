proxies = {'http': 'http://wsg-proxy.oecd.org:80'}
import urllib2
import json
import csv

dir="C:\\Documents and Settings\\cukier_j\\My Documents\\python\\OECD tweets\\"

tweetIds=[]
enFile=open(dir+'tweetsen.csv','r')
frFile=open(dir+'tweetsfr.csv','r')

masterFile=open(dir+'tweets.csv','w')
nbTweets=0

for tweet in enFile.readlines()[1:]:
    id=json.loads(tweet)[7]
    dupe=0
    for ids in tweetIds:
        if id==ids:
            dupe=1
            break
    if dupe==0:
        masterFile.write(tweet)
        tweetIds.append(id)
        nbTweets+=1

for tweet in frFile.readlines()[1:]:
    id=json.loads(tweet)[7]
    dupe=0
    for ids in tweetIds:
        if id==ids:
            dupe=1
            break
    if dupe==0:
        masterFile.write(tweet)
        tweetIds.append(id)
        nbTweets+=1
print "consolidated file: "+str(nbTweets)+" tweets"
enFile.close()
frFile.close()
masterFile.close()

