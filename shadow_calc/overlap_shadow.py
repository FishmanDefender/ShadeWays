#!/usr/bin/env python3
import numpy as np

def overlap(shadowlist, path_coords):
    '''
    Overlap calculator to get the percent shadow.
    '''

'''
Grid method of calculating overlap:
1. Create grid: Import the path. Use the path extrema as the xy limits of the grid. Use a uniform point interval that is equal in the x and y directions.
	1.1 The path is a list of two-element lists, with form [[lat, long], [lat, long],…].
	1.2 Find path extrema: Search for greatest, smallest path long, lat.
	1.3: Make grid: might be best to use a numpy.linspace.
'''
    path_lat, path_long = [x[0] for x in path_coords], [x[1] for x in path_coords]
    path_bounds = (round(min(path_lat),6), round(min(path_long),6), round(max(path_lat),6), round(max(path_long),6))
    delta_lat, delta_long = (path_bounds[2]-path_bounds[0]), (path_bounds[3]-path_bounds[1])
    #grid_spacing = max(delta_lat,delta_long)/10000
    grid_spacing = 1e-6
    grid_lat, grid_long = list(np.arange(path_bounds[0],delta_lat+path_bounds[0],grid_spacing)),list(np.arange(path_bounds[1],delta_long+path_bounds[1],grid_spacing))

'''
2. Associate grid points with the path. Store them in a list.
	2.1. Associate grid points with the path:
        The easiest method might be to parametrize the line.
        Then to plug in the line parameter with discrete intervals.
    Then to coerce the result points to the grid points.
    Then to remove any duplicate points.
'''
    path_grid = []
    path_lengths = []

    for i in range(len(path_lat)-1):
        path_lengths.append(((path_lat[i+1]-path_lat[i])**2+(path_long[i+1]-path_long[i])**2)**(1/2))
    for i in range(len(path_lat)):

        (path_lat[i+1]-path_lat[i]

'''
3. Import the shadow parallelograms. Associate grid points with the shadows. Remove duplicate points from the list.
	3.1. Sort the 4 points of each parallelogram by least y to greatest y. Also take the least and greatest x. Only examine the grid points with xy in this range.
	3.2. Use the 3 lowest-y points to create two lines. Go through the grid points horizontal line by line, starting from the lowest y. Only add those grid points to the list of shadow grid points which have x values in between the x values of the bounding lines for that y.
	3.3. Once reaching the second lowest y-value of the 4 shadow parallelogram points, change that bounding line. Again change the bounding line once reaching the 3rd-lowest-y point.
	3.4 Collect all the grid points that were in shadow in a list.
'''
'''
4. Search each path point in the shadow list to see if it has a match. The number of path tuples that have matches out of the total gives the shadow percent.
'''
