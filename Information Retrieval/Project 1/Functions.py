# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:59:59 2020

@author: Sudarshan Pol
"""

#Functions
trim_tweets = []
def mentions(trim_tweets,_ ):
    if len(trim_tweets[_]['entities']['user_mentions']) > 0:
        trim_tweets[_]['mentions'] = []
        for n in range(len(trim_tweets[_]['entities']['user_mentions'])):
            mention = trim_tweets[_]['entities']['user_mentions'][n]['screen_name']
            trim_tweets[_]['mentions'].append(mention)
    else :
        trim_tweets[_]['mentions'] = []
    return trim_tweets[_]
            
def hashtags(trim_tweets,_ ):
    if len(trim_tweets[_]['entities']['hashtags']) > 0:
        trim_tweets[_]['hashtags'] = []
        for n in range(len(trim_tweets[_]['entities']['hashtags'])):
            hashtag = trim_tweets[_]['entities']['hashtags'][n]['text']
            trim_tweets[_]['hashtags'].append(hashtag)
    else :
        trim_tweets[_]['hashtags'] = []
    return trim_tweets[_]
                    
def tweet_urls(trim_tweets,_ ):
    if len(trim_tweets[_]['entities']['urls']) > 0:
        trim_tweets[_]['tweet_urls'] = []
        for n in range(len(trim_tweets[_]['entities']['urls'])):
            url = trim_tweets[_]['entities']['urls'][n]['expanded_url']
            trim_tweets[_]['tweet_urls'].append(url)
    else :
        trim_tweets[_]['tweet_urls'] = []
    return trim_tweets[_]

def copy_poi(trim_tweets,_ ):
    
    tweet_time = trim_tweets[_]['created_at']
    new_datetime = datetime.strftime(datetime.strptime(tweet_time,'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:00:00')
    trim_tweets[_]['tweet_date'] = new_datetime
    trim_tweets[_]['poi_id'] = trim_tweets[_]['user']['id']
    trim_tweets[_]['poi_name'] = trim_tweets[_]['user']['screen_name']
    trim_tweets[_]['tweet_text'] = trim_tweets[_]['full_text']
    trim_tweets[_]['tweet_lang'] = trim_tweets[_]['lang']
        
    return trim_tweets[_]
