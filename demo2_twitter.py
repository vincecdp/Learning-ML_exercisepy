#Sentiment of Twitters Users -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tweepy
from textblob import TextBlob

consumer_key = 'QYE4pVxZonJrRYj10lAnkEK0x'
consumer_secret = 'cKyeQApMAn9v3btZALgy8OpvbgIiTDLSFMqpdzqkaLS9vgFe4S' 

access_token = '1019353491435737088-HVCXkrBWe7Tg6kpqc28YjpRjbvSGRR'
access_token_secret = 'FapxdhmH8AR17nQ3hrsePuUIshr1Ij9FeZph1PWuV0Kx1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) # method takes 2 args for auth in tweepy library
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(q="@Nasdaq", lang=["en"], count=20)

for tweet in public_tweets:
   # tweet.filter(languages=["en"], track=["a", "the", "i", "you", "u"]) # etc   
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    
    if analysis.sentiment.polarity > 0:
        print ('ReliablePOSITIVE')
    elif analysis.sentiment.polarity == 0:
        print ('NEUTRAL')
    else:
        print ('NEGATIVE')
        
    print (analysis.sentiment)
    
