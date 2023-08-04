
import json
import requests
from collections import defaultdict
import pandas as pd
import os


def get_df_from_foursquare(query, latitude, longitude, radis="500", sort = "DISTANCE"):
    foursquare_key = os.environ["FOURSQUARE_API_KEY"]
    headers = {
    "Accept": "application/json",
    "Authorization": os.environ["FOURSQUARE_API_KEY"]
    }
    url = "https://api.foursquare.com/v3/places/search"

    params = {
        "query": query,
        "ll": latitude + "," + longitude,
        "radius":radis,
        "open_now": "false",
        "sort":"DISTANCE"
    }
    response = requests.request("GET", url, params=params, headers=headers)
    data = response.json()
    resturant_list = data['results']
    
    resturant_dict = defaultdict(list)
    for resturant in resturant_list:
        name = resturant['name']
        latitude = resturant['geocodes']['main']['latitude']
        longitude = resturant['geocodes']['main']['longitude']
        address = resturant['location']['address']
        resturant_dict['name'].append(name)
        resturant_dict['foursquare_latitude'].append(latitude)
        resturant_dict['foursquare_longitude'].append(longitude)
        resturant_dict['foursquare_address'].append(address)

    foursquare_df = pd.DataFrame.from_dict(resturant_dict)
    
    return foursquare_df


def get_df_from_yelp(query, latitude, longitude, radis="500", sort = "distance"):
    url = "https://api.yelp.com/v3/businesses/search"

    yelp_key = os.environ['YELP_KEY']
    headers = {
    "Accept": "application/json",
    'Authorization': f'Bearer {yelp_key}'
    }

    params = {
        "term": query,
        "latitude": latitude,
        "longitude": longitude,
        "radius":radis,
        "open_now": "false",
        "sort_by":"distance"
    }
    response = requests.request("GET", url, params=params, headers=headers)
    data = response.json()
    resturant_list = data['businesses']
    
    resturant_dict = defaultdict(list)
    for resturant in resturant_list:
        name = resturant['name']
        latitude = resturant['coordinates']['latitude']
        longitude = resturant['coordinates']['longitude']
        address = str(resturant['location']['address1']) + str(resturant['location']['address2']) + str(resturant['location']['address3'])
        resturant_dict['name'].append(name)
        resturant_dict['yelp_latitude'].append(latitude)
        resturant_dict['yelp_longitude'].append(longitude)
        resturant_dict['yelp_address'].append(address)

    yelp_df = pd.DataFrame.from_dict(resturant_dict)
    return yelp_df

