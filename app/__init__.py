import os
import sys
import config

from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']
from api import MarkerSubmit
api = Api(app)
api.add_resource(MarkerSubmit, "/verify")

from app import views
