# -*- coding: utf-8 -*-
import json

f = codecs.open("keywords.txt", encoding='utf-8', mode='r')
kw=f.readlines()
f.close()
searches=[]
for i in range(len(kw)):
    s=kw[i][:-1].split("\t")
    if len(s)>1:
        searches.append(s)

output=[]

for s in searches:
    s1=s[0].replace("/search?","").split("&")

    s2=[]

    for t in s1:
        t=t.split("=")
        if len(t)==2:
            if t[1]<>"":
                s2.append({t[0]:t[1]})
    s3={}

    for t in s2:
        k=t.keys()[0]
        if k[:5]=="value":
            o=k.replace("value","option")
            ov=""
            for t2 in s2:
                if t2.keys()[0]==o:
                    ov=t2.values()[0]
                    break
        if ov<>"":	
            kv=t.values()[0]
            s3[ov]=kv
        else:
            if k[:6]<>"option":
                s3[t.keys()[0]]=t.values()[0]

    s3["visits"]=s[1]
    #if "fullText" in s3.keys():
    output.append(s3)


f = codecs.open("output.txt", encoding='utf-8', mode='wb')
f.write(json.dumps(output,encoding='latin1'))
f.close()
