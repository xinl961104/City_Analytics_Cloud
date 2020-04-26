#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask,render_template
from query import QueryForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'NieYanIsTheBest'
# some dummy data
vegan_map = [
    {
        'name' : 'Carlton',
        'postcode' : '3053',
        'veggie_restaurant' : [],
        'vegan_number' : 150
    },
    {
        'name' : 'North Melbourne',
        'postcode' : '3051',
        'veggie_restaurant' : [],
        'vegan_number' : 100
    }
]


@app.route('/')
@app.route('/home')
def home():
    form = QueryForm()
    return render_template('home.html', vegan_map = vegan_map, form = form)