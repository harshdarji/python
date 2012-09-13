#proxies = {'http': 'http://wsg-proxy.oecd.org:80'}
from pickle import *
from urllib2 import *
from BeautifulSoup import *
from parse import *

urlStart="http://elections.interieur.gouv.fr/PR2012/"
#urlEnd="&content=list&event=M2011&lang=FR&num_results=30&pid=search&search[name]=&search[firstname]=&search[nation]=&search[start_no]=&search_sort=name&search_sort_order=ASC&top_results=3&type=search"
ResultatDep=[]
listePages=[]
listeCom=[]
ResultatCom=[]
departements=[
["01 - AIN","082/001/index.html"]
["02 - AISNE","022/002/index.html"]
["03 - ALLIER","083/003/index.html"]
["04 - ALPES DE HAUTE PROVENCE","093/004/index.html"]
["05 - HAUTES ALPES","093/005/index.html"]
["06 - ALPES MARITIMES","093/006/index.html"]
["07 - ARDECHE","082/007/index.html"]
["08 - ARDENNES","021/008/index.html"]
["09 - ARIEGE","073/009/index.html"]
["10 - AUBE","021/010/index.html"]
["11 - AUDE","091/011/index.html"]
["12 - AVEYRON","073/012/index.html"]
["13 - BOUCHES DU RHONE","093/013/index.html"]
["14 - CALVADOS","025/014/index.html"]
["15 - CANTAL","083/015/index.html"]
["16 - CHARENTE","054/016/index.html"]
["17 - CHARENTE MARITIME","054/017/index.html"]
["18 - CHER","024/018/index.html"]
["19 - CORREZE","074/019/index.html"]
["2A - CORSE SUD","094/02A/index.html"]
["2B - HAUTE CORSE","094/02B/index.html"]
["21 - COTE D'OR","026/021/index.html"]
["22 - COTES D'ARMOR","053/022/index.html"]
["23 - CREUSE","074/023/index.html"]
["24 - DORDOGNE","072/024/index.html"]
["25 - DOUBS","043/025/index.html"]
["26 - DROME","082/026/index.html"]
["27 - EURE","023/027/index.html"]
["28 - EURE ET LOIR","024/028/index.html"]
["29 - FINISTERE","053/029/index.html"]
["30 - GARD","091/030/index.html"]
["31 - HAUTE GARONNE","073/031/index.html"]
["32 - GERS","073/032/index.html"]
["33 - GIRONDE","072/033/index.html"]
["34 - HERAULT","091/034/index.html"]
["35 - ILLE ET VILAINE","053/035/index.html"]
["36 - INDRE","024/036/index.html"]
["37 - INDRE ET LOIRE","024/037/index.html"]
["38 - ISERE","082/038/index.html"]
["39 - JURA","043/039/index.html"]
["40 - LANDES","072/040/index.html"]
["41 - LOIR ET CHER","024/041/index.html"]
["42 - LOIRE","082/042/index.html"]
["43 - HAUTE LOIRE","083/043/index.html"]
["44 - LOIRE ATLANTIQUE","052/044/index.html"]
["45 - LOIRET","024/045/index.html"]
["46 - LOT","073/046/index.html"]
["47 - LOT ET GARONNE","072/047/index.html"]
["48 - LOZERE","091/048/index.html"]
["49 - MAINE ET LOIRE","052/049/index.html"]
["50 - MANCHE","025/050/index.html"]
["51 - MARNE","021/051/index.html"]
["52 - HAUTE MARNE","021/052/index.html"]
["53 - MAYENNE","052/053/index.html"]
["54 - MEURTHE ET MOSELLE","041/054/index.html"]
["55 - MEUSE","041/055/index.html"]
["56 - MORBIHAN","053/056/index.html"]
["57 - MOSELLE","041/057/index.html"]
["58 - NIEVRE","026/058/index.html"]
["59 - NORD","031/059/index.html"]
["60 - OISE","022/060/index.html"]
["61 - ORNE","025/061/index.html"]
["62 - PAS DE CALAIS","031/062/index.html"]
["63 - PUY DE DOME","083/063/index.html"]
["64 - PYRENEES ATLANTIQUES","072/064/index.html"]
["65 - HAUTES PYRENEES","073/065/index.html"]
["66 - PYRENEES ORIENTALES","091/066/index.html"]
["67 - BAS RHIN","042/067/index.html"]
["68 - HAUT RHIN","042/068/index.html"]
["69 - RHONE","082/069/index.html"]
["70 - HAUTE SAONE","043/070/index.html"]
["71 - SAONE ET LOIRE","026/071/index.html"]
["72 - SARTHE","052/072/index.html"]
["73 - SAVOIE","082/073/index.html"]
["74 - HAUTE SAVOIE","082/074/index.html"]
["75 - PARIS","011/075/index.html"]
["76 - SEINE MARITIME","023/076/index.html"]
["77 - SEINE ET MARNE","011/077/index.html"]
["78 - YVELINES","011/078/index.html"]
["79 - DEUX SEVRES","054/079/index.html"]
["80 - SOMME","022/080/index.html"]
["81 - TARN","073/081/index.html"]
["82 - TARN ET GARONNE","073/082/index.html"]
["83 - VAR","093/083/index.html"]
["84 - VAUCLUSE","093/084/index.html"]
["85 - VENDEE","052/085/index.html"]
["86 - VIENNE","054/086/index.html"]
["87 - HAUTE VIENNE","074/087/index.html"]
["88 - VOSGES","041/088/index.html"]
["89 - YONNE","026/089/index.html"]
["90 - TERRITOIRE DE BELFORT","043/090/index.html"]
["91 - ESSONNE","011/091/index.html"]
["92 - HAUTS DE SEINE","011/092/index.html"]
["93 - SEINE SAINT-DENIS","011/093/index.html"]
["94 - VAL DE MARNE","011/094/index.html"]
["95 - VAL D'OISE","011/095/index.html"]
["971 - GUADELOUPE","001/971/index.html"]
["972 - MARTINIQUE","002/972/index.html"]
["973 - GUYANE","003/973/index.html"]
["974 - LA REUNION","004/974/index.html"]
["976 - MAYOTTE","006/976/index.html"]
["988 - NOUVELLE CALEDONIE","000/988/index.html"]
["987 - POLYNESIE FRANCAISE","000/987/index.html"]
["975 - SAINT PIERRE ET MIQUELON","000/975/index.html"]
["986 - WALLIS-ET-FUTUNA","000/986/index.html"]
["977 et 978 - SAINT-MARTIN/SAINT-BARTHELEMY","000/977/index.html"]]
listCandidats=["Mme Eva JOLY","Mme Marine LE PEN","M. Nicolas SARKOZY","M. Jean-Luc MÉLENCHON","M. Philippe POUTOU","Mme Nathalie ARTHAUD","M. Jacques CHEMINADE","M. François BAYROU","M. Nicolas DUPONT-AIGNAN","M. François HOLLANDE"]
listVotes=[]
resultat='premierTour.txt'

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    



for dep in departements:
    print dep[0]
    depSoup=soup(urlStart+dep[1])
    t=depSoup.findAll("table")[0]
    #resultats departement
    inscrits=int(t.findAll("tr")[1].findAll("td")[1].contents[0].replace(u'\xa0',''))
    abstentions=int(t.findAll("tr")[2].findAll("td")[1].contents[0].replace(u'\xa0',''))
    blancs=int(t.findAll("tr")[4].findAll("td")[1].contents[0].replace(u'\xa0',''))
    ResultatDep.append([dep[0],"inscrits",inscrits])
    ResultatDep.append([dep[0],"abstentions",inscrits])
    ResultatDep.append([dep[0],"blancs",inscrits])
    t=depSoup.findAll("table")[1]
    for tr in range(1,len(t)):
        ResultatDep.append([dep[0],t[tr].findAll("td")[0].contents[0],int(t[tr].findAll("td")[1].contents[0].replace(u'\xa0',''))])

    listA=depSoup.findAll("a")
    listA=[a for a in listA if len(a.contents[0])==1 and "http" not in a.attrs[0][1]]
    for a in listA:
        listePages.append[dep[0],a.contents[0],a.attrs[1][1]]
        urlPage=urlStart+dep[1].split("/")[0]+a.attrs[1][1]
        soupPage=soup(
        
