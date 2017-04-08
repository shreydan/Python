"""
I'm Feeling Lucky using Selenium module: pip install selenium. Ignore if installed from requirements.txt
written in Python 3

Uses Firefox webdriver, feel free to change the browser variable with desired driver

"""
from selenium import webdriver

search = input("Enter search:\n>>>")
search = search.replace(" ","+")
url = "https://www.google.com/search?q="+search

browser = webdriver.Firefox()
browser.maximize_window()
browser.get(url)
h3 = browser.find_element_by_class_name("r")
link = h3.find_element_by_tag_name('a')
link.click()
