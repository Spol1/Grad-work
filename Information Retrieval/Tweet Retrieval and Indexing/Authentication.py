# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:56:59 2020

@author: Sudarshan Pol
"""

import tweepy
import webbrowser
import time
import csv
import json
import pandas as pd
from datetime import datetime
import time

consumer_key = "key"
consumer_secret = "S_key"
callback_uri = 'oob'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
redirect_url = auth.get_authorization_url()
webbrowser.open(redirect_url)
user_pin = input("Pin Value")
auth.get_access_token(user_pin)

api = tweepy.API(auth,  parser=tweepy.parsers.JSONParser())