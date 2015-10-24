import os
import json
from flask import Blueprint, request, render_template, flash, g, session,\
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

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    print('New entry was successfully posted')
    return render_template('index.html')
