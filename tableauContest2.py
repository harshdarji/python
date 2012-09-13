# now we get more info behind the followers we got.
# it will be sthg of the form:
# response=t.users.lookup(user_id='220,456')

index=0
myList=''
info={}

for id in totalList:
    if myList=='':
        myList=str(id)
    else:
        myList=myList+','+str(id)
    if index<99:
        index=index+1
    else:
        response=t.users.lookup(user_id=myList)
        # now assuming this has worked!
        # we get only what we need from the response
        for line in response:
           info[line['id']]=followers[line['id']]
           info[line['id']]['name']=line['screen_name']
           #info[line['id']]['followers']=line['followers_count']
           #info[line['id']]['color']=line['profile_background_color']
           info (line['id']]['location']=line['location']
        index=0
        print 'got 100 ids down.'
        myList=''
if myList!='':
        response=t.users.lookup(user_id=myList)
        # now assuming this has worked!
        # we get only what we need from the response
        for line in response:
           info[line['id']]=followers[line['id']]
           info[line['id']]['name']=line['screen_name']
           info (line['id']]['location']=line['location']
           #info[line['id']]['followers']=line['followers_count']
           #info[line['id']]['color']=line['profile_background_color']
        print 'and nabbed the final '+str(len(myList.split(',')))+'.'
        

#f=open("followerInfo.txt","wb")
#f.write(json.dumps(info))
#f.close()
