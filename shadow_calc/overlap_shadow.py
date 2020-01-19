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

    interpolated_path = []
    for i in range(len(path_coords)-1):
        interpolated_path.extend(list(np.arange(path_coords[i],path_coords[i+1],grid_spacing/2)))

    shadow_coords, good_point_index = [], []
    for rectangle in shadowlist:
        shadow_coords = [rectangle[i:i+2] for i in range(0,len(rectangle),2)]

        shadow_lat, shadow_long = [x[0] for x in shadow_coords], [x[1] for x in shadow_coords]
        shadow_bounds = (min(shadow_lat), min(shadow_long), max(shadow_lat), max(shadow_long))
        s_delta_lat, s_delta_long = (shadow_bounds[2]-shadow_bounds[0]), (shadow_bounds[3]-shadow_bounds[1])
        s_grid_spacing = max(s_delta_lat,s_delta_long)/1000
        s_grid_lat, s_grid_long = list(np.arange(shadow_bounds[0],s_delta_lat+shadow_bounds[0],s_grid_spacing)),list(np.arange(shadow_bounds[1],s_delta_long+shadow_bounds[1],s_grid_spacing))

        vertex1 = shadow_lat.index(shadow_bounds[0])
        vertex4 = shadow_lat.index(shadow_bounds[2])
        vertex3 = shadow_long.index(shadow_bounds[3])
        vertex2 = shadow_long.index(shadow_bound[1])

        for point in interpolated_path:
            latp, longp = point[0], point[1]
            lat1, long1 = shadow_lat[vertex1], shadow_long[vertex1]
            lat2, long2 = shadow_lat[vertex2], shadow_long[vertex2]
            lat3, long3 = shadow_lat[vertex3], shadow_long[vertex3]
            lat4, long4 = shadow_lat[vertex4], shadow_long[vertex4]
            if latp > lat1+((lat3 - lat1)/(long3 - long1))*long3 and latp > lat2+((lat1 - lat2)/(long1 - long2))*long1 \
            and latp < lat2+((lat4-lat2)/(long4-long2))*long4 and latp < lat4+((lat3-lat4)/(long3-long4))*long3 and \
            longp > long2 and longp < long3:
                good_point_index.append(point.index())

    good_point_index = list(set(good_point_index))
    percent = len(good_point_index)/len(interpolated_path)
