import json
import pandas as pd
file_path = "Documents/GitHub/Statistical-Modelling-Project/data/sobi-hamilton.json"

def convert_json_into_df(file_path):
    
    with open(file_path, 'r') as f:
        raw_data = json.load(f)
        
    station_name = raw_data['network']['stations']['name']
    latitude = raw_data['network']['stations']['latitude']
    longitude = raw_data['network']['stations']['longitude']
    number_of_bikes = raw_data['network']['stations']['free_bikes']

    pre_data = {
        'station_name' :station_name,
        'latitude' :latitude,
        'longitude' :longitude,
        'number_of_bikes' :number_of_bikes
    }
    raw_df = pd.DataFrame(pre_data)
    return raw_df
    
