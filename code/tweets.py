"""
This program allows you to tweet directly from terminal.

Prerequisites: 
	install tweepy (python module) with "pip install tweepy"
	Also, grab your Twitter API from apps.twitter.com
	Get your comsumer key, consumer key secret, access token, access token secret.
	Replace them in initialize() method.

Have fun, this code is all yours.
NEVER SHARE YOUR CONSUMER KEY SECRET AND ACCESS TOKEN SECRET!!!
"""
import tweepy

def tweeter(tweet):
	api.update_status(tweet)
	print "\n\nDONE!!"
	
def tweetthis():
	print "Enter your tweet "+user.name
	tweet = raw_input()
	tweeter(tweet)

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
	doit = raw_input("Wanna tweet? [y/n]")
	doit = doit.lower()
	if doit == 'y':
		initialize()
		tweetthis()
	else:
		print "OK!"
		
main()

# written by shreydan. github.com/shreydan
