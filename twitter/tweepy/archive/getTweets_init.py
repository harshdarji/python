# -*- coding: latin-1 -*-
import codecs
import tweepy
import time
import json

key="ppHAC64cJGBBlwIx9ES4fw"
secret="P6DfN32vTZDkSZfglYryXWStT3xJaOKaRUz8SszHQ"
access_token="14624309-G4FTU63rdlGEFPCJdKbN1qLcOwlRysTou06ZtYVto"
access_token_secret="rxVrryQdlcfZPuO8QrHal4DMj2tI9WHaNXhwSOGdSM"
auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets=[]
lastIds={}

textFile="politweets.txt"
idFile="politweetsIds.txt"

accounts={"MLP":"MLP_officiel","Hollande":"fhollande","Sarkozy":"SARKOZY_2012","Joly":"evajoly","Bayrou":"bayrou"}
for account in accounts.keys():
    wait_period = 2 # secs
    ok = -1
    while ok !=0:
        if wait_period > 3600: # 1 hour
            print 'Too many retries. Saving partial data to disk and exiting'
            f=open(textFile,"wb")
            f.write(json.dumps(tweets))
            f.close()
            f=open(idFile,"wb")
            f.write(json.dumps(ids))
            f.close()
        try:
            response = api.user_timeline(screen_name=accounts[account],count=200)
            wait_period = 2
        except tweepy.TweepError:
            if api.rate_limit_status()['remaining_hits']== 0:
                status=api.rate_limit_status()
                now = time.time() # UTC
                when_rate_limit_resets = status['reset_time_in_seconds'] # UTC
                sleep_time = when_rate_limit_resets - now
                print 'Rate limit reached. Trying again in %i seconds' % (sleep_time, )
                time.sleep(sleep_time)
                continue
            else:
                print 'Encountered an error. Trying again in %i seconds' % (wait_period)
                time.sleep(wait_period)
                wait_period *= 1.5
                continue
            

        ok = 0
    print "obtained "+str(len(response))+" tweets for account "+account+"."
    for t in response:
        tweet=account+"\t"+str(t.created_at)+"\t"+t.text+"\t"+t.id_str;
        tweets.append(tweet)
    lastIds[account]=repr(response[0].id_str)
f = codecs.open(textFile, encoding='utf-8', mode='wb')
for t in tweets:
 	f.write(t)
f.close()
f=open(idFile,"wb")
f.write(json.dumps(lastIds))
f.close()
