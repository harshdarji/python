wait_period = 2 # secs

for id in ids:
    if index<100 or cursor+index==nbFollowers:
        index=index+1
        if myList=='':
            myList=str(id)
        else:
            myList=myList+','+str(id)
    else:
        if wait_period > 3600: # 1 hour
            print 'Too many retries. Saving partial data to disk and exiting'
            f = file(str(index+cursor)+orgfile, 'wb')
            f.write(json.dumps(info))
            f.close()
            exit()
        try:
            response=t.users.lookup(user_id=myList)
            wait_period=2
        except twitter.api.TwitterHTTPError, e:
            if e.e.code == 401:
                print 'Encountered 401 Error (Not Authorized)'
                print 'User %s is protecting their tweets' % (SCREEN_NAME, )
            elif e.e.code in (502, 503):
                print 'Encountered %i Error. Trying again in %i seconds' % (e.e.code,wait_period)
                time.sleep(wait_period)
                wait_period *= 1.5
                continue
            elif t.account.rate_limit_status()['remaining_hits'] == 0:
                status = t.account.rate_limit_status()
                now = time.time() # UTC
                when_rate_limit_resets = status['reset_time_in_seconds'] # UTC
                sleep_time = when_rate_limit_resets - now
                print 'Rate limit reached. Trying again in %i seconds' % (sleep_time, )
                time.sleep(sleep_time)
                continue
        except:
            print 'il se passe un problème. on réessaye dans %i seconds' % (sleep_time, )
            time.sleep(wait_period)
            wait_period *= 1.5
            continue

        print('getting info for followers #'+str(cursor)+'-'+str(cursor+index)+' '+str(len(response))+'/100 results')
        cursor=cursor+index
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
        print 'saving '+str(len(response))+' results.'
        
              



