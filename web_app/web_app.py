#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, redirect, url_for
from query import QueryForm

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
        return redirect(url_for('home'))
    return render_template('home.html', vegan_map=vegan_map,
                           form=form)


@app.route('/chart')
def chart():
    labels = [r['name'] for r in vegan_map]
    values = [r['vegan_number'] for r in vegan_map]
    return render_template('chart.html', labels=labels
                           , values=values)


if __name__ == "__main__":
    app.run(debug=False)
