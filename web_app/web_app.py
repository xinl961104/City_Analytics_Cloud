#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask,render_template, flash, redirect, url_for
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


@app.route('/', methods= ['GET', 'POST'])
@app.route('/home', methods= ['GET', 'POST'])
def home():
    form = QueryForm()
    if form.validate_on_submit():
        flash(f'Query submitted!', 'success')
        return redirect(url_for('home'))
    return render_template('home.html', vegan_map = vegan_map, 
    form = form)