#!/usr/bin/env python3
import requests
import json
import matplotlib.pyplot as plt
import numpy as np
import math

class OSMAPI:
    '''
    Constructor class for OpenStreetMap API.
    '''

    def __init__(self, lat_long_list):
        '''
        Initializes the constructor with the a list of (longitude, latitude) coordinates passed from the javascript frontend, along with
        setting up general variables for running the overpass api json queries.
        '''

        self.latlong = lat_long_list
        self.overpass_url = "http://overpass-api.de/api/interpreter"
        self.query_data = []

    def run_pointwise_query(self):
        '''
        Runs an OSM query of the area surrounding each longitude, latitude point in the latlong list.
        '''

        min_coord = [999, 999]
        max_coord = [-999, -999]
        for coord in self.latlong:
            if coord[0] < min_coord[0]:
                min_coord[0] = coord[0]
            if coord[1] < min_coord[1]:
                min_coord[1] = coord[1]
            if coord[0] > max_coord[0]:
                max_coord[0] = coord[0]
            if coord[1] > max_coord[1]:
                max_coord[1] = coord[1]

        self.overpass_query = f'\
        [out:json];\
        (nwr["building"]["height"]({min_coord[0]-0.001079},{min_coord[1]-0.001523},{max_coord[0]+0.001079},{max_coord[1]+0.001523});\
        <;\
        );\
        out geom;\
        '
        # print(self.overpass_query)
        self.response = requests.get(self.overpass_url, params={'data': self.overpass_query})
        self.query_data.append(self.response.json())
        self.query_data = np.array(self.query_data)

    def debug_data(self):
        '''
        DEBUG: Prints self.data
        '''
        with open('osm_api.out', 'w+') as f:
            self.query_data.tofile(f,sep=',')

    def get_elements(self):
        '''
        Extracts elelemts and lat/long coords from buildings along with height and width parameters.
        '''

        elements = []
        [elements.extend(dic['elements']) for dic in list(self.query_data)]
        # print(elements)

        lat, long, heights, widths = [], [], [], []
        for elem in elements:
            #if not 'height' in elem['tags'].keys():
            #    continue
            if elem['type'] == 'node':
                lat.append(float(elem['lat']))
                long.append(float(elem['lon']))
                heights.append(float(elem['tags']['height']))
                widths.append(0.0)
            if elem['type'] == 'way':# or 'relation':
                minlat, minlon, maxlat, maxlon = elem['bounds']['minlat'], elem['bounds']['minlon'], elem['bounds']['maxlat'], elem['bounds']['maxlon']
                lat.append(float((maxlat-minlat)/2)+minlat)
                long.append(float((maxlon-minlon)/2)+minlon)
                height_string = elem['tags']['height']
                height = float(''.join(i for i in height_string if i.isdigit()))
                heights.append(height)
                widths.append(math.sqrt(float(maxlat-minlat)**2 + float(maxlon-minlon)**2))
        self.zipped_vector = list(zip(lat,long,widths,heights))
        return self.zipped_vector

    def debug_vector(self):
        '''
        DEBUG: Plots the let/long of the zipped vector for easy visual validation.
        '''
        numpy_vector = np.array(self.zipped_vector)
        # print(numpy_vector)
        plt.plot(numpy_vector[:, 1], numpy_vector[:, 0], 'o')
        plt.title('VALIDATE ZIPPED VECTOR')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.axis('equal')
        plt.show()

# coordlist = np.column_stack((np.linspace(34.100252,34.102349,10),np.linspace(-118.340217,-118.335341,10))) #(np.linspace(32.230056,32.230043,20),np.linspace(-110.956763,-110.951025,20))
# new_api = OSMAPI(coordlist)
# new_api.run_pointwise_query()
# new_api.debug_data()
# important_values = new_api.get_elements()
# print(important_values)
# new_api.debug_vector()
