import os
import json
from prettytable import PrettyTable

with open ('weather.json' ,'r') as file:
    info = json.load(file)

city = info['request']['query']   
temperature = info['current']['temperature']
wind_speed = info['current']['wind_speed']
humidity = info['current']['humidity']
uv_index = info['current']['uv_index']
table = PrettyTable(['city','temperature','wind_speed','humidity','uv_index'])
table.add_row([city,temperature,wind_speed,humidity,uv_index])
print(table)