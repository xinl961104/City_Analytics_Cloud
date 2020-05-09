import shapefile
from shapely.geometry import Point
from shapely.geometry import shape

tweet_loc = Point(144.96558329, -37.81999659)
shp = shapefile.Reader(r'../sa4/SA4_2016_AUST')
print(shp.records()[0])

shape_recs = shp.shapeRecords()



mel_areas = []
for elem in shape_recs:
    if (elem.record[-4] == 'Greater Melbourne') :
        mel_areas.append(elem)
        if tweet_loc.within(shape(elem.shape)):
            print(elem.record[0])





