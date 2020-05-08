#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, flash, redirect, url_for, g
from flaskext.couchdb import CouchDBManager, ViewDefinition
from query import QueryForm
from cloudant.client import CouchDB
from cloudant.design_document import DesignDocument
import simplejson


USERNAME = 'terry'
PASSWORD = '1234567'
##URL = 'http://172.26.132.199:5984'
URL = 'http://localhost:5984'
DBNAME = 'processed_data'
ddoc_id = 'ddoc001'
view_id = 'mapreduce'

#initial connection with couchdb server
client = CouchDB(USERNAME, PASSWORD, url=URL, connect=True)
my_database = client[DBNAME]
view1 = my_database.get_design_document(ddoc_id).get_view(view_id)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'NieYanIsTheBest'



# some dummy data, will be replaced when couchDB is deployed
vegan_map = [
    {
        'name': 'Carlton',
        'postcode': '3053',
        'veggie_restaurant': [],
        'vegan_number': 150
    },
    {
        'name': 'North Melbourne',
        'postcode': '3051',
        'veggie_restaurant': [],
        'vegan_number': 100
    },
    {
        'name': 'Ardeer',
        'postcode': '3022',
        'veggie_restaurant': [],
        'vegan_number': 30
    },
    {
        'name': 'Footscray and Seddon',
        'postcode': '3011',
        'veggie_restaurant': [],
        'vegan_number': 50
    },
    {
        'name': 'Williamstown',
        'postcode': '3016',
        'veggie_restaurant': [],
        'vegan_number': 75
    }

]


@app.route('/', methods=['GET', 'POST'])


@app.route('/home', methods=['GET', 'POST'])
def home():

    form = QueryForm()
    if form.validate_on_submit():
        flash(f'Query submitted!', 'success')
        print(type(form))
        with view1.custom_result(group = True) as rslt:
            #each elem should contain a key and a value
            #a key should be the region name classified by Statistical Area Level 4
            #value should be the average of sentiment anaysis of that region
            for elem in rslt:
                flash(elem['key'])
                flash(round(elem['value']['sum']/elem['value']['count'], 3))
        ##return render_template('home.html', vegan_map=document,
                               ##form=form)

    return render_template('home.html', vegan_map=vegan_map,
                           form=form)

#@app.route("/test")
#def


@app.route('/chart')
def chart():
    vegan_map = g.couch["002"]
    labels = [r['name'] for r in vegan_map]
    values = [r['vegan_number'] for r in vegan_map]
    return render_template('chart.html', labels=labels
                           , values=values)


app.config.update(
        DEBUG=True,
        COUCHDB_SERVER='http://terry:1234567@localhost:5984/',
        COUCHDB_DATABASE='haha'
    )
manager = CouchDBManager()
manager.setup(app)
if __name__ == '__main__':
    app.run(debug = True)

