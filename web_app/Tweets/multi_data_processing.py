from db_constants import *
from db_utils import *
from cloudant import client, cloudant
from cloudant.client import CouchDB
from cloudant.design_document import DesignDocument
#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import shapefile
from shapely.geometry import Point
from shapely.geometry import shape
from multiprocessing import Pool, cpu_count
import time

DBNAME = 'historical_data'
DBNAME2 = 'processed_data'

#initial connection with couchdb server
my_database = connect_database(USERNAME, PASSWORD,URL, DBNAME)
my_database2 = create_database(USERNAME, PASSWORD,URL, DBNAME2)

map_fun = '''function(doc) {
            if (/( art )|(music)|(film)/.test(doc.text.toLowerCase())){
                emit(doc.coordinates.coordinates, doc.text);
            }
        }'''

ddoc_id = 'ddoc001'
view_id = 'vegan_location_text'

ddoc = DesignDocument(my_database, ddoc_id, partitioned = False)
ddoc.add_view(view_id, map_fun)
my_database.create_document(ddoc)
view1 = my_database.get_design_document(ddoc_id).get_view(view_id)

#open statistical areas 4 shapes and records to classify tweets location in to regions
shp = shapefile.Reader(r'../sa4/SA4_2016_AUST')
shape_recs = shp.shapeRecords()
mel_areas = []
for shape_record in shape_recs:
    if (shape_record.record[-4] == 'Greater Melbourne') :
        mel_areas.append(shape_record)


sid = SentimentIntensityAnalyzer()
batch_size = 250

def process_data(row):
    for area in mel_areas:
        if Point(row['key']).within(shape(area.shape)):
            region_code = area.record[0]
            region_name = area.record[1]
            compound_value =  sid.polarity_scores(row['value'])['compound']
            #row['tweet_id'] = row['key'][1]
            row['_id'] = row['id']
            row['compound'] = compound_value
            row['region_name'] = region_name
            row['region_code'] = region_code
            return row

time1 = time.time()

if __name__ == '__main__':
    with view1.custom_result() as rslt:
        pool = Pool(cpu_count())
        results = pool.map(process_data, rslt)
        results = [i for i in results if i is not None]
        print(time.time() - time1)
        my_database2.bulk_docs(results)








