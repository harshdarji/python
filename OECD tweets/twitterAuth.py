import twitter
import json
import sys
import time
import cPickle
from twitter.oauth_dance import oauth_dance

consumer_key = 'ppHAC64cJGBBlwIx9ES4fw'
consumer_secret = 'P6DfN32vTZDkSZfglYryXWStT3xJaOKaRUz8SszHQ'
SCREEN_NAME = 'jcukier'
friends_limit = 100000
(oauth_token, oauth_token_secret) = oauth_dance('jcukier', consumer_key, consumer_secret)
t = twitter.Twitter(domain='api.twitter.com', api_version='1',auth=twitter.oauth.OAuth(oauth_token, oauth_token_secret,consumer_key, consumer_secret))
