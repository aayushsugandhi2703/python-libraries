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

import json

# Load JSON log data
with open('logs.json', 'r') as files:
    data = json.load(files)  

# User selects sorting key
sorting_criteria = input("Enter sorting criteria (ip/timestamp): ").strip().lower()

# Dictionary-based switch case alternative
sort_options = {
    "ip": lambda x: x['ip'],
    "timestamp": lambda x: x['timestamp']
}

# Check if valid sorting key was entered
if sorting_criteria in sort_options:
    sorted_data = sorted(data, key=sort_options[sorting_criteria])  
    print(f"Data sorted by {sorting_criteria}:")
    for entry in sorted_data:
        print(entry)
else:
    print("Invalid sorting criteria. Please enter 'ip' or 'timestamp'.")
