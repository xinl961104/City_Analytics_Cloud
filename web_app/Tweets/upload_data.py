import json
import time
from cloudant import client, cloudant
from cloudant.client import CouchDB
from cloudant.design_document import DesignDocument

#metadata of couchdb server
##USERNAME = 'admin'
##PASSWORD = 'password'
USERNAME = 'terry'
PASSWORD = '1234567'
##URL = 'http://172.26.132.199:5984'
URL = 'http://localhost:5984'
DBNAME = 'historical_data'


#initial connection with couchdb server
client = CouchDB(USERNAME, PASSWORD, url=URL, connect=True)
my_database = client.create_database(DBNAME)


bulk_docs = []

count = 0
batch_size = 250
with open('../../../historic_data/twitter-melb.json', encoding="utf8") as f:
    next(f)
    start_time = time.time()
    for line in f:
        data = json.loads(line[:-2])
        bulk_docs.append(data)
        if (len(bulk_docs)==batch_size):
            count+=1
            my_database.bulk_docs(bulk_docs)
            time_taken = time.time()-start_time
            percentage = (count*batch_size)/2500000
            print('time elapsed: ', int(time_taken), ' s', 'time remaining: ', int((time_taken/percentage)*(1-percentage)), ' s')
            bulk_docs = []



