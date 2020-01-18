#!/usr/bin/env python3
import requests
import json
import matplotlib.pyplot as plt
import numpy as np

class OSMAPI:
    '''
    Constructor class for OpenStreetMap API.
    '''

    def __init__(self, long_lat_list):
        '''
        Initializes the constructor with the a list of (longitude, latitude) coordinates passed from the javascript frontend, along with
        setting up general variables for running the overpass api json queries.
        '''

        self.longlat = long_lat_list
        self.overpass_url = "http://overpass-api.de/api/interpreter"
        self.query_data = []

    def run_pointwise_query(self):
        '''
        Runs an OSM query of the area surrounding each longitude, latitude point in the longlat list.
        '''

        min_coord = [999, 999]
        max_coord = [-999, -999]
        for coord in self.longlat:
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
        [bbox:{min_coord[0]-0.001079},{min_coord[1]-0.001523},{max_coord[0]+0.001079},{max_coord[1]+0.001523}];\
        (nwr["height"];\
        );\
        out center;\
        '
        print(self.overpass_query)
        self.response = requests.get(self.overpass_url, params={'data': self.overpass_query})
        self.query_data.append(self.response.json())
        self.query_data = np.array(self.query_data)

    def print_data(self):
        '''
        DEBUG: Prints self.data
        '''
        print(self.query_data)

coordlist = np.column_stack((np.linspace(34.092672,34.106389,10),np.linspace(-118.345723,-118.317927,10))) #(np.linspace(32.230056,32.230043,20),np.linspace(-110.956763,-110.951025,20))
new_api = OSMAPI(coordlist)
new_api.run_pointwise_query()
new_api.print_data()
