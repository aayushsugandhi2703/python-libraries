import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

page1 = urlopen('https://thehackernews.com/')
soup1 = BeautifulSoup(page1, 'html.parser')

page2 = urlopen('https://thehackernews.com/search/label/Cyber%20Attack')
soup2 = BeautifulSoup(page2, 'html.parser')

# extracting the top 10 headlines from the hacker news

headlines =  soup1.select('h2')
for i in headlines[:10]:
    print(f"News : {i.get_text()}")

# extracting top 10 recent cyber attacks news

headlines =  soup2.select('h2')
for i in headlines[:10]:
    print(f"Attacks : {i.get_text()}")

