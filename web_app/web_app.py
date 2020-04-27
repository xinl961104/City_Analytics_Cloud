#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, flash, redirect, url_for, g
from flaskext.couchdb import CouchDBManager
from query import QueryForm
import simplejson

app = Flask(__name__)
app.config['SECRET_KEY'] = 'NieYanIsTheBest'


@app.route('/home', methods=['GET', 'POST'])
def home():
    form = QueryForm()
    if form.validate_on_submit():
        flash(f'Query submitted!', 'success')
        print(type(form))
        document = [g.couch[form.postcode.data]]
        return render_template('home.html', vegan_map=document,
                        form=form)
    document = [g.couch["002"]]
    return render_template('home.html', vegan_map=document,
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

if __name__ == '__main__':
    app.config.update(
        DEBUG=True,
        COUCHDB_SERVER='http://terry:1234567@localhost:5984/',
        COUCHDB_DATABASE='demo'
    )
    manager = CouchDBManager()
    manager.setup(app)
    app.run(debug = True)
