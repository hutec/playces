import os
import sys

from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
app.config.from_object('config')

