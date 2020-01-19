import googlemaps
from datetime import datetime


def googleapi(start_lat, start_lng, finish_lat, finish_lng):
    gmaps = googlemaps.Client(key='AIzaSyCCKpKX4eqJYPKQOB-HlcuxdlOArp_0nNg')



    # Request directions via public transit
    now = datetime.now()

    prompt1=gmaps.reverse_geocode((start_lat, start_lng))
    prompt2=gmaps.reverse_geocode((finish_lat, finish_lng))
    directions_result = gmaps.directions(prompt1,
                                         prompt2,
                                         mode="walking",
                                         departure_time=now)


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

    return listoflists


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1
