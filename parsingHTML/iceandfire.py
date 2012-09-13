proxies = {'http': 'http://wsg-proxy.oecd.org:80'}
from pickle import *
from BeautifulSoup import *
from urllib2 import *
from json import *


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

#chapters=[]
characters={}
charactersInChapters=[]
places={}
terms={}
placesInChapters=[]
termsInChapters=[]


#chapters=[]
urlStart="http://awoiaf.westeros.org"
urlChapters="/index.php/Chapters"
#urlEnd="&content=list&event=M2011&lang=FR&num_results=30&pid=search&search[name]=&search[firstname]=&search[nation]=&search[start_no]=&search_sort=name&search_sort_order=ASC&top_results=3&type=search"

"""
divs=[{'number':13,'book':"A Game of Thrones"},{'number':17,'book':"A Storm of Swords"},{'number':21,'book':"A Clash of Kings"},{'number':25,'book':"A Feast for Crows"},{'number':29,'book':"A Dance with Dragons"}]
url=urlStart+urlChapters
filehandle=urlopen(url)
html=filehandle.read()
filehandle.close()
soup=BeautifulSoup(html)
index=0
for div in divs:
    for a in soup.findAll("div")[div['number']].findAll("a"):
        chapter={}
        chapter['index']=index
        index+=1
        chapter['book']=div['book']
        chapter['title']=a.contents[0].strip()
        chapter['url']=a.attrs[0][1].strip()
        chapters.append(chapter)
"""

urlStart="http://awoiaf.westeros.org"
characters={}
charactersInChapters=[]
places={}
terms={}
placesInChapters=[]
termsInChapters=[]
charIndex=0
placeIndex=0
termIndex=0
for chapter in chapters:
    url=urlStart+chapter["url"]
    filehandle=urlopen(url)
    html=filehandle.read()
    filehandle.close()
    soup=BeautifulSoup(html)
    if len(soup.findAll("table", {"class":"wikitable"}))>0:
        t=soup.findAll("table", {"class":"wikitable"})[0]
        present=True
        for td in t.findAll("td"):
            if len(td.findAll("b"))>0:
                present=(td.find("b").contents[0].strip()=="Appearing:") #if no bold text is present, we keep the value for the previous cell, and true by default
            for li in td.findAll("li"):
                name=li.find("a").contents[0].strip()
                if name not in characters.keys():
                    characters[name]={"url":li.find("a").attrs[0][1].strip(),"index":charIndex}
                    charIndex+=1
                cic={"chapter":chapter["index"],"character":name,"role":"present" if present else "mentioned"}
                charactersInChapters.append(cic)
        if len(soup.findAll("table", {"class":"wikitable"}))>1:
            t=soup.findAll("table", {"class":"wikitable"})[1]
            for td in t.findAll("td"):
                if(len(td.findAll("b"))>0):
                    place=(td.find("b").contents[0].strip()=="Places:")
                else:
                    place=True #assuming places are in that table then.
                for li in td.findAll("li"):
                    name=li.find("a").contents[0].strip()
                    if place:
                        if name not in places.keys():
                            places[name]={"url":li.find("a").attrs[0][1].strip()}
                        pic={"chapter":chapter["index"],"place":name}
                        placesInChapters.append(pic)
                    else:
                        if name not in terms.keys():
                            terms[name]={"url":li.find("a").attrs[0][1].strip()}
                        tic={"chapter":chapter["index"],"term":name}
                        termsInChapters.append(tic)
        else:
            print "WARNING: no places or terms table for chapter "+chapter["title"]+" ("+str(chapter["index"])+")"
    else:
        print "WARNING: no character table found for chapter "+chapter["title"]+" ("+str(chapter["index"])+")"
    print "done for "+chapter["title"]                    
                