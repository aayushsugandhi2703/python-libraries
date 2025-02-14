from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
url = requests.get("https://www.bbc.com/news")
page = urlopen('https://www.bbc.com/news')
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify()) # this pretiffy function helps in formating the document
print(soup.title)
print(soup.title.string)
print(soup.a)
print(soup.find_all('a')) # this will print all the anchor tags