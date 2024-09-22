import requests

url = 'https://echoedge.top'
response = requests.get(url)
html_content = response.text
print(html_content)
