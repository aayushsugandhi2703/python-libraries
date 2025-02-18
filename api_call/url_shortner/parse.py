import os
import json
import re
from prettytable import PrettyTable

list=[]
#loading json file
with open('data.json', 'r') as file:
    data =json.load(file)
# finding specific details
for i in data:
    created_at = data['created_at']
    id = data['id']
    link = data['link']
    long_url = data['long_url']
    refrences = data['references']
list.append([created_at,id,link,long_url,refrences])
print(list)