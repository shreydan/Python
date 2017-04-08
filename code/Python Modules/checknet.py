"""
program to check internet connection
written in: Python 3
written by: Shreyas Daniel github.com/shreydan
"""

import urllib2

try:
	urllib2.urlopen("https://www.google.com")
	print ("Internet is working...")
except urllib2.URLError:
	print ("Internet is not working...")

