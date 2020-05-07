from cloudant.client import CouchDB
from cloudant.design_document import DesignDocument
from nltk.sentiment.vader import SentimentIntensityAnalyzer


#metadata of couchdb server
USERNAME = 'terry'
PASSWORD = '1234567'
URL = 'http://localhost:5984'
DBNAME = 'haha'
DBNAME2 = 'processed_data'

#initial connection with couchdb server
client = CouchDB(USERNAME, PASSWORD, url=URL, connect=True)
my_database = client[DBNAME]
my_database2 = client.create_database(DBNAME2)

map_fun = '''function(doc) {
                emit(doc.user.location, doc.text);
        }'''

ddoc_id = 'ddoc001'
view_id = 'location_text'
ddoc = DesignDocument(my_database, 'ddoc001', partitioned = False)
ddoc.add_view(view_id, map_fun)
my_database.create_document(ddoc)
view1 = my_database.get_design_document(ddoc_id).get_view(view_id)

#initialize the sentiment analysis classifier
sid = SentimentIntensityAnalyzer()

to_upload = []
for elem in view1.result:
    print(elem)
    compound_value =  sid.polarity_scores(elem['value'])['compound']
    elem['compound'] = compound_value
    to_upload.append(elem)
    if (len(to_upload) == 10) :
        my_database2.bulk_docs(to_upload)
        to_upload = []