"""
Google search using Selenium module: pip install selenium. Ignore if installed from requirements.txt
written in Python 3

Uses Firefox webdriver, feel free to change the browser variable with desired driver

"""

from selenium import webdriver

search = input("Enter your search:\n>>>")
search = search.replace(" ","+")
url = "https://www.google.com/search?q="+search

browser = webdriver.Firefox()
browser.get(url)
