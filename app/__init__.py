import os
import sys
import config

from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']

from app import views
