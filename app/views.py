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
    locations = places.get_all_locations()
    session['locations'] = jsonpickle.encode(locations)
    if locations:
        print(len(locations))

    if not index or locations is None or session['index'] > len(locations):
        return render_template('index.html')
    return render_template('index.html',
        places=locations[session['index']].name, city=places.get_city())

@app.route('/reset')
def reset():
    session['index'] = 0
    return redirect(url_for('index'))

#@app.route('/submit', methods=['POST'])
#def submit():
#    lat = request.values['lat']
#    lng = request.values['lng']
#    print('New entry (' + str(lat) + ',' + str(lng) + ') was successfully posted')
#    current_place = jsonpickle.decode(session['locations'])[session['index']]
#    distance = places.calculate_distance(current_place,
#                                        Location("", "", {'lat':lat, 'lng':lng}))
#    percentile = scores.add_and_get_percentile(current_place.id, distance)
#
#    result_string = "Under best " + percentile + "%"
#
#    print(result_str)
#
#    session['percentile'] = percentile;
#
#    session['index'] = session['index'] + 1
#    session.modified = True
#    print(session['index'])
#    return render_template("index.html", name=jsonpickle.decode(session['locations'])[session['index']].name,
#                           percentile=result_str)

@app.route('/new', methods=['POST'])
def new_game():
    print("New keywords: " + request.form['keyword'])
    keywords = request.form['keyword']
    city = request.form['city']
    places.new_game(city, keywords)
    locations = places.get_all_locations()
    session['locations'] = jsonpickle.encode(locations)
    session['index'] = 0
    session.modified = True
    return redirect('/')


@app.route('/update', methods=['POST'])
def update():

    while session['index'] < len(jsonpickle.decode(session['locations'])):
        return render_template("index.html", name=jsonpickle.decode(session['locations'])[session['index']].name,
                               percentile='adfijnfsdaf')
    print("you have seen them all - restart?")
    return redirect(url_for('reset'))
