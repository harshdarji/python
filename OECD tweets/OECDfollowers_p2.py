for id in ids:
    if index<100 or cursor+index==nbFollowers:
        index=index+1
        if myList=='':
            myList=str(id)
        else:
            myList=myList+','+str(id)
    else:
        response=t.users.lookup(user_id=myList)
        print('getting info for followers #'+str(cursor)+'-'+str(cursor+index))
        cursor=cursor+index
        # now assuming this has worked!
        # we get only what we need from the response
        for line in response:
           info[line['id']]={}
           info[line['id']]['name']=line['screen_name']
           info[line['id']]['followers']=line['followers_count']
           info[line['id']]['color']=line['profile_background_color']
        index=0
        myList=''
        f=open(orgfile,"ab")
        f.write(json.dumps(info))
        f.close()
        info={}


