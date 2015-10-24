import os
import json
from flask import Blueprint, request, redirect, render_template, flash, g, session,\
            url_for

from app import app
from pprint import pprint
import urllib
from app import places

@app.route('/reset')
def reset():
    session['index'] = 0
    return redirect(url_for('index'))

@app.route('/')
def index():
    name, latLng = places.get_random_location()
    locations = places.get_all_locations()
    session['locations'] = locations
    latLng = session['locations'][session['index']][1]
    return render_template('index.html',
            name=session['locations'][session['index']][0],
            lat = latLng['lat'],
            lng = latLng['lng'])

@app.route('/submit', methods=['POST'])
def submit():
    lat = request.values['lat']
    lng = request.values['lng']
    print('New entry (' + str(lat) + ',' + str(lng) + ') was successfully posted')
    print(places.calculate_distance(session['locations'][session['index']][1], {'lat': float(lat),
        'lng': float(lng)}))

    session['index'] = session['index'] + 1
    session.modified = True
    print(session['index'])
    latLng = session['locations'][session['index']][1]
    return render_template('index.html',
            name=session['locations'][session['index']][0],
            lat = latLng['lat'],
            lng = latLng['lng'])

