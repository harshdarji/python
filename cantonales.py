proxies = {'http': 'http://wsg-proxy.oecd.org:80'}
import pickle
import urllib
import BeautifulSoup
from BeautifulSoup import BeautifulSoup  
urlStart="http://elections.interieur.gouv.fr/CN2011/"
#urlEnd="&content=list&event=M2011&lang=FR&num_results=30&pid=search&search[name]=&search[firstname]=&search[nation]=&search[start_no]=&search_sort=name&search_sort_order=ASC&top_results=3&type=search"

listCandidats=[]
listVotes=[]
cantonFile='C:\Documents and Settings\cukier_j.OECDMAIN\My Documents\python\list_cantons.txt'

cantonList = open(cantonFile)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    



for canton in cantonList:
    print canton
    filehandle=open(canton.strip())
    html=filehandle.read()
    soupCanton=BeautifulSoup(html)
    #depName=soup.findAll('strong')[1].contents[0].strip()
    depId=canton[71:74]
    canId=canton[75:80]
    cantonName = soupCanton.findAll('strong')[0].contents[3].replace("&gt;","").strip()
    print cantonName
    tally={"EXG":0,"COM":0,"PG":0,"SOC":0,"RDG":0,"DVG":0,"VEC":0,"ECO":0,"REG":0,"AUT":0,"MODM":0,"M-NC":0,"M":0,"UMP":0,"DVD":0,"FN":0,"EXD":0,"ABS":0,"NUL":0}
    tally['ABS']+=int(soupCanton.findAll('table')[1].findAll('tr')[2].findAll('td')[1].contents[0].replace(u'\xa0',""))
    tally['NUL']+=int(soupCanton.findAll('table')[1].findAll('tr')[4].findAll('td')[1].contents[0].replace(u'\xa0',""))
    for candidat in soupCanton.findAll('table')[3].findAll('tr')[1:]:
        gender=candidat.findAll('td')[0].contents[0].replace("&nbsp;"," ").split(u'\xa0')[0]
        name=candidat.findAll('td')[0].contents[0].replace("&nbsp;"," ").split(u'\xa0')[1]
        party=candidat.findAll('td')[0].contents[0].replace("&nbsp;"," ").split(u'\xa0')[2].replace("(","").replace(")","")
        votes=int(candidat.findAll('td')[1].contents[0].replace(u'\xa0',""))
        tally[party]+=votes
        myCandidat={}
        myCandidat["depId"]=depId
        myCandidat["canId"]=canId
        myCandidat["gender"]=gender
        myCandidat["name"]=name
        myCandidat["party"]=party
        myCandidat["votes"]=votes
        listCandidats.append(myCandidat)
        
    tally["depId"]=depId
    tally["canId"]=canId
    listVotes.append(tally)
    
print listCandidats
print listVotes

candidatFile=open('candidats','w')
candidatFile.write(json.dumps(listCandidats))
candidatFile.close()

votesFile=open('votes','w')
votesFile.write(json.dumps(listVotes))
votesFile.close()

        

