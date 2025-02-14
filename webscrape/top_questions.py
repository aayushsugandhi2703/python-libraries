# this is a chatgpt generted problem to find hte top 10 questions from stackoverflow
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

response = requests.get('https://stackoverflow.com/questions/tagged/python')
soup = BeautifulSoup(response.text, 'html.parser')

question = soup.select('h3', class_='s-post-summary--content-title')
for i in question[:10]:
    print(f"Question : {i.text.strip()}")

# extracting top repository and from github find the names, stars

response = requests.get('https://github.com/trending')
soup = BeautifulSoup(response.text, 'html.parser')

repository = soup.select('h2', class_='h3 lh-condensed')
for i in repository[:10]:
    print(f"Repository : {i.text.strip()}")

repo = soup.select('article', class_='Box-row')
for i in repo[:10]:
    question = i.select('h2', class_='h3 lh-condensed')
    stars = i.select('span', class_='d-inline-block float-sm-right')
