import os
import json
from flask import Blueprint, request, redirect, render_template, flash, g, session,\
            url_for
from app import app
from pprint import pprint
import urllib
from app import places

@app.route('/')
def index():
    name, latLng = places.get_random_location()
    print(name)
    session['current_location'] = [name, latLng]
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    lat = request.values['lat']
    lng = request.values['lng']
    print('New entry (' + str(lat) + ',' + str(lng) + ') was successfully posted')
    return render_template("index.html")

