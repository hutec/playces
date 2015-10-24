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
    print(place.name)
    session['place'] = jsonpickle.encode(place)
    return render_template('index.html', place=place)

@app.route('/submit', methods=['POST'])
def submit():
    guessed = Location("Guessed location", request.values)
    print('New entry (' + str(guessed.latitude) + ',' + str(guessed.longitude) + ') was successfully posted')
    print(places.calculate_distance(jsonpickle.decode(session['place']), guessed))
    return render_template("index.html")

