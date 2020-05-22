import json
import time
from cloudant import client, cloudant
from cloudant.client import CouchDB
from cloudant.design_document import DesignDocument
from db_constants import *
from db_utils import *

# DBNAME = 'historical_data'
# #initial connection with couchdb server
#
# my_database = connect_database(USERNAME, PASSWORD,URL, DBNAME)
#
# bulk_docs = []
# count = 0
# batch_size = 250
# with open('../../../historic_data/twitter-melb.json', encoding="utf8") as f:
#     next(f)
#     start_time = time.time()
#     for line in f:
#         data = json.loads(line[:-2])['doc']
#         del data['_rev']
#         data['_id'] =  data['id_str']
#         bulk_docs.append(data)
#         if (len(bulk_docs)==batch_size):
#             count+=1
#             my_database.bulk_docs(bulk_docs)
#             time_taken = time.time()-start_time
#             percentage = (count*batch_size)/2500000
#             print('time elapsed: ', int(time_taken), ' s', 'time remaining: ', int((time_taken/percentage)*(1-percentage)), ' s')
#             bulk_docs = []

DBNAME = 'historical_data'

#initial connection with couchdb server
my_database = connect_database(USERNAME, PASSWORD,URL, DBNAME)
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

