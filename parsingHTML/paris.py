from geopy import geocoders
import codecs
output=codecs.open("C:\\Documents and Settings\\cukier_j\\My Documents\\python\\geocoder\\latlon.txt","w","utf-8")
g=geocoders.Google(domain='maps.google.fr')
input=open("C:\\Documents and Settings\\cukier_j\\My Documents\\python\\geocoder\\paris.txt","r")
paris=input.readlines()
input.close()

for adresse in paris:
    place, (lat, lng) = list(g.geocode(adresse,exactly_one=False))[0]
    output.write(place+"\t"+str(lat)+"\t"+str(lng)+"\n")
    print place
output.close()

