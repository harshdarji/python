import csv
ifile  = open("C:\\Documents and Settings\\cukier_j\\My Documents\\vast challenge\\MC_1_Materials_3-30-2011\\Microblogs.csv", "rb")
reader = csv.reader(ifile)
out=open("C:\\Documents and Settings\\cukier_j\\My Documents\\vast challenge\\MC_1_Materials_3-30-2011\\locs.js",'w')
rownum = 0
out.write("var locs=[")
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row        
    else:
        loc=row[2].split(" ")
        out.write("["+loc[0]+","+loc[1]+"],")
    rownum=rownum+1
out.write("];")
out.close()        
ifile.close()
print rownum
