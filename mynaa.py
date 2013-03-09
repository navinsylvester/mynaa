#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import tweepy

CONSUMER_KEY = 'HrqHfSAcdnN91NG5sAiksA'
CONSUMER_SECRET = 'TloIAOTXwJxD93UDD6bWcfDiWAdRtGXM0G2ahRleu0'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url()

print '\n'
print 'Copy and paste the beside url in browser to get pin: ' + auth_url
verifier = raw_input('Enter acquired PIN to proceed: ').strip()
print '\n'

auth.get_access_token(verifier)

print "ACCESS_KEY = '%s'" % auth.access_token.key
print "ACCESS_SECRET = '%s'" % auth.access_token.secret
print '\n'

ACCESS_KEY = auth.access_token.key
ACCESS_SECRET = auth.access_token.secret

auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

def tweet_the_blog(blog_entry, tweet_width=129):
    tweets = []

    for sentence in blog_entry.split('\n'):
        line = []
        len_line = 0

        for word in sentence.split(' '):
            len_word = len(word)

            if len_line + len_word <= tweet_width:
                line.append(word)
                len_line += len_word + 1
            else:
                tweets.append(' '.join(line))
                line = [word]
                len_line = len_word + 1

        tweets.append(' '.join(line))

    return tweets

if len(sys.argv) == 2:
    chirps = tweet_the_blog(sys.argv[1])
    
    tweet_len = len(chirps)
    current_tweet_len = tweet_len
    
    arrow = u"▼"
    arrow = arrow.encode('utf8')
    
    for chirp in reversed(chirps):
        if current_tweet_len != tweet_len:
            part = arrow + " [%s/%s]" % (current_tweet_len, tweet_len)
        else:
            part = " [%s/%s]" % (current_tweet_len, tweet_len)
        chirp = chirp+part
    
        api.update_status(chirp)
    
        print "Tweet: ", chirp
    
        current_tweet_len -= 1
else:
    print "Usage: ./mynaa.py 'Your tweet text'"
