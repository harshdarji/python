import urllib2
import json
urlStart="http://search.twitter.com/search.json?q="
urlEnd="&rpp=100&page="
candidats=("hollande","aubry")
lastId={"hollande":"","aubry":"","royal":"","valls":"","montebourg":"","baylet":""}
tweets={"hollande":[],"aubry":[],"royal":[],"valls":[],"montebourg":[],"baylet":[]}
users={"hollande":[],"aubry":[],"royal":[],"valls":[],"montebourg":[],"baylet":[]}
sunday=u'Sun, 16 Oct 2011'

for candidat in candidats:
    print "----------------------------------------------------------------"
    print candidat
    print "----------------------------------------------------------------"
    nbTweets=0
    for i in range(1,16):
        print "loading page "+str(i)
        url=urlStart+candidat+urlEnd+str(i)
        query=urllib2.urlopen(url)
        results=json.loads(query.read())["results"]
        duplicate=0
        for tweet in results:
            if tweet["id_str"]==lastId[candidat]:
                duplicate=1
                break
            if tweet["created_at"][:16]!=sunday:
                duplicate=1
                break
            if tweet["iso_language_code"]==u'fr':
                tweets[candidat].append(tweet)
                nbTweets+=1    
        if duplicate==1:
            break
    print str(nbTweets)+" new tweets"
    lastId[candidat]=tweet["id_str"]
