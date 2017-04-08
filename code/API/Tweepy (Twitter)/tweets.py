"""
This program allows you to tweet directly from terminal.

Prerequisites:
	install tweepy (python module) with "pip install tweepy" Ignore if installed from requirements.txt
	Also, grab your Twitter API from apps.twitter.com
	Get your comsumer key, consumer key secret, access token, access token secret.
	Replace them in initialize() method.

Have fun, this code is all yours.
NEVER SHARE YOUR CONSUMER KEY SECRET AND ACCESS TOKEN SECRET!!!
"""

import tweepy, os

def tweetthis(type):
	if type == "text":
		print ("Enter your tweet "+user.name)
		tweet = input()
		api.update_status(tweet)
	elif type == "pic":
		print ("Enter pic path "+user.name)
		pic = os.path.abspath(input())
		print ("Enter status "+user.name)
		title = input()
		api.update_with_media(pic, status=title)

	print ("\n\nDONE!!")

def initialize():
	global api, auth, user
	ck = "here" # consumer key
	cks = "here" # consumer key SECRET
	at = "here" # access token
	ats = "here" # access token SECRET

	auth = tweepy.OAuthHandler(ck,cks)
	auth.set_access_token(at,ats)

	api = tweepy.API(auth)
	user = api.me()

def main():
	doit = int(input("\n1. text\n2. picture\n"))
	initialize()
	if doit == 1:
		tweetthis("text")
	elif doit == 2:
		tweetthis("pic")
	else:
		print ("OK, Let's try again!")
		main()

main()

# written by shreydan. github.com/shreydan
