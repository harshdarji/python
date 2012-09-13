tweetFile=open('tweets.csv', 'wb')
tweetFile.write(json.dumps(tweets[0].keys())+'\n')
for tweet in reversed(tweets):
    tweetA=[]    
    for k in tweet.keys():
        tweetA.append(tweet[k])
    tweetFile.write(json.dumps(tweetA))
    tweetFile.write('\n')

tweetFile.close()
cfgFile=open('cfgFile.txt','w')
cfgFile.write("lastId:"+tweets[0]["id_str"])
cfgFile.close()



