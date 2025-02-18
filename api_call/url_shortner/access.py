import json
import requests

#Access token: 759718f146fd23a19d7a6a98fbd7c56ae0344d44
url ="https://api-ssl.bitly.com/v4/shorten"
access_token = "759718f146fd23a19d7a6a98fbd7c56ae0344d44"

parameters = {
    "Authorization": f"Bearer {access_token}",  
    "content-type": "application/json"    
}
long_url = "https://notch-clerk-87e.notion.site/MY-LEARNINGS-3c14b18a400849f4a2f885d9ff57360d?pvs=74"
data = {
    "long_url": long_url
}
request = requests.post(url, headers=parameters, data=json.dumps(data))
if request.status_code ==200:
    with open('data.json', 'w') as file:
        json.dump(request.json(), file, indent=2)

    short_url = request.json()["link"]
    print(f"Shortened URL: {short_url}")
else:
    print('Error in API call')