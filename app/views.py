import os
#import json
from flask import Blueprint, request, redirect, render_template, flash, g, session,\
            url_for

from app import app
from pprint import pprint
import urllib
import jsonpickle
from app import places
from app import scores
from places import Location

@app.route('/')
def index():
    place = places.get_random_location()
    locations = places.get_all_locations()
    session['locations'] = jsonpickle.encode(locations)
    return render_template('index.html', places=locations[session['index']].name)

@app.route('/reset')
def reset():
    session['index'] = 0
    return redirect(url_for('index'))

@app.route('/submit', methods=['POST'])
def submit():
    lat = request.values['lat']
    lng = request.values['lng']
    print('New entry (' + str(lat) + ',' + str(lng) + ') was successfully posted')
    current_place = jsonpickle.decode(session['locations'])[session['index']]
    distance = places.calculate_distance(current_place,
                                        Location("", "", {'lat':lat, 'lng':lng}))

    percentile = scores.add_and_get_percentile(current_place.id, distance)
    result_str = "Under best " + str(percentile) + "%"

    print(result_str)

    session['index'] = session['index'] + 1
    session.modified = True
    print(session['index'])
    return render_template("index.html", name=jsonpickle.decode(session['locations'])[session['index']].name)

@app.route('/update', methods=['POST'])
def update():
    return render_template("index.html", name=jsonpickle.decode(session['locations'])[session['index']].name)
