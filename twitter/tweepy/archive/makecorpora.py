# -*- coding: utf-8 -*-
import codecs
import tweepy
import time
import json
import nltk
import re

stemmer=nltk.stem.snowball.SnowballStemmer(u"french")

n = datetime.datetime.now()

tweets=[]
lastIds={}
corpora={}
words={}
PT=[]
outputFile="corpora.js"
textFile="politweets_45j.txt"
IdFile="politweetsIds.txt"

kwFile="mots.txt"
atFile="attack.txt"
scoredFile="scored.js"

camp={'lauredlr': 4,'fn_officiel': 5, 'ump': 4, 'franckriester': 4, 'vrossodebord': 4, 'fhollande': 2, 'jvplace': 1, 'dominiquevoynet': 1, 'partisocialiste': 2, 'ianbrossat': 0, 'vincent_peillon': 2, 'sauvagelaurence':0,'tf1news_select': -1, 'francetv2012': -1, 'yjadot': 1, 'pierremoscovici': 2, 'dartigolles': 0, 'bayrou': 3, 'mlp_officiel': 5, 'eelv': 1, 'placeaupeuple': 0, 'leilachaibi': 0, 'frontdegauche': 0, 'vpecresse': 4, 'fnj_officiel': 5, 'deputetardy': 4, 'evajoly': 1, 'frebsamen': 2, 'lemonde_pol': -1, 'marisoltouraine': 2, 'delphinebatho': 2, 'jf_cope': 4, 'jeunesump': 4, 'melenchon2012': 0, 'flefebvre_ump': 4, 'najatvb': 2, 'jlbennahmias': 3, 'vincentfeltesse': 2, 'aurelifil': 2, 'lefigaro_news': -1, 'julienbayou': 1, 'faureolivier': 2, 'modem': 3, 'democrates': 3, 'yannwehrling': 3, 'sarkozy_2012': 4, 'libe_2012': -1, 'cecileduflot': 1}
f = codecs.open(kwFile, encoding='utf-8', mode='r')
keywords=f.readlines()
f.close()

for i in range(len(keywords)):
	keywords[i]=keywords[i].split("\t")
	keywords[i][1]=keywords[i][1][:-1]
	kw=""
	for k in keywords[i][1].split(" "):
		kw+=stemmer.stem(k)+" "
	keywords[i][1]=kw[:-1]
	

f = codecs.open(atFile, encoding='utf-8', mode='r')
attackwords=f.readlines()
f.close()

for a in range(len(attackwords)):
	#print a
	attackwords[a]=attackwords[a].strip().split('\t')
	for j in range(1,7):
		#print j,
		attackwords[a][j]=int(attackwords[a][j])

#n = datetime.datetime.now()

f = codecs.open(textFile, encoding='utf-8', mode='r')
tweets=f.readlines()
f.close()

f=codecs.open(scoredFile,encoding='utf-8', mode='wb')
f.write("var PT=[")

#f = codecs.open(idFile,encoding='utf-8',mode='r')
#ids=f.read()
#f.close()
#lastIds=json.loads(ids)
time_format = "%Y-%m-%d %H:%M:%S"
byday=[]
for d in range(45):
	byday.append("")
	
accounts={"MLP":["MLP_officiel"],"Hollande":["fhollande"],"Sarkozy":["SARKOZY_2012"], "Joly":["evajoly"],"Bayrou":["bayrou"], "EELV":["EELV","CecileDuflot","JVPlace", "DominiqueVoynet","yjadot","julienbayou"], "UMP":["UMP","jeunesump","jf_cope", "FLefebvre_UMP","vpecresse","VRossoDebord","DeputeTardy","franckriester","lauredlr"], "PS":["partisocialiste","pierremoscovici","aurelifil","vincent_peillon","faureolivier", "frebsamen","marisoltouraine","najatvb","delphinebatho","vincentfeltesse"], "FN":["FN_officiel","FNJ_officiel"],"Modem":["modem","yannwehrling","democrates", "jlbennahmias"],"Libe":["libe_2012"],"Figaro":["LeFigaro_News"],"LeMonde":["lemonde_pol"], "TF1":["TF1News_Select"],"France TV":["Francetv2012"],"Melenchon":["Melenchon2012"], "FDG":["SauvageLaurence","IanBrossat","Dartigolles","FrontDeGauche","PlaceAuPeuple","leilachaibi"]}
for k in accounts.keys():
 	corpora[k]=""
 	words[k]=[]

pat1=re.compile(r'(http|https)://[^\s]*',re.IGNORECASE | re.DOTALL)
pat2=re.compile(r"[',;\.:/!?()\"#*%]",re.IGNORECASE | re.DOTALL)
pat3=re.compile(r" +",re.IGNORECASE | re.DOTALL)
PT=[]
scoredTweets=0
attackerTweets=0
couldbeAttacks=0
for i in range(len(tweets)):
	if (i%500 == 0):
		print str(i) + " tweets down."
	#print "now treating tweet" +str(i)
	t=tweets[i]
	isScored=0
	isAttack=0
	isCrit=0
	to={}
	tw=t.split('\t')
	category=tw[0]
	corpora[category]+=tw[3]+'\n'
	d=datetime.datetime.fromtimestamp(time.mktime(time.strptime(tw[2], time_format)))
	diff=45-(n-d).days
	if diff in range(0,44):
		byday[diff]+=tw[3]+'\n'
	to["account"]=tw[1]
	to["category"]=tw[0]	
	to["date"]=tw[2]
	to["day"]=str(d.year)+"-"+str(d.month)+"-"+str(d.day)
	to["secs"]=(n-d).total_seconds()
	to["text"]=tw[3]
	to["ids"]=i
	#to["id_str"]=tw[4];
	to["score"]={"critique":0,"culture":0,"dem":0,"eco":0,"egal":0,"env":0,"peur":0,"promo":0,"social":0,"valeurs":0};
	#print ("building main parts - done")
	textwords=pat1.sub('',tw[3])
	textwords=pat2.sub(' ',textwords)
	textwords=pat3.sub(' ',textwords).split(" ")
	tw=""
	for w in textwords:
		tw+=stemmer.stem(w)+" "
	textwords=tw[:-1].split(" ")
	#print ("tokenized and stemmed - done")						
	for j in range(len(textwords)):

		for kw in keywords:
			kws=kw[1].split(' ')
			l=len(kws)
		
			if textwords[j]==kws[0] and j+l<len(textwords):
				#print "tweet #" + str(i) + "may contain "+kw[1]
				foundword=1
				for k in range(l):
					if textwords[j+k]<>kws[k]:
						#print "but "+textwords[j+k]+" is not like "+kws[k]
						foundword=0
						break
					#else:
						#print textwords[j+k]+" is indeed like "+kws[k]
				if foundword==1:
					to["score"][kw[0]]+=1
					isScored=1
					#print "one point in "+kw[0]

	if to["score"]["critique"]>0 and camp[to["account"].lower()]>-1:
		to["attacks"]=[0,0,0,0,0,0]
		isCrit=1
		for a in attackwords:
			if a[camp[to["account"].lower()]+1]==0:
				if a[0].lower() in to["text"]:
					for j in range(6):
						to["attacks"][j]+=a[j+1]
						isAttack=1
	scoredTweets+=isScored
	attackerTweets+=isAttack
	couldbeAttacks+=isCrit
	
	PT.append(to)

	f.write (json.dumps(to))
	if(i<len(tweets)-1):
		f.write(",")
	

f.write("];")
f.close()

print "Total tweets "+ str(len(tweets))
print "of which - " + str(scoredTweets) + " are scored"
print "of which - " + str(couldbeAttacks) + " could be attacks"
print "of which - " + str(attackerTweets) + " really are attacks"


pat1 = re.compile(r"(^|[\n ])(([\w]+?://[\w\#$%&~.\-;:=,?@\[\]+]*)(/[\w\#$%&~/.\-;:=,?@\[\]+]*)?)", re.IGNORECASE | re.DOTALL)
for c in corpora.keys():
    corpora[c]=pat1.sub(r'',corpora[c])


F=['au', 'aux', 'avec', 'ce', 'ces', 'dans', 'de', 'des', 'du', 'elle', 'en', 'et', 'eux', 'il', 'je', 'la', 'le', 'leur', 'lui', 'ma', 'mais', 'me', 'm\xc3\xaame', 'mes', 'moi', 'mon', 'ne', 'nos', 'notre', 'nous', 'on', 'ou', 'par', 'pas', 'pour', 'qu', 'que', 'qui', 'sa', 'se', 'ses', 'son', 'sur', 'ta', 'te', 'tes', 'toi', 'ton', 'tu', 'un', 'une', 'vos', 'votre', 'vous', 'c', 'd', 'j', 'l', '\xc3\xa0', 'm', 'n', 's', 't', 'y', '\xc3\xa9t\xc3\xa9', '\xc3\xa9t\xc3\xa9e', '\xc3\xa9t\xc3\xa9es', '\xc3\xa9t\xc3\xa9s', '\xc3\xa9tant', '\xc3\xa9tante', '\xc3\xa9tants', '\xc3\xa9tantes', 'suis', 'es', 'est', 'sommes', '\xc3\xaates', 'sont', 'serai', 'seras', 'sera', 'serons', 'serez', 'seront', 'serais', 'serait', 'serions', 'seriez', 'seraient', '\xc3\xa9tais', '\xc3\xa9tait', '\xc3\xa9tions', '\xc3\xa9tiez', '\xc3\xa9taient', 'fus', 'fut', 'f\xc3\xbbmes', 'f\xc3\xbbtes', 'furent', 'sois', 'soit', 'soyons', 'soyez', 'soient', 'fusse', 'fusses', 'f\xc3\xbbt', 'fussions', 'fussiez', 'fussent', 'ayant', 'ayante', 'ayantes', 'ayants', 'eu', 'eue', 'eues', 'eus', 'ai', 'as', 'avons', 'avez', 'ont', 'aurai', 'auras', 'aura', 'aurons', 'aurez', 'auront', 'aurais', 'aurait', 'aurions', 'auriez', 'auraient', 'avais', 'avait', 'avions', 'aviez', 'avaient', 'eut', 'e\xc3\xbbmes', 'e\xc3\xbbtes', 'eurent', 'aie', 'aies', 'ait', 'ayons', 'ayez', 'aient', 'eusse', 'eusses', 'e\xc3\xbbt', 'eussions', 'eussiez', 'eussent', '.', '#', '@', '?', '...', '!', "'", ',', '\\xe0', 'les', '-', '"', '\\u2019', ':', 'cette', '\\xe9', 'a', '\\xe8', ')', 'r', 'e', '\\xe7', "c'est", '\\xea', 'pr', '\\xbb', '\xc3\xa0', '%', '\\xab', '\xe2\x80\x99', 're', '/', 'via', '11', '\\xbb:', ']', '[', 'RT', '&', 'gt', ';', '#', '".', "'#", '+', '+,', '&#', '.@', '|', '\\xb4', '^', 'cc', '(#', '(', u'', u'\\xe0', u'\\xe9t\\xe9']



otherTokens={}
unique={}
t={}
f={}
for c in corpora.keys():
	t[c]=nltk.wordpunct_tokenize(corpora[c])
	f[c]=nltk.FreqDist(t[c])
	
for c in corpora.keys():
	
	otherTokens[c]=[]
	for d in corpora.keys():
		if d<>c:
			otherTokens[c].extend(t[d])
	otherTokens[c]=set(otherTokens[c])
	unique[c]=[]
	for w in f[c].keys():
		if w not in otherTokens[c]:
			unique[c].append(w)
mf={}
for c in corpora.keys():
	mf[c]=[]
	for k in f[c].keys():
		if k.lower().encode("unicode_escape") not in F:
			mf[c].append({"word":k,"freq":f[c][k]})
text={}
bigrams={}
bigram_measures = nltk.collocations.BigramAssocMeasures()
for c in corpora.keys():
	for i in range(len(t[c])):
		t[c][i]=t[c][i].encode("unicode_escape")

	text[c]=nltk.Text(t[c])
	finder = nltk.collocations.BigramCollocationFinder.from_words(text[c])
	finder.apply_word_filter(lambda w: w.lower() in F)
	bigrams[c]=finder.nbest(bigram_measures.raw_freq,10)
	
# il est temps de conclure et de sortir un fichier...

var={}
def notrouble(w): return ',' not in w and '\"' not in w
file="var NLP={\n"
for c in corpora.keys():
	var[c]="\""+c+"\":{unique: \""
	var[c]=var[c]+filter(notrouble,(", ".join(unique[c])))
	var[c]=var[c]+"\", mostf:\""
	for i in range(10):
		if notrouble(mf[c][i]['word']):
			var[c]=var[c]+mf[c][i]['word']+", "
	var[c]=var[c][:-2]+"\", bigrams:\""
	for i in range(10):
		if notrouble(" ".join(bigrams[c][i])):
			var[c]=var[c]+" ".join(bigrams[c][i])+", "
	var[c]=var[c][:-2]+"\"},\n"
var[c]=var[c][:-2]

for c in var.keys():
	file=file+var[c]
file = file + "};"

f = codecs.open(outputFile, encoding='utf-8', mode='wb')
f.write(file)
f.close()