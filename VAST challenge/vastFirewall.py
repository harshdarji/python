import os, csv,json
path="C:/Documents and Settings/cukier_j.OECDMAIN/My Documents/MiniChallenge2 Core Data/"

myFiles=(path+'20110413/firewall/csv/'+'20110413_VAST11MC2_firewall_log_1.csv',path+'20110413/firewall/csv/'+'20110413_VAST11MC2_firewall_log_2.csv',path+'20110413/firewall/csv/'+'20110413_VAST11MC2_firewall_log_3.csv',path+'20110413/firewall/csv/'+'20110413_VAST11MC2_firewall_log_4.csv',path+'20110413/firewall/csv/'+'20110413_VAST11MC2_firewall_log_5.csv',path+'20110414/firewall/csv/'+'20110414_VAST11MC2_firewall_log.csv',path+'20110415/firewall/csv/'+'20110415_VAST11MC2_firewall_log.csv')
out=open(path+'rules2.txt','w')
#log=[]
fileNb=0
for myFile in myFiles:
    file=open(myFile,'r')
    #listing = os.listdir(path)
    lineNb=0
    lines=csv.reader(file)
    for line in lines:
        if (len(line)>0):
            if (line[5]=="192.168.2.171" or line[5]=="192.168.2.172" or line[5]=="192.168.2.173" or line[5]=="192.168.2.174" or line[5]=="192.168.2.175" or line[6]=="192.168.2.171" or line[6]=="192.168.2.172" or line[6]=="192.168.2.173" or line[6]=="192.168.2.174" or line[6]=="192.168.2.175"):
                lineWriter=str(fileNb)+","
                lineWriter=lineWriter+str(lineNb)+","
                lineWriter=lineWriter+line[0]+","
                lineWriter=lineWriter+line[5]+","
                lineWriter=lineWriter+line[6]+","
                lineWriter=lineWriter+line[7]+","
                lineWriter=lineWriter+line[8]+","
                lineWriter=lineWriter+str(line[9])+","
                lineWriter=lineWriter+str(line[10])+","
                lineWriter=lineWriter+line[11]+","
                lineWriter=lineWriter+line[12]+","
                lineWriter=lineWriter+str(line[13])+","
                lineWriter=lineWriter+str(line[14])+"\n"
                out.write(lineWriter)
                #log.append(lineWriter)
    lineNb=lineNb+1
    file.close()
    fileNb=fileNb+1
#out.write(json.dumps(log))
out.close()
