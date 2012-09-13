accountHash={"evajoly":0,"francetv2012":1,"ump":2,"jeunesump":3,"jf_cope":4,"flefebvre_ump":5,"vpecresse":6,"vrossodebord":7,"deputetardy":8,"franckriester":9,"lauredlr":10,"mlp_officiel":11,"modem":12,"yannwehrling":13,"democrates":14,"jlbennahmias":15,"tf1news_select":16,"fn_officiel":17,"fnj_officiel":18,"partisocialiste":19,"pierremoscovici":20,"aurelifil":21,"vincent_peillon":22,"faureolivier":23,"frebsamen":24,"marisoltouraine":25,"najatvb":26,"delphinebatho":27,"vincentfeltesse":28,"eelv":29,"cecileduflot":30,"jvplace":31,"dominiquevoynet":32,"yjadot":33,"julienbayou":34,"fhollande":35,"libe_2012":36,"sarkozy_2012":37,"bayrou":38,"lemonde_pol":39,"lefigaro_news":40,"melenchon2012":41,"leilachaibi":42,"ianbrossat":43,"dartigolles":44,"frontdegauche":45,"placeaupeuple":46,"sauvagelaurence":47};

PT2=[]
f=codecs.open("scored2.js",encoding='utf-8', mode='wb')
f.write("var PT2=[")

for i in range(len(tweets)):
    myTweet=tweets[i].split("\t")
    t=[i,accountHash[myTweet[1].lower()],myTweet[4][:-1],PT[i]["secs"],PT[i]["day"],PT[i]["score"].values()]
    if "attacks" in PT[i].keys():
        t.append(PT[i]["attacks"])
    PT2.append(t)
    f.write (json.dumps(t))
    if(i<len(tweets)-1):
        f.write(",")

f.write("];")
f.close()
