# this showcase hte use of search function
import re

str = "The rain in Spain"
match = re.search(r'\w\w',str)
if match:
    print("found", match.group())  #this group function helps in adding all the found pattern together
else:
    print("No match")