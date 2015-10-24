import os
import json
#import requests
from googleplaces import GooglePlaces, types, lang
from app import app
from math import sin, cos, sqrt, atan2, radians

google_places = GooglePlaces(app.config['API_KEY'])

def get_location(location, keyword):
    query_result = google_places.nearby_search(
            location=location, keyword=keyword,
            radius=20000)
    return [query_result.places[0].name, query_result.places[0].geo_location]

def calculate_distance(guessed_location, actual_location):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(guessed_location['lat'])
    lon1 = radians(guessed_location['lng'])
    lat2 = radians(actual_location['lat'])
    lon2 = radians(actual_location['lng'])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    print("Result:", distance)

    return distance
