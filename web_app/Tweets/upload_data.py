import json
import time
from cloudant import client, cloudant
from cloudant.client import CouchDB
from cloudant.design_document import DesignDocument

#metadata of couchdb server
USERNAME = 'admin'
PASSWORD = 'password'
URL = 'http://172.26.132.199:5984'
DBNAME = 'historical_data'


#initial connection with couchdb server
client = CouchDB(USERNAME, PASSWORD, url=URL, connect=True)
my_database = client.create_database(DBNAME)


bulk_docs = []

count = 0
with open('../../../historic_data/twitter-melb.json', encoding="utf8") as f:
    next(f)
    start_time = time.time()
    for line in f:
        data = json.loads(line[:-2])
        bulk_docs.append(data)
        if (len(bulk_docs)==20):
            count+=1
            my_database.bulk_docs(bulk_docs)
            time_taken = time.time()-start_time
            percentage = (count*20)/154405640
            print('time elapsed: ', int(time_taken), ' s', 'time remaining: ', int((time_taken/percentage)*(1-percentage)), ' s')
            bulk_docs = []



