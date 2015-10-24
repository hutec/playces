import os
#import json
#import requests
from googleplaces import GooglePlaces, types, lang
from app import app
from math import sin, cos, sqrt, atan2, radians
import random

google_places = GooglePlaces(app.config['API_KEY'])
city = "Karlsruhe, Germany"
keywords = "Shopping"
query_results = google_places.nearby_search(
        location=city,
        keyword=keywords,
        radius=20000)

def calculate_distance(guessed_location, actual_location):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(guessed_location.latitude)
    lon1 = radians(guessed_location.longitude)
    lat2 = radians(actual_location.latitude)
    lon2 = radians(actual_location.longitude)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    print("Result:", distance)

    return distance

def get_random_location():
    random_place = random.choice(query_results.places)
    place = Location(random_place.name, random_place.geo_location)
    return place

class Location:
    def __init__(self, name, geo_location):
        self.name = name
        self.longitude = float(geo_location['lng'])
        self.latitude = float(geo_location['lat'])
