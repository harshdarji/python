# this just selects the items in totalList with several followers.

newList=[]
newFollowers={}

for id in totalList:
    if(followers[id]['nb']>1):
        newList.append(id)
        newFollowers[id]=followers[id]
        