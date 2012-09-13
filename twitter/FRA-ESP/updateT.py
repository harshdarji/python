# -*- coding: utf-8 -*-
poswords=["allez","aller la","aller les",u"allé", "espoir","boost","j'y crois", "pas fini", "vive la france","pour la france",u"peut égaliser","lloris","respect","merci hugo","merci capitaine"]
for t in tweets:
    text=t[1].replace("\n"," ").replace("\r"," ").replace("\t"," ")
    pos=0
    for w in poswords:
        if w in text.lower():
            pos=1
    if len(t) ==4:
        t.append(pos)
    else:
        t[4]=pos
    t[1]=text
fileh=codecs.open("output.txt","w","utf-8")
for t in tweets:
    fileh.write(str(t[0])+"\t"+t[1]+"\t"+t[2]+"\t"+t[3]+"\t"+str(t[4])+"\n")
fileh.close()
