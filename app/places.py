import os
import json
#import requests
from googleplaces import GooglePlaces, types, lang
from app import app

google_places = GooglePlaces(api_key)

query_result = google_places.nearby_search(
        location='Karlsruhe, Germany', keyword='Doener',
        radius=20000, types=[types.TYPE_FOOD])

for place in query_result.places:
    print place.name
    print place.geo_location
