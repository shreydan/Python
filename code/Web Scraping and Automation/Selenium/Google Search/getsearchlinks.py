"""

Get search links using Beautiful Soup and requests libraries to find links from search terms:
Beautiful Soup install: pip install beautifulsoup4
Requests install: pip install requests

"""

import requests
from bs4 import BeautifulSoup
import re

search = input("Enter your search:\n>>> ")
search = search.replace(" ","+")
url = "https://www.google.com/search?q=" + search #format search query

page = requests.get(url)
soup = BeautifulSoup(page.content, features='lxml') #get request and bring content into beautiful soup

links = soup.findAll("a") #Find all <a> tags

print('\n\n')

for link in soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")): #use regex to find links with correct format
    print(re.split(":(?=http)",link["href"].replace("/url?q=",""))[0])
    
