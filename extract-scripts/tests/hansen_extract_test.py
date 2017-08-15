
import sys
import time 
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'extract'))
import test_rasterstats as rs

vector = "./data/srtm_polygons.shp"

vector = "/home/userz/Desktop/shps/NPL/NPL_adm1.shp"
# vector = "/home/userz/Desktop/shps/NPL/NPL_adm2.shp"

raster2 = "/sciclone/aiddata10/REU/data/rasters/external/global/accessibility_map/access_50k.tif"
raster3 = "/sciclone/aiddata10/REU/data/rasters/external/global/hansen/GFC2015/treecover2000/treecover2000.tif"

raster2 = "/home/userz/Desktop/test1_tc00.tif"



# import pandas as pd

# test_extract = rs.zonal_stats(vector, raster, stats='mean', all_touched=False, weights=False, geojson_out=True)

# test_data = [i['properties'] for i in test_extract]

# test_df = pd.DataFrame(test_data)
# test_df.rename(columns = {'mean':'ad_extract'}, inplace=True)
# test_df['ad_extract'].fillna('NA', inplace=True)
# test_df.to_csv("/home/userz/Desktop/test_pd_out.csv", sep=",", encoding="utf-8", index=False)



# print '-----'
# Ts1 = time.time()

# stats1 = rs.zonal_stats(vector, raster, stats='mean', weights=False, all_touched=False)#, geojson_out=True)
# print stats1

# T_run1 = time.time() - Ts1

print '-----'
Ts2 = time.time()

stats2 = rs.zonal_stats(vector, raster2, stats='mean', weights=True, all_touched=True)#, geojson_out=True)
print stats2

T_run2 = time.time() - Ts2

print '-----'
Ts3 = time.time()

stats3 = rs.zonal_stats(vector, raster3, stats='mean', weights=True, all_touched=True)#, geojson_out=True)
print stats3

T_run3 = time.time() - Ts3


# print 'Normal Center: ' + str(T_run1)

print 'Raster2: ' + str(T_run2)

print 'Raster3: ' + str(T_run3)

