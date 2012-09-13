import os, csv,json
path="C:/Documents and Settings/cukier_j.OECDMAIN/My Documents/MiniChallenge2 Core Data/"

myFiles=(path+'20110413/firewall/csv/'+'20110413_VAST11MC2_firewall_log_1.csv',path+'20110413/firewall/csv/'+'20110413_VAST11MC2_firewall_log_2.csv',path+'20110413/firewall/csv/'+'20110413_VAST11MC2_firewall_log_3.csv',path+'20110413/firewall/csv/'+'20110413_VAST11MC2_firewall_log_4.csv',path+'20110413/firewall/csv/'+'20110413_VAST11MC2_firewall_log_5.csv',path+'20110414/firewall/csv/'+'20110414_VAST11MC2_firewall_log.csv',path+'20110415/firewall/csv/'+'20110415_VAST11MC2_firewall_log.csv')


nodesA=[]
nodesD={}

links={}
nbNodes=0
nbLinks=0

lineNb=0
linkNb=0
#log=[]
for myFile in myFiles:
    file=open(myFile,'r')
    #listing = os.listdir(path)
    lines=csv.reader(file)
    for line in lines:
        lineNb=lineNb+1
        if (len(line)>0):
            if line[5]!="" and line[5]!="(empty)" and line[5]!="Source IP" and line[6]!="" and line[6]!="(empty)":
                linkNb=linkNb+1
                sourceNode=-1
                if line[5] in nodesD:
                    sourceNode=nodesD[line[5]]
                else:
                    nodesD[line[5]]=nbNodes
                    sourceNode=nbNodes
                    nbNodes=nbNodes+1
                    nodesA.append(line[5])
                targetNode=-1
                if line[6] in nodesD:
                    targetNode=nodesD[line[6]]
                else:
                    nodesD[line[6]]=nbNodes
                    targetNode=nbNodes
                    nbNodes=nbNodes+1
                    nodesA.append(line[6])
    
                if sourceNode not in links:
                    links[sourceNode]={}
                links[sourceNode][targetNode]=links[sourceNode].get(targetNode,0)+1
    file.close()

out=open(path+'nodes.js','w')
out.write("var network={\n")
out.write("  nodes:[")        

writeN=0
for n in nodesA:
    out.write("    {nodeName:"+n+", group:")
    if n.split('.')[0]=='10':
        out.write('0}')
    elif n.split('.')[0]=='172':
        out.write('1}')
    elif n.split('.')[2]='1':
        out.write('2}')
    elif n.split('.')[2]='2':
        out.write('3}')
    else:
        out.write('-1}')
    writeN=writeN+1
    if writeN<len(nodesA):
        out.write(',')
    out.write('\n')
out.write('  ],\n')
out.write('  links:[')
writeN=0
for l in links:
    writeN=writeN+1
    thisL=0
    for myL in links[l]:
        out.write('    {sourceNode:'+l+', targetNode:'+myL+', value:'+links[l][myL]+'}')
        thisL=thisL+1
        if writeN<len(links) or thisL<len(links[l]):
            out.write(',')
        out.write('\n')
out.write('  ]\n')
out.write("};\n")
out.close()
