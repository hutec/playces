import os
import json
#import requests
from googleplaces import GooglePlaces, types, lang
from app import app

google_places = GooglePlaces(app.config['API_KEY'])

def get_location(location, keyword):
    query_result = google_places.nearby_search(
            location=location, keyword=keyword,
            radius=20000)
    return [query_result.places[0].name, query_result.places[0].geo_location]

