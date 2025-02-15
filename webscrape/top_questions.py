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
#for i in repository[:10]:
    #print(f"Repository : {i.text.strip()}")

repos = soup.select('article.Box-row')
for i in repos[:10]:
    # Extract repository name
    repo_name_tag = i.select_one("h2.h3.lh-condensed a")
    repo_name = repo_name_tag.text.strip() 

    # Extract star count (using updated GitHub selector)
    star_tag = i.select_one("a[href*='/stargazers']")
    star_count = star_tag.text.strip() if star_tag else "No stars"

    # Print results
    print(f"Repository: {repo_name} | Stars: {star_count}") 