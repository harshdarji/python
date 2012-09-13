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
corpora={}
textFile="politweets.txt"
idFile="politweetsIds.txt"

accounts={"MLP":["MLP_officiel"],"Hollande":["fhollande"],"Sarkozy":["SARKOZY_2012"],"Joly":["evajoly"],"Bayrou":["bayrou"], "EELV":["EELV","CecileDuflot","JVPlace","DominiqueVoynet","yjadot","julienbayou"], "UMP":["UMP","jeunesump","jf_cope","FLefebvre_UMP","vpecresse","VRossoDebord","DeputeTardy","franckriester","lauredlr"],"PS":["partisocialiste","pierremoscovici","aurelifil","vincent_peillon","faureolivier","frebsamen","marisoltouraine","najatvb","delphinebatho","vincentfeltesse"],"FN":["FN_officiel","FNJ_officiel"],"Modem":["modem","yannwehrling","democrates","jlbennahmias"],"Libe":["libe_2012"],"Figaro":["LeFigaro_News"],"LeMonde":["lemonde_pol"],"TF1":["TF1News_Select"],"France TV":["Francetv2012"]}
for category in accounts:
    print "New category: "+category
    print "============================================================="
    corpora[category]=""
    for account in accounts[category]:
        print "trying to get tweets from "+account 
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
                print "sending request to "+account
                response = api.user_timeline(screen_name=account,count=200)
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
            print "adding tweets..."
            for t in response:
                # here there could be some normalization of the tweet text.
                tweet=category+"\t"+account+"\t"+str(t.created_at)+"\t"+t.text+"\t"+t.id_str;
                tweets.append(tweet)
                corpora[category]+=(t.text+"\n")
                # there could be scoring here
            print 'added %i tweets.' % (len(response))
            lastIds[account]=repr(response[0].id_str)

print "encoding tweets"
f = codecs.open(textFile, encoding='utf-8', mode='wb')
for t in tweets:
 	f.write(t.replace("\n","")+"\n")
f.close()
f=open(idFile,"wb")
f.write(json.dumps(lastIds))
f.close()
