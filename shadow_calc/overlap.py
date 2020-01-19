#!/usr/bin/env python3
import numpy as np

def overlap(shadowlist, path_coords):
    '''
    Overlap calculator to get the percent shadow.
    '''

    path_lat, path_long = [x[0] for x in path_coords], [x[1] for x in path_coords]
    path_bounds = (min(path_lat), min(path_long), max(path_lat), max(path_long))
    delta_lat, delta_long = (path_bounds[2]-path_bounds[0]), (path_bounds[3]-path_bounds[1])

    grid_spacing = max(delta_lat,delta_long)/1000
    grid_lat, grid_long = list(np.arange(0,delta_lat,grid_spacing)),list(np.arange(0,delta_long,grid_spacing))