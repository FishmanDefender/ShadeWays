import googlemaps
from datetime import datetime
from flask import jsonify
import json


def googleapi(start_tup, finish_tup):
    gmaps = googlemaps.Client(key='AIzaSyCCKpKX4eqJYPKQOB-HlcuxdlOArp_0nNg')

    # Request directions via public transit
    now = datetime.now()

    directions_result = gmaps.directions(origin=(start_tup[0],start_tup[1]),
                                        destination=(finish_tup[0],finish_tup[1]),
                                        mode='walking',
                                        departure_time='now')

    # with open('output.json','w+') as f:
    #     json.dump(directions_result,f)

    d_r= ''.join(str(directions_result))
    d_r_string=d_r.split()
    length=len(d_r_string)
    listoflists =[]
    latlng=[]
    counter=0

    new_output=dict(directions_result[0])
    keys=new_output.keys()


    var1=new_output['legs']

    new_outputv2=dict(var1[0])

    var1_s= ''.join(str(var1))
    var1_ss=var1_s.split()
    lengthv2=len(var1_ss)
    for i in range(lengthv2):
        #print(var1_ss[i])
        if var1_ss[i]=="{'lat':":
            sr1=listToString((listToString(var1_ss[i+1])).split(","))
            latlng.append(float(sr1))
        if var1_ss[i]=="'lng':":
            sr2=listToString((listToString(var1_ss[i+1])).split("},"))
            latlng.append(float(sr2))
            listoflists.append(latlng)
            latlng=[]

    return listoflists, directions_result

def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1
