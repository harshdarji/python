proxies = {'http': 'http://wsg-proxy.oecd.org:80'}
import pickle
import urllib
import BeautifulSoup
from BeautifulSoup import BeautifulSoup  
urlStart="http://www.datacatalogs.org/"
urlSearch="dataset?page="
#urlEnd="&content=list&event=M2011&lang=FR&num_results=30&pid=search&search[name]=&search[firstname]=&search[nation]=&search[start_no]=&search_sort=name&search_sort_order=ASC&top_results=3&type=search"



def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

pageCatalogs=[]

for i in range(1,11):
    url=urlStart+urlSearch+str(i)
    print "opening "+url+"..."
    filehandle=urllib2.urlopen(url)
    html=filehandle.read()
    filehandle.close()
    soupSearch=BeautifulSoup(html)
    print "url\tname"
    for a in soupSearch.ul.findAll("a"):
        print a.attrs[0][1]+"\t"+a.contents[0]
        pageCatalogs.append({"pagename":a.attrs[0][1].replace('/catalog/',''), "name":a.contents[0]})
    print "- parsed!"
    
for i in range(len(pageCatalogs)):
    url=urlStart+'catalog/'+pageCatalogs[i]["pagename"]
    filehandle=urllib2.urlopen(url)
    html=filehandle.read()
    filehandle.close()
    soupPage=BeautifulSoup(html)
    s=soupPage.table
    pageCatalogs[i]["url"]=s.findAll("tr")[0].findAll("td")[1].findNext("a").attrs[0][1].strip()
    try:
        pageCatalogs[i]["desc"]=s.findAll("tr")[1].findAll("td")[1].contents[0]
    except:
        pass
    try:
        pageCatalogs[i]["pub"]=s.findAll("tr")[2].findAll("td")[1].contents[0]
    except:
        pass
    try:
        pageCatalogs[i]["license"]=s.findAll("tr")[3].findAll("td")[1].contents[0]
    except:
        pass
    try:
        pageCatalogs[i]["coverage"]=s.findAll("tr")[4].findAll("td")[1].contents[0]
    except:
        pass
    
    url=urlStart+'catalog/history/'+pageCatalogs[i]["pagename"]
    filehandle=urllib2.urlopen(url)
    html=filehandle.read()
    filehandle.close()
    soupHistory=BeautifulSoup(html)
    s=soupHistory.table
    pageCatalogs[i]["created"]=s.findAll("tr")[len(s.findAll("tr"))-1].findAll("a")[1].contents[0]
    print pageCatalogs[i]

