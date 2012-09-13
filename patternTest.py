from pattern.web   import Twitter, Google, plaintext
from pattern.table import Table
t = Table()
for politician, party in (("nicolas sarkozy", "ump"), ("dsk", "ps")):
    for tweet in Twitter().search(politician):
        if tweet.language in ("nl", "fr"):
            s = plaintext(tweet.description)
            s = Google().translate(s, tweet.language, "en")
#            w = sum([sentiment_score(word) for word in s.split(" ")])
            t.append([politician, party, tweet.date, s])