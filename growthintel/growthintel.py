APIKey="00a5f2164e5e49b29981ddcbe9df7d7c"
import parse
import json
output={"type":"FeatureCollection","features":[]}

postcodes=["AB","AL","B","BA","BB","BD","BH","BL","BN","BR","BS","BT","CA","CB","CF","CH","CM","CO","CR","CT","CV","CW","DA","DD","DE","DG","DH","DL","DN","DT","DY","E","EC","EH","EN","EX","FK","FY","G","GL","GU","HA","HD","HG","HP","HR","HS","HU","HX","IG","IM","IP","IV","KA","KT","KW","KY","L","LA","LD","LE","LL","LN","LS","LU","M","ME","MK","ML","N","NE","NG","NN","NP","NR","NW","OL","OX","PA","PE","PH","PL","PO","PR","RG","RH","RM","S","SA","SE","SG","SK","SL","SM","SN","SO","SP","SR","SS","ST","SW","SY","TA","TD","TF","TN","TQ","TR","TS","TW","UB","W","WA","WC","WD","WF","WN","WR","WS","WV","YO","ZE","BR","CR","DA","E","EC","EN","HA","IG","KT","N","NW","RM","SE","SM","SW","TW","UB","W","WC","WD"]
stuburl="http://geocoding.cloudmade.com/"+APIKey+"/geocoding/v2/find.js?query=postcode:"
urlend="&return_geometry=true"

for postcode in postcodes:
    url=stuburl+postcode+urlend;
    data=json.loads(htmlify(url))
    print postcode,len(url)
    if ("features" in data):
        output["features"].append(data["features"][0])
    else:
        print "no data found for "+postcode
        
