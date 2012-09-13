# This script will use arin.net to lookup an IP address
# and display the findings

__author__="jsalmon"
__date__ ="$Jun 24, 2010 10:40:20 AM$"

import urllib2
import re
import sys
import tempfile
import os


regexIP = r"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\." +\
            "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\." +\
            "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\." +\
            "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
regexHTML = r"<[^<]*?/?>"
#For Testing.
searchIP = "192.168.1.1"

temp = tempfile.NamedTemporaryFile()

#
#Get the source code from the web page
#
def fetchSource(url):
    url = urllib2.urlopen(url)
    source = url.read()
    return source

#
#Clean and remove all HTML
#
def cleanSource(content):
    source = str(content)
    for match in re.finditer(regexHTML, content):
        print match.group(0)
        source = source.replace(str(match.group(0)), '')
    return source

#
#Entry point
#
if __name__ == "__main__":
    #Get the IP address to search
    if searchIP:
        print "I have the IP."
    else:
        searchIP = raw_input("Please enter the IP address: ")
    #format the raw_input string for an IP
    raw_string = re.match(regexIP, searchIP)
    if raw_string:
        searchstring = raw_string.group(0)
        print "The IP I'll look for is: %s " % searchstring
    else:
        sys.exit("Exit: Please enter a valid IP address")
    url = "http://ws.arin.net/whois/?queryinput=" + searchstring

    source = fetchSource(url)
    capStart = source.index('<pre>') + 6
    capEnd = source.index('</pre>')
    printSource = cleanSource(source[capStart:capEnd])
    print
    try:
        temp.write(printSource + "\n")
        print 'temp.name:', temp.name
        temp.flush()
    finally:
    # Automatically cleans up the file
        #os.system('notepad.exe ' + temp.name) # For Windows uncomment
        os.system('gedit ' + temp.name) # For Ubuntu uncomment
        temp.close()
    
    print "Complete. All Whois sites will be added soon."