# I'm Feeling Lucky - Google

from selenium import webdriver

search = raw_input("Enter search:\n>>>")
search = search.replace(" ","+")
url = "https://www.google.com/search?q="+search

browser = webdriver.Firefox()
browser.maximize_window()
browser.get(url)
h3 = browser.find_element_by_class_name("r")
link = h3.find_element_by_tag_name('a')
link.click()
