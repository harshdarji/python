from BeautifulSoup import BeautifulSoup
import json
l=open("C:\Documents and Settings\cukier_j\My Documents\python\listhtml.txt",'r')
listVotes=[]
for canton in l:
    depId=canton[-11:-8]
    canId=canton[-11:-6]
    c=open(canton[:-1],'r')
    s=BeautifulSoup(c)
    if (s.findAll('table')[0].findAll('tr')[1].findAll('td')[0].findAll('strong')[0].contents[0].encode('utf-8')[-1:]=='2'):
        #print(depId+" "+canId+": deuxième tour")
        tally={"depId":depId, "canId":canId, "EXG":0,"COM":0,"PG":0,"SOC":0,"RDG":0,"DVG":0,"VEC":0,"ECO":0,"REG":0,"AUT":0,"MODM":0,"M-NC":0,"M":0,"UMP":0,"DVD":0,"FN":0,"EXD":0,"ABS":0,"NUL":0}
        inscrits=int(s.findAll('table')[1].findAll('tr')[1].findAll('td')[1].contents[0].replace(u'\xa0','').encode('UTF-8'))
        tally["ABS"]=int(s.findAll('table')[1].findAll('tr')[2].findAll('td')[1].contents[0].replace(u'\xa0','').encode('UTF-8'))
        tally["NUL"]=int(s.findAll('table')[1].findAll('tr')[4].findAll('td')[1].contents[0].replace(u'\xa0','').encode('UTF-8'))
        for candidat in s.findAll('table')[2].findAll('tr')[1:]:
            party=candidat.findAll('td')[0].contents[0].replace("&nbsp;"," ").split(u'\xa0')[2].replace("(","").replace(")","").replace(' ','')
            votes=int(candidat.findAll('td')[1].contents[0].replace(u'\xa0',""))
            tally[party]+=votes
        listVotes.append(tally)
#print listVotes
out=open("C:\Documents and Settings\cukier_j\My Documents\python\deuxieme.js",'w')
out.write(json.dumps(listVotes))



        