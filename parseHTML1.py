proxies = {'http': 'http://wsg-proxy.oecd.org:80'}
import pickle
import urllib
import BeautifulSoup
from BeautifulSoup import BeautifulSoup  
urlStart="http://org-results.semideparis.com/2011/index.php?page="
urlEnd="&content=list&event=M2011&lang=FR&num_results=30&pid=search&search[name]=&search[firstname]=&search[nation]=&search[start_no]=&search_sort=name&search_sort_order=ASC&top_results=3&type=search"

runners=[]
for i in range(1,791):
    url=urlStart+str(i)+urlEnd
    filehandle=urllib.urlopen(url, proxies=proxies)
    html=filehandle.read()
    soup=BeautifulSoup(html)
    for line in soup.tbody.findAll('tr'):
        runner=""
        tokens=line.findAll('td')
        runner+="{place: "+tokens[0].contents[0]+", "
        runner+="plcat: "+tokens[1].contents[0]+", "
        runner+="dossard: "+tokens[2].contents[0]+", "
        runner+="name: "+tokens[3].contents[1].contents[0].split('(')[0]+", "
        runner+="country: "+tokens[3].contents[1].contents[0].split('(')[1].replace(')','')+", "
        runner+="cat: "+tokens[4].contents[0]+", "
        time5=tokens[5].contents[0].split(':')
        if(len(time5)==3):
            runner+="time5:"+str(int(time5[2])+60*int(time5[1])+3600*int(time5[0]))+", "
        else:
            runner+="time5: -1, "
        time10=tokens[6].contents[0].split(':')
        if(len(time10)==3):
            runner+="time10:"+str(int(time10[2])+60*int(time10[1])+3600*int(time10[0]))+", "
        else:
            runner+="time10: -1, "
        time15=tokens[7].contents[0].split(':')
        if(len(time15)==3):        
            runner+="time15:"+str(int(time15[2])+60*int(time15[1])+3600*int(time15[0]))+", "
        else:
            runner+="time10: -1, "
        timeF=tokens[8].contents[0].split(':')
        if(len(timeF)==3):
            runner+="timeF:"+str(int(timeF[2])+60*int(timeF[1])+3600*int(timeF[0]))+"}, "
        else:
            runner+="timeF: -1},"
            
        runners.append(runner)
    
    filehandle.close()
output = open('runners.txt', 'wb')
for line in runners:
    output.write(line.encode('utf-8')+"\n")
output.close()

