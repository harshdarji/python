import os
path="C:/Documents and Settings/cukier_j.OECDMAIN/My Documents/vastChallenge/mc3/MC_3_Materials_4_4_2011"
out=open("C:/Documents and Settings/cukier_j.OECDMAIN/My Documents/vastChallenge/mc3/list.txt",'w')
listing = os.listdir(path)
for infile in listing:
    myfile=open(path+"/"+infile, 'r')
    keeper=False
    parse=myfile.readlines()
    for line in parse:
        if line.lower().find("vast")>-1:
            keeper=True
            break
    if keeper:
        out.write(infile+"\t"+parse[0])
    myfile.close()
out.close()

    