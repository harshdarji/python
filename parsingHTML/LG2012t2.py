# -*- coding: utf-8 -*-
import os
import codecs
output=codecs.open("output.txt","w","utf-8")
files=os.listdir("C:\Documents and Settings\cukier_j\My Documents\python\parsingHTML\lg2012T2")

data=[]

for f in files:
    
    circo=f.replace(".html","")
    if circo!=f:
        circo=circo[0:3]+"-"+circo[3:]
        
        soup=localsoup(f)
        
        t1=soup.findAll("table")[1]
        inscrits=float(t1.findAll("tr")[1].findAll("td")[1].contents[0].replace(u'\xa0',""));
        abstentions=float(t1.findAll("tr")[2].findAll("td")[1].contents[0].replace(u'\xa0',""));
        blancs=float(t1.findAll("tr")[4].findAll("td")[1].contents[0].replace(u'\xa0',""));
        votants=inscrits-abstentions
        exprimes=votants-blancs
        data.append([circo,"","","","inscrits",inscrits,1])
        data.append([circo,"","","","abstentions",abstentions,abstentions/inscrits])
        data.append([circo,"","","","blanc",blancs,blancs/inscrits])

        t2=soup.findAll("table")[2]
        for tr in t2.findAll("tr")[1:]:
            record=[circo]
            candidat=tr.find("td").contents[0].split("&nbsp;")
            c1=candidat[0].split(u'\xa0')
            if(c1[0]=="M."):
                record.append("m")
            else:
                record.append("f")
            record.append(c1[1])
            c2=candidat[1].split(u'\xa0')
            record.append(c2[0])
            record.append(c2[1].replace("(","").replace(")",""))
            voix=float(tr.findAll("td")[1].contents[0].replace(u'\xa0',""))
            record.append(voix)
            record.append(voix/exprimes)        
            data.append(record)



for d in data:
   for i in range(len(d)):
       if i>4:
           if i==5:
               output.write(str(int(d[i])))
           else:
               output.write(str(d[i]))
       else:
           output.write(d[i])     
       if i<6:
            output.write('\t')
       else:
            output.write('\n')
output.close()

    
    
        
        
        
        