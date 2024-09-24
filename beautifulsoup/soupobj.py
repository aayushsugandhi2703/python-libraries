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
    '''
    # gettin the title of the page
    title = soup.title
    print(title.text)

    # gettin the desired tag
    print(soup.h1)

    # searching for a tag or element
    hello = soup.find_all('body')
    print(hello)

    # prettify the html format it
    print(soup.prettify())

    # get the next element of the tag
    next_element = soup.find('h1').find_next()
    print(next_element)

    # get the previous element of the tag
    previous_element = soup.find('h2').find_previous()
    print(previous_element)

    # get the css element of the tag
    selected_elements = soup.select('body')
    print(selected_elements)

    # replace the tag from the html
    dead = soup.find('h2').replace_with(soup.new_tag('p'))
    print(dead)

    # create a new tag and insert it after the desired tag
    new_tag = soup.new_tag('p')
    new_tag.string = "This is a new paragraph"
    print(new_tag)
    soup.find('h2').insert_after(new_tag)
    print(soup.prettify())

    # get the next sibling of the tag
    next_sibling = soup.find('h2').find_next_sibling()
    print(next_sibling)
    '''


url = 'https://echoedge.top'
path = 'webdata/echo2.html'
get_content(url, path)