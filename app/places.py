import os
import json
#import requests
from googleplaces import GooglePlaces, types, lang
from app import app
import random

google_places = GooglePlaces(app.config['API_KEY'])
city = "Karlsruhe, Germany"
keywords = "Shopping"
query_results = google_places.nearby_search(
        location=city, 
        keyword=keywords,
        radius=20000)

def get_random_location():
    random_place = random.choice(query_results.places)
    return [random_place.name, random_place.geo_location]
