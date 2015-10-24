from flask_restful import Resource, Api
from flask import request, session, render_template
from places import Location
import places
import jsonpickle

class MarkerSubmit(Resource):
    def put(self):
#       print("Got called")
        latLng = {'lat': request.form['lat'], 'lng': request.form['lng']}
        guessed = Location("Guessed location", None, latLng)
        distance = places.calculate_distance(jsonpickle.decode(session['locations'])[session['index']], guessed)
        goal = jsonpickle.decode(session['locations'])[session['index']]
        session['index'] = session['index'] + 1
        session.modified = True

        return {
            'distance': distance,
            'lat': goal.latitude,
            'lng': goal.longitude
        }

    def get(self):
        return "Test"
