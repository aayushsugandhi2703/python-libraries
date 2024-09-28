import requests

url = 'https://echoedge.top'
r = requests.get(url)
html_content = r.text
print(html_content)

##################################

def get_content(url, path):
    response = requests.get(url)
    with open(path, "w") as f:
        f.write(response.text)

url = 'https://echoedge.top'
path = 'webdata/echo.html'

get_content(url, path)
