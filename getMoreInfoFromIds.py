# now we get more info behind the followers we got.
# it will be sthg of the form:
# response=t.users.lookup(user_id='220,456')

index=0
myList=''
info={}

for id in newList:
    if index<100:
        index=index+1
        if myList=='':
            myList=str(id)
        else:
            myList=myList+','+str(id)
    else:
        response=t.users.lookup(user_id=myList)
        # now assuming this has worked!
        # we get only what we need from the response
        for line in response:
           info[line['id']]={}
           info[line['id']]['name']=line['screen_name']
           info[line['id']]['followers']=line['followers_count']
           info[line['id']]['color']=line['profile_background_color']
        index=0
        myList=''

f=open("info.txt","wb")
f.write(json.dumps(info))
f.close()
