# this contain the code for weathr api call
import requests
import os 
import json


API_KEYS = 'f75bb3533a71f3c1e90ef6c58a0c4656'
Location = 'Bangalore, India'
base_url = 'http://api.weatherstack.com/current'

parameters = {
    "access_key": API_KEYS,
    "query": Location
}

response = requests.get(base_url, parameters)

if response.status_code ==200:
    data = response.json()
    with open('weather.json','w') as file:
        json.dump(data,file,indent=2)
else:
    print('Error in API call')
