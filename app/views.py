import os
import json
from flask import Blueprint, request, render_template, flash, g, session,\
            url_for
from app import app
from pprint import pprint
import urllib

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    print('New entry was successfully posted')
    return render_template('index.html')

