import couchdb
import json
import os
from pathlib import Path


#CouchDB authentication
COUCHDB_SERVER='http://admin:password@172.26.132.199:5984/'
DBNAME = 'haha'
couch = couchdb.Server(COUCHDB_SERVER)
db = couch[DBNAME]



with open('../result_tweets.json') as f:
    count = 0
    for line in f:
        data = json.loads(line)
        db.save(data)
        if count ==0:
            print(data)
        count += 1

