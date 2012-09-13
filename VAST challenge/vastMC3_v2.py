import os
path="C:/Documents and Settings/cukier_j.OECDMAIN/My Documents/vastChallenge/mc3/MC_3_Materials_4_4_2011"
out=open("C:/Documents and Settings/cukier_j.OECDMAIN/My Documents/vastChallenge/mc3/list-kw.txt",'w')
listing = os.listdir(path)
#groups=('network of dread', 'ethical treatment of lab mice', 'brotherhood of antartica', 'anarchists for freedom', 'brotherhood of maintenance of way employees')
keywords=('attack', 'threat', 'terror', 'strike', 'explosion', 'bomb', 'danger', 'arson', 'suspicious', 'homeland security')
for infile in listing:
    myfile=open(path+"/"+infile, 'r')
    keeper=False
    parse=myfile.readlines()
    for line in parse:
        for group in groups:
            if line.lower().find(group)>-1:
                keeper=True
                break
    if keeper:
        out.write(infile+"\t"+parse[0])
    myfile.close()
out.close()

    