#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys

total = 0.0
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'abcdefg...'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'abcdefg...'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = 'abcdefg...'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'abcdefg...'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
while(1==1):
    total += 0.05;
    api.update_status("#BellLetsTalk : This bot has raised $"+str(total))
    time.sleep(30)#Tweet every 30 seconds