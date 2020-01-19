#Shadow Finder module:::::
#Input: Building array; Lat& long location of interest.
#Output: The corner coordinates of the shadow rectangles.

#Python documentation https://docs.python.org/3/index.html
#PySolar package documentation: https://pysolar.readthedocs.io/en/latest/

from pysolar.solar import *
import datetime
import math
#import numpy as np
#from osm_api import OSMAPI

def sunAngle(lat, long):
    #date = datetime.datetime.now()
    date = datetime.datetime.now(datetime.timezone.utc)
    altitude_deg = get_altitude(lat, long, date)
    azimuth_deg = get_azimuth(lat, long, date)
    return [altitude_deg, azimuth_deg]


#Data on the building locations are given by
#[...,[latitude, longitude, width, height],...]
#The latitude and longitude are of the building's center.
#The width is in meters, and is the full width.
#The height of the building is also in meters.

#Shadow data is returned by the program.
#Assumes all the shadows are rectangles.
#The shadows' positions are given
#by the geographic coordinates of their corners.
#The data type is of a once-nested list:
#[...,[corner1_latitude, corner1_longitude, corner2_latitude,..., corner4...],...]

#shadowFinder algorithm:
#coordinates of building's near corners = building center +/- width/2
    #the coordinates are added and subtracted in the direction
        #perpendicular to the sun's azimuth.
        #have to convert the width to radial coordinates.
    #building coordinates are always listed in the counter-clockwise direction
def shadowFinder(buildingList, lat, long):
    [altitude_deg, azimuth_deg] = sunAngle(lat, long)
    lat_rad = lat*math.pi/180
    long_rad = long*math.pi/180
    if altitude_deg < 0:
        raise ValueError("Warning: Sun is below the horizon. Shadow finding does not work!") #if altitude is greater than or equal to zero, continue.
            #if altitude is less than zero, return an error. (Sun is below the horizon.)
    azimuth_rad = azimuth_deg*(math.pi/180) #shadow is in opposite direction as sun. In radians.
    if (azimuth_rad < math.pi):
        azimuth_rad = azimuth_rad + 2*math.pi
    if (azimuth_rad > math.pi):
        azimuth_rad = azimuth_rad - 2*math.pi
    azperp_rad = azimuth_rad - (math.pi/2) #The perpendicular to the azimuth.
    negazim_rad = -azimuth_rad
    thetazimuth = (math.pi/2)-azimuth_rad
    thetazperp = thetazimuth - (math.pi/2)
    sunthetazim = thetazimuth + math.pi
    latconv = 1/(111132.954-559.822*math.cos(2*lat_rad)+1.175*math.cos(4*lat_rad)) #Wikipedia: convert to degrees of latitude from meters.
    aparam = 6378137
    eccen = ((aparam**2)-(6356752.3142**2))/(aparam**2) #eccentricity of the WGS84 earth ellipsoid
    longconv = (180*((1-((eccen*math.sin(lat_rad))**2))**(1/2)))/(math.pi*aparam*math.cos(lat_rad))
    #180/(math.pi*6378137*math.cos((6356752.3142/6378137)*math.tan))
    #height = []
    shadowLength = []
    shadowList = []
    for i in range(len(buildingList)):
        #height.append(buildingList[i][3])
        shadowLength.append(buildingList[i][3]/(math.tan(altitude_deg*(math.pi/180)))) #shadow length = building height times the cotangent of the altitude
        shadowList.append([0,0,0,0,0,0,0,0])
        shadowList[i][0] = buildingList[i][0] + (buildingList[i][2]/2)*math.sin(thetazperp) #corner1_latitude
        shadowList[i][2] = buildingList[i][0] - (buildingList[i][2]/2)*math.sin(thetazperp) #corner2_latitude
        shadowList[i][1] = buildingList[i][1] + (buildingList[i][2]/2)*math.cos(thetazperp) #corner1_longitude
        shadowList[i][3] = buildingList[i][1] - (buildingList[i][2]/2)*math.cos(thetazperp) #corner2_longitude
        shadowList[i][4] = shadowList[i][0] + latconv*math.sin(sunthetazim)*shadowLength[i] #corner3_latitude (shadow)
        shadowList[i][6] = shadowList[i][2] + latconv*math.sin(sunthetazim)*shadowLength[i] #corner4_latitude (shadow)
        shadowList[i][5] = shadowList[i][1] + longconv*math.cos(sunthetazim)*shadowLength[i] #corner3_longitude (shadow)
        shadowList[i][7] = shadowList[i][3] + longconv*math.cos(sunthetazim)*shadowLength[i] #corner4_longitude (shadow)
    return shadowList
