#proxies = {'http': 'http://wsg-proxy.oecd.org:80'}
from pickle import *
from urllib2 import *
from BeautifulSoup import *
from parse import *
import os
import codecs
resultat=codecs.open("C:\\Documents and Settings\\cukier_j\\My Documents\\python\\parsingHTML\\2tour.txt","w","utf-8")


listCandidats=["Mme Eva JOLY","Mme Marine LE PEN","M. Nicolas SARKOZY","M. Jean-Luc MÉLENCHON","M. Philippe POUTOU","Mme Nathalie ARTHAUD","M. Jacques CHEMINADE","M. François BAYROU","M. Nicolas DUPONT-AIGNAN","M. François HOLLANDE"]
listVotes=[]
#resultat='premierTour.txt'

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

os.chdir("C:\Documents and Settings\cukier_j\My Documents\python\parsingHTML\PR2012-2")
dir=os.listdir(os.getcwd())
index=0
for file in dir:
    index+=1
    if(index%100)==0:
        print ".",
    
    filehandle=open(file,'r')
    html=filehandle.read()
    soup=BeautifulSoup(html)
    filehandle.close()
    isDep=(len(file)==8)
    name=soup.findAll("strong")[0].contents[-1].replace(u'\xa0&gt;\xa0','')
    reg=soup.findAll("a")[3].contents[0]
    
    if isDep:
        dep=name
    else:
        dep=soup.findAll("a")[4].contents[0]

    resultatLine=str(index)+"\t"+reg+"\t"+dep+"\t"+name+"\t"+str(isDep)+"\t"
    t=soup.findAll("table")[0]
    
    inscrits=int(t.findAll("tr")[1].findAll("td")[1].contents[0].replace(u'\xa0',''))
    abstentions=int(t.findAll("tr")[2].findAll("td")[1].contents[0].replace(u'\xa0',''))
    blancs=int(t.findAll("tr")[4].findAll("td")[1].contents[0].replace(u'\xa0',''))
    resultatLine+=str(inscrits)+"\t"
    resultatLine+=str(abstentions)+"\t"
    resultatLine+=str(blancs)
    t=soup.findAll("table")[1]
    for tr in range(1,len(t)):
        resultatLine+="\t"+str((int(t.findAll("tr")[tr].findAll("td")[1].contents[0].replace(u'\xa0',''))))
    resultat.write(resultatLine+"\n") 
resultat.close()
