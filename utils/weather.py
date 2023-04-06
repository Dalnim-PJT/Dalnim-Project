import requests
import json


def weather_json(city):
    # weather json get
    api = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang=kr&units=metric'
    
    return json.loads(requests.get(api).text)


def pm_json(city):
    # location lat, lon
    location_api = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={apikey}'
    location_api_result = json.loads(requests.get(location_api).text)
    lat = location_api_result[0]['lat']
    lon = location_api_result[0]['lon']

    # pm json get
    api = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={apikey}'

    return json.loads(requests.get(api).text)


with open('etc/openweathermap_apikey.txt') as f:
    apikey = f.read().strip()