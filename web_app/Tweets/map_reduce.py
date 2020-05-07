import json

from cloudant import client, cloudant
from cloudant.client import CouchDB
from cloudant.design_document import DesignDocument

#metadata of couchdb server
USERNAME = 'terry'
PASSWORD = '1234567'
URL = 'http://127.0.0.1:5984'
DBNAME = 'haha'

#initial connection with couchdb server
client = CouchDB(USERNAME, PASSWORD, url=URL, connect=True)

#maping function and reduce function-> can be modified
map_fun = '''function(doc) {
                emit(doc.user.location, 1);
        }'''
reduce_fun = '_count'

#specify which database you want to access, returns all the document within the database
my_database = client[DBNAME]


#creating a example using the mapping function and reduce function, adding it to the database
viewName = 'mapreduce'
ddoc = DesignDocument(my_database, 'ddoc001', partitioned = False)
ddoc.add_view('mapreduce', map_fun, reduce_fun)
my_database.create_document(ddoc)

#how to access created view with reducing functions to group results to a group
ddoc_id = 'ddoc001'
view_id = 'mapreduce'
my_database2 = client.get(DBNAME, remote = True)
view1 = my_database2.get_design_document(ddoc_id).get_view(view_id)
with view1.custom_result(group = True) as rslt:
    for elem in rslt:
        print(elem)


#example of how to access view created from web
#http://127.0.0.1:5984/haha/_design/ddoc001/_view/mapreduce?group=true

