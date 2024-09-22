# in this file we have cretaed a soup object and extracted the title of the page
# we have also cretaed a function to get directly result by passisng hte url and path to the function
# we have also extracted the desired tag from the page

import requests
from bs4 import BeautifulSoup

def get_content(url, path):
    response = requests.get(url)
    with open(path, "w") as f:
        f.write(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')

    # gettin the title of the page
    title = soup.title
    print(title.text)

    # gettin the desired tag
    print(soup.h1)

    # searching for a tag or element
    hello = soup.find_all('body')
    print(hello)

url = 'https://echoedge.top'
path = 'webdata/echo2.html'
get_content(url, path)