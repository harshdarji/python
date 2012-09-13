import os
import sys
import cPickle
from urllib2 import HTTPError
from geopy import geocoders

import xml.dom.minidom


from cluster import KMeansClustering, centroid
# A very uninteresting helper function to build up an XML tree
#from linkedin__kml_utility import createKML
def createKML(items, centroid_color='ff0000ff'):
    kmlDoc = xml.dom.minidom.Document()

    kmlElement = kmlDoc.createElementNS('http://earth.google.com/kml/2.2', 'kml')
    kmlElement.setAttribute('xmlns', 'http://earth.google.com/kml/2.2')
    kmlDoc.appendChild(kmlElement)

    styleElement = kmlDoc.createElement('Style')
    styleElement.setAttribute('id', 'centroid')
    iconStyleElement = kmlDoc.createElement('IconStyle')
    colorElement = kmlDoc.createElement('color')
    colorElement.appendChild(kmlDoc.createTextNode(centroid_color))
    iconStyleElement.appendChild(colorElement)
    styleElement.appendChild(iconStyleElement)

    documentElement = kmlDoc.createElement('Document')
    documentElement.appendChild(styleElement)

    for item in items:
        pm = _createPlacemark(kmlDoc, item)

        if item['label'] == 'CENTROID':
            styleUrlElement = kmlDoc.createElement('styleUrl')
            styleUrlElement.appendChild(kmlDoc.createTextNode('#centroid'))
            pm.appendChild(styleUrlElement)

        documentElement.appendChild(pm)

    kmlElement.appendChild(documentElement)

    return kmlDoc.toprettyxml('  ', newl='\n', encoding='utf-8')


K = 10
# Use your own API key here if you use a geocoding service
# such as Google or Yahoo!
GEOCODING_API_KEY = "BDL0q23V34Gk0JwejAqXFJF9FV7eDKDRz_EfEYdiYKuW3KZHqqQ0SVwgkx6t"
CONNECTIONS_DATA="C:/Documents and Settings/cukier_j/My Documents/python/linkedin_connections.pickle"

OUT="clusters.kmeans.kml"

# Open up your saved connections with extended profile information

extended_connections = cPickle.load(open("C:/Documents and Settings/cukier_j/My Documents/python/linkedin_connections.pickle"))
def f(x): return (repr(x.__class__)=="<class 'linkedin.linkedin.Profile'>")
extended_connections = filter(f, extended_connections)
locations = [ec.location for ec in extended_connections]
g = geocoders.Yahoo(GEOCODING_API_KEY)

# Some basic transforms may be necessary for geocoding services to function properly
# Here are a few examples that seem to cause problems for Yahoo. You'll probably need
# to add your own.

transforms =[('Greater ', ''), ('Area', ''), ('San Francisco Bay', 'San Francisco')]

# Tally the frequency of each location

coords_freqs = {}
for location in locations:

    #Avoid unnecessary I/O

    if coords_freqs.has_key(location):
        coords_freqs[location][1]+=1
        continue
    transformed_location=location

    for transform in transforms:
        transformed_location=transformed_location.replace(*transform)
        while True:
            num_errors=0
            try:
                # this call returns a generator

                results = g.geocode(transformed_location, exactly_one=False)
                break
            except HTTPError, e:
                num_errors+=1
                if num_errors>3:
                    sys.exit()
                print >> sys.stderr, e
                print >> sys.stderr, 'Encountered an urllib2 error. Trying again...'
            for result in results:

                # Each result is of the form ("Description", (X,Y))

                coords_freqs[location]=[result[1],1]
                break

# Here, you could optionally segment location by continent
# country so as to avoid potentially finding a mean in the middle of the ocean

# the k-means algorithm will expect distinct points for each contact so build out
# an expanded list to pass it

expanded_coords = []
for label in coords_freqs:
    ((lat,lon),f)=coords_freqs[label]
    expanded_coords.append((label, [(lon, lat)]*f)) # flip lat/lon for google earth

# No need to clutter the map with unnecessary placemarks...

kml_items = [{'label': label, 'coords': '%s,%s' % coords[0]} for (label, coords) in expanded_coords]

# It could also be interesting to include names of your contacts on the map for display

for item in kml_items:
    item['contacts'] = '\n'.join(['%s %s.' % (ec.first_name, ec.last_name[0]) for ec in extended_connections if ec.location == item['label']])

cl = KMeansClustering([coords for (label, coords_list) in expanded_coords for coords in coords_list])

centroids=[{'label': 'CENTROID', 'coords': '%s,%s' % centroid(c)} for c in cl.getclusters(K)]

#kml_items.extend(centroids)
#kml=createKML(kml_items)

if not os.path.isdir('out'):
    os.mkdir('out')

f = open("out/" + OUT, 'w')
f.write(centroids)
f.close()

print >> sys.stderr, "Data pickled to out/" +OUT
    

