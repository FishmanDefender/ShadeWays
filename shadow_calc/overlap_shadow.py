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
    path_bounds = (min(path_lat), min(path_long), max(path_lat), max(path_long))
    delta_lat, delta_long = (path_bounds[2]-path_bounds[0]), (path_bounds[3]-path_bounds[1])
    grid_spacing = max(delta_lat,delta_long)/10000
    grid_lat, grid_long = list(np.arange(path_bounds[0],delta_lat+path_bounds[0],grid_spacing)),list(np.arange(path_bounds[1],delta_long+path_bounds[1],grid_spacing))

    interpolated_path = []
    for i in range(len(path_coords)-1):
        interpolated_path.extend(list(np.arange(path_coords[i],path_coords[i+1],grid_spacing/2)))

'''
2. Associate grid points with the path. Store them in a list.
	2.1. Associate grid points with the path:
        The easiest method might be to parametrize the line.
        Then to plug in the line parameter with discrete intervals.
    Then to coerce the result points to the grid points.
    Then to remove any duplicate points.
'''

    grid_path_associations = []
    for lat_val in grid_lat:
        for long_val in grid_long:
            for point in interpolated_path:
                if


'''
3. Import the shadow parallelograms. Associate grid points with the shadows. Remove duplicate points from the list.
	3.1. Sort the 4 points of each parallelogram by least y to greatest y. Also take the least and greatest x. Only examine the grid points with xy in this range.
	3.2. Use the 3 lowest-y points to create two lines. Go through the grid points horizontal line by line, starting from the lowest y. Only add those grid points to the list of shadow grid points which have x values in between the x values of the bounding lines for that y.
	3.3. Once reaching the second lowest y-value of the 4 shadow parallelogram points, change that bounding line. Again change the bounding line once reaching the 3rd-lowest-y point.
	3.4 Collect all the grid points that were in shadow in a list.
4. Search each path point in the shadow list to see if it has a match. The number of path tuples that have matches out of the total gives the shadow percent.
'''

    shadow_coords = []
    for rectangle in shadowlist:
        shadow_coords=[rectangle[i:i+2] for i in range(0,len(rectangle),2)]

        shadow_lat, shadow_long = [x[0] for x in shadow_coords], [x[1] for x in shadow_coords]
        shadow_bounds = (min(shadow_lat), min(shadow_long), max(shadow_lat), max(shadow_long))
        s_delta_lat, s_delta_long = (shadow_bounds[2]-shadow_bounds[0]), (shadow_bounds[3]-shadow_bounds[1])
        s_grid_spacing = max(s_delta_lat,s_delta_long)/1000
        s_grid_lat, s_grid_long = list(np.arange(shadow_bounds[0],s_delta_lat+shadow_bounds[0],s_grid_spacing)),list(np.arange(shadow_bounds[1],s_delta_long+shadow_bounds[1],s_grid_spacing))

        lat_
