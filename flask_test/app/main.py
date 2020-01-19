import shadow_calc as sc
from sc.shadowFinder import *
from sc.test_code_cleaned import *
from sc.osm_api import *
from sc.overlap import *

def main(tup_start, tup_end):
    path_coords, directions_result = googleapi(tup_start, tup_end)
    osm = OSMAPI(path_coords)
    osm.run_pointwise_query()
    important_values = osm.get_elements()
    lat0, long0 = important_values[0][0:2]
    shadowlist = shadowFinder(important_values, lat0, long0)
    percent = overlap(shadowlist,path_coords)
    return percent, directions_result
