import os
#import json
from flask import Blueprint, request, redirect, render_template, flash, g, session,\
            url_for

from app import app
from pprint import pprint
import urllib
import jsonpickle
from app import places
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
    guessed = Location("Guessed location", request.values)
    print('New entry (' + str(guessed.latitude) + ',' + str(guessed.longitude) + ') was successfully posted')
    print(places.calculate_distance(jsonpickle.decode(session['locations'])[session['index']], guessed))
    session['index'] = session['index'] + 1
    session.modified = True
    print(session['index'])
    return render_template("index.html", name=jsonpickle.decode(session['locations'])[session['index']].name)

