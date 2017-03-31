from selenium import webdriver

search = raw_input("Enter your search:\n>>>")
search = search.replace(" ","+")
url = "https://www.google.com/search?q="+search

driverFirefox = webdriver.Firefox()
driverFirefox.get(url)
