#!/usr/bin/env python3
import requests
import json
import sys

#area(32.227754,-110.959464,32.236005,-110.944097);

overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
[out:json];
area[name="Tucson"];
(node["building"="yes"](area);
 way["building"="yes"](area);
 rel["building"="yes"](area);
);
out center;
"""
response = requests.get(overpass_url,
                        params={'data': overpass_query})
data = response.json()

overpass_query2 = """
[out:json];
(rel["name"="Tucson"];way(r);node(w);
);
out center;
"""
response2 = requests.get(overpass_url,
                        params={'data': overpass_query2})
data2 = response2.json()

# print(data,data2)
print(data)

## From https://towardsdatascience.com/loading-data-from-openstreetmap-with-python-and-the-overpass-api-513882a27fd0

# sys.exit()

import numpy as np
import matplotlib.pyplot as plt
import math

# Collect coords into list
coords = []
coords2 = []
for element in data['elements']:
  if element['type'] == 'node':
    lon = element['lon']
    lat = element['lat']
    coords.append((lon, lat))
  elif 'center' in element:
    lon = element['center']['lon']
    lat = element['center']['lat']
    coords.append((lon, lat))# Convert coordinates into numpy array
X = np.array(coords)

for element in data2['elements']:
    if element['type'] == 'node':
        lon = element['lon']
        lat = element['lat']
        coords2.append((lon, lat))
y = np.array(coords2)

# y = list(y)
# ordered_y, first = [], True
# for point in y:
#     if first:
#         point1 = y.pop(0)
#         ordered_y.append(point1)
#         first = False
#     else:
#         min_r = 999
#         mindex = 0
#         for point2 in y:
#             r = math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)
#             if r < min_r:
#                 min_r = r
#                 mindex = y.index(point2)
#         point1 = y.pop(mindex)
#         ordered_y.append(point1)
# ordered_y = np.array(ordered_y)
# y = np.array(y)

plt.plot(X[:, 0], X[:, 1], 'o')
# plt.plot(ordered_y[:,0], ordered_y[:,1], '-')
plt.plot(y[:,0], y[:,1], '.')
plt.title('Parking in Tucson')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.axis('equal')
plt.show()
