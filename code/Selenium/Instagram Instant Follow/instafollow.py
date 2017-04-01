"""
Instagram Instant follow using Selenium module: pip install selenium
written in Python 2.7

Uses Firefox webdriver, feel free to change the browser variable with desired driver
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def done():
	print "Followed all the users"
	time.sleep(2)
	browser.quit()
	
def follow(userlist):
	for users in userlist:
		url = "https://www.instagram.com/"+users
		browser.get(url)
		follow_btn = browser.find_element_by_class_name("_ah57t")
		follow_btn.click()
		print "Followed: "+users
		time.sleep(2)
	
	done()
		

def users():
	time.sleep(3)
	userlist = []
	n = int(raw_input("Enter no. of users to follow "))
	for i in range(0,n):
		follow_user = raw_input("Enter correct username ")
		userlist.append(follow_user)
	follow(userlist)

def login():
	global usr
	usr = raw_input("Enter your username ")
	psw = raw_input("Enter your password ")
	username = browser.find_element_by_name("username")
	username.send_keys(usr)
	password = browser.find_element_by_name("password")
	password.send_keys(psw)
	password.send_keys(Keys.RETURN)

	
browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://www.instagram.com/accounts/login/")
login()
users()




