import json
import os

resultaat = []


def tijden():
    
    if os.stat('./Flask-webserver/log_prob.json').st_size == 0:
    #if os.stat('log_prob.json').st_size == 0:

        return
    
    json_data=open('./Flask-webserver/log_prob.json')
    #json_data=open('log_prob.json')


    # EERST DE LIJST ORDENEN

    data=json.load(json_data)
    data=sorted(data, key=lambda item : item["cid"])
    #print(len(data))
    joinlist=[]
    leftlist=[]
    timelist=[]

    #TIJD IN SECONDEN OMZETTEN
    for i in range(len(data)):

        timelist=data[i]['time'].split(":")
        #timelist=map(int,timelist)
        seconden=int(timelist[0])*3600+int(timelist[1])*60+int(timelist[2])
        #print(seconden)
        data[i]['time']=seconden

    for i in range(len(data)):
        
        #print(data[i]['cid'],data[i]['time'])
        if(data[i]['entry']=='joined'):

            #print("Joined:",data[i]['time'])
            newitem = { "cid": data[i]['cid'], "time": data[i]['time'] }
            joinlist.append(newitem)

        if(data[i]['entry']=='left'):

            #print("Left:",data[i]['time'])
            newitem = { "cid": data[i]['cid'], "time": data[i]['time'] }
            leftlist.append(newitem)

        #splitsop=data[i]['time'].split(":")
        #print(splitsop)
    """
    print('Joinlist:')
    for i in range(len(joinlist)):

        print(joinlist[i]['cid'])

    print('Leftlist:')
    for i in range(len(leftlist)):

        print(leftlist[i]['cid'])
    """
    waitlist=[]
    #print(len(leftlist), leftlist)
    #print('Lengte van leftlist :', len(leftlist))
    #print('Lengte van leftlist :', len(joinlist))


    #print("Joinlist: ", joinlist)
    #print("Leftlist :", leftlist)

    if(len(joinlist)!=len(leftlist)):
        return waitlist

    for i in range(len(joinlist)):
        j=0
        if(joinlist[i]['cid']==leftlist[j]['cid']):
            #print(joinlist[i]['cid'])
            time = (leftlist[j]['time'] - joinlist[i]['time'])

            newitem = { "cid": joinlist[i]['cid'], "time": time }
            waitlist.append(newitem)

            del leftlist[j]

        else:

            while(j<len(leftlist)):
                if(joinlist[i]['cid']==leftlist[j]['cid']):
                    time = (leftlist[j]['time']-joinlist[i]['time'])
                    
                    newitem = { "cid": joinlist[i]['cid'], "time": time }
                    waitlist.append(newitem)

                    del leftlist[j]
                j+=1

    '''
    print('Waitlist:')    
    for i in range(len(waitlist)):

        print(waitlist[i]['cid'],waitlist[i]['time'],'seconden')

    return waitlist
    '''

resultaat=tijden()
print(resultaat)