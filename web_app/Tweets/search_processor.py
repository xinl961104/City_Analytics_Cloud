import json
import nltk
from cloudant import client, cloudant
from cloudant.client import CouchDB
from cloudant.design_document import DesignDocument
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


#metadata of couchdb server
USERNAME = 'admin'
PASSWORD = 'password'
URL = 'http://172.26.132.199:5984'
DBNAME = 'historic_data'
DBNAME2 = 'processed_data'

#initial connection with couchdb server
client = CouchDB(USERNAME, PASSWORD, url=URL, connect=True)
my_database = client[DBNAME]
my_database2 = client.create_database(DBNAME2)

map_fun = '''function(doc) {
                emit(doc.doc.user.location, doc.doc.text);
        }'''

ddoc_id = 'ddoc001'
view_id = 'location_text'
ddoc = DesignDocument(my_database, 'ddoc001', partitioned = False)
ddoc.add_view(view_id, map_fun)
my_database.create_document(ddoc)
view1 = my_database.get_design_document(ddoc_id).get_view(view_id)

#initialize the sentiment analysis classifier
sid = SentimentIntensityAnalyzer()
with view1.custom_result(group = True) as rslt:
    to_upload = []
    for elem in rslt:
        compound_value =  sid.polarity_scores(elem['doc']['text'])['compound']
        elem['compound'] = compound_value
        to_upload.append(elem)







