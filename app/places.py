import os
import json
#import requests
from googleplaces import GooglePlaces, types, lang
from app import app
from math import sin, cos, sqrt, atan2, radians
import random

def my_key(place):
    if "reviews" in place.details:
        return len(place.details["reviews"])
    else:
        return 0

google_places = GooglePlaces(app.config['API_KEY'])
city = "Karlsruhe, Germany"
keywords = "Restaurants"
query_results = google_places.nearby_search(
        location=city, 
        keyword=keywords,
        radius=5000)

# has to be called in order for the details to be fetched
for p in query_results.places:
    p.get_details()

# sorted by number of reviews in descending order
sorted_results = sorted(query_results.places, key=my_key, reverse=True)


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

def get_random_location():
    random_place = random.choice(sorted_results)
    return [random_place.name, random_place.geo_location]

def get_all_locations():
    return [[place.name, place.geo_location] 
            for place in query_results.places]
