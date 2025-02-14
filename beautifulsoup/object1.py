from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
url = requests.get("https://thehackernews.com/")
page = urlopen('https://thehackernews.com/')
soup = BeautifulSoup(page, "html.parser")
# to extact the top 10 headlines from hacker news
headdlines = soup.select('.left-box h2')
for i in headdlines [:10]:
    print(i.get_text())
#print(soup.prettify()) # this pretiffy function helps in formating the document
#print(soup.title)
#print(soup.title.string)
#print(soup.a)
#print(soup.find_all('a')) # this will print all the anchor tags

        