import json
import requests

url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

query_params = {
    'format': 'geojson',
    'starttime': '2020-10-01',
    'endtime': '2020-10-30',
    'minlatitude': 8.0,
    'minlongitude': 37.0,
    'maxlatitude': 68.0,
    'maxlongitude': 97.0  
}

response = requests.get(url, params=query_params)
data = response.json()

with open("earthquake.json", "w") as f:
    json.dump(data, f, indent= 4)