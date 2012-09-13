from urllib2 import *
from BeautifulSoup import *

def htmlify(url):
    filehandle=urlopen(url)
    html=filehandle.read()
    filehandle.close()
    return html

def soupify(url):
    filehandle=urlopen(url)
    html=filehandle.read()
    filehandle.close()
    soup=BeautifulSoup(html)
    return soup

def localsoup(file):
    filehandle=open(file,'r')
    html=filehandle.read()
    filehandle.close()
    soup=BeautifulSoup(html)
    return soup

    