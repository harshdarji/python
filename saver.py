out=open(path+'nodes2.js','w')
out.write("var network={\n")
out.write("  nodes:[")        

writeN=0
for n in nodesA:
    out.write("    {nodeName:"+n+", group:")
    if n.split('.')[0]=='10':
        out.write('0}')
    elif n.split('.')[0]=='172':
        out.write('1}')
    elif n.split('.')[2]=='1':
        out.write('2}')
    elif n.split('.')[2]=='2':
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
        out.write('    {sourceNode:'+str(l)+', targetNode:'+str(myL)+', value:'+str(links[l][myL])+'}')
        thisL=thisL+1
        if writeN<len(links) or thisL<len(links[l]):
            out.write(',')
        out.write('\n')
out.write('  ]\n')
out.write("};\n")
out.close()