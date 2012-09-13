import urllib2
import json
#tweets=[]
#maxT=10000
#tweetsNb=0
#queryBase="https://twitter.com/search.json?q=%23FranceEspagne&rpp=100&result_type=recent&until=2012-06-24"
#maxId=-1
while tweetsNb<maxT:
    if(maxId==-1):
        tweeturl=queryBase
    else:
        tweeturl=queryBase+"&max_id="+str(maxId)
    print tweeturl
    tweetStream=urllib2.urlopen(tweeturl)
    tweetHTML=tweetStream.read()
    tweetStream.close()
    tweetJSON=json.loads(tweetHTML)
    for tweet in tweetJSON['results']:
        tweetOutput=[]
        tweetOutput.append(tweet['id'])
        if (tweet['id']<maxId or maxId==-1):
            maxId=tweet['id']
        tweetOutput.append(tweet['text'])
        tweetOutput.append(tweet['created_at'])
        tweetOutput.append(tweet['from_user'])
        tweets.append(tweetOutput)
        tweetsNb=tweetsNb+1
    
                           
