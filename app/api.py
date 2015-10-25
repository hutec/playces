from flask_restful import Resource, Api
from flask import request, session, render_template
from places import Location
import places
import jsonpickle
import scores

class MarkerSubmit(Resource):
    def put(self):
#       print("Got called")
        latLng = {'lat': request.form['lat'], 'lng': request.form['lng']}
        guessed = Location("Guessed location", None, latLng)
        current_place = jsonpickle.decode(session['locations'])[session['index']]
        distance = places.calculate_distance(current_place, guessed)
        goal = jsonpickle.decode(session['locations'])[session['index']]
        session['index'] = session['index'] + 1
        session.modified = True
                                             
        percentile = scores.add_and_get_percentile(current_place.id, distance)
        result_string = "Better than " + str(100 - percentile) + "%"

        return {
            'distance': distance,
            'lat': goal.latitude,
            'lng': goal.longitude,
            'percentile': result_string
        }

    def get(self):
        return "Test"
