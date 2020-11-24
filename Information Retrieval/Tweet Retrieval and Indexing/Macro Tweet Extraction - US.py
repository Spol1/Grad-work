# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 22:03:09 2020

@author: Sudarshan Pol
"""

#IT Generate Max ID
total_tweets = 0
string_list = []
max_id = []

#tweets = api.search(q = " ((Trump2020 OR VOTEBIDEN OR BidenHarris2020 OR senate OR congress OR democrat OR democrats OR conservatives OR conservative OR liberal OR liberals OR potus OR republican OR trump OR fauci OR mcconnel OR pelosi OR Biden) AND (lockdown OR masks OR mask OR corona OR covid OR covid19 OR pandemic OR crisis OR virus OR disease OR socialdistancing OR quarantine OR rally OR CDC OR administration OR admin OR government OR govt)) OR (maskupamerica) -filter:retweets until:2020-09-15 since:2020-09-14 ",result_type = 'recent', count = 1, tweet_mode = "extended")
#tweets = api.search(q = " ((Trump2020 OR VOTEBIDEN OR BidenHarris2020 OR senate OR congress OR democrat OR democrats OR conservatives OR conservative OR liberal OR liberals OR potus OR republican OR trump OR fauci OR mcconnel OR pelosi OR Biden) AND (lockdown OR masks OR mask OR corona OR covid OR covid19 OR pandemic OR crisis OR virus OR disease OR socialdistancing OR quarantine OR rally OR CDC OR administration OR admin OR government OR govt)) OR (maskupamerica) -filter:retweets until:2020-09-16 since:2020-09-15 ",result_type = 'recent', count = 1, tweet_mode = "extended")
#tweets = api.search(q = " ((Trump2020 OR VOTEBIDEN OR BidenHarris2020 OR senate OR congress OR democrat OR democrats OR conservatives OR conservative OR liberal OR liberals OR potus OR republican OR trump OR fauci OR mcconnel OR pelosi OR Biden) AND (lockdown OR masks OR mask OR corona OR covid OR covid19 OR pandemic OR crisis OR virus OR disease OR socialdistancing OR quarantine OR rally OR CDC OR administration OR admin OR government OR govt)) OR (maskupamerica) -filter:retweets until:2020-09-17 since:2020-09-16 ",result_type = 'recent', count = 1, tweet_mode = "extended")
#tweets = api.search(q = " ((Trump2020 OR VOTEBIDEN OR BidenHarris2020 OR senate OR congress OR democrat OR democrats OR conservatives OR conservative OR liberal OR liberals OR potus OR republican OR trump OR fauci OR mcconnel OR pelosi OR Biden) AND (lockdown OR masks OR mask OR corona OR covid OR covid19 OR pandemic OR crisis OR virus OR disease OR socialdistancing OR quarantine OR rally OR CDC OR administration OR admin OR government OR govt)) OR (maskupamerica) -filter:retweets until:2020-09-18 since:2020-09-17 ",result_type = 'recent', count = 1, tweet_mode = "extended")
#tweets = api.search(q = " ((Trump2020 OR VOTEBIDEN OR BidenHarris2020 OR senate OR congress OR democrat OR democrats OR conservatives OR conservative OR liberal OR liberals OR potus OR republican OR trump OR fauci OR mcconnel OR pelosi OR Biden) AND (lockdown OR masks OR mask OR corona OR covid OR covid19 OR pandemic OR crisis OR virus OR disease OR socialdistancing OR quarantine OR rally OR CDC OR administration OR admin OR government OR govt)) OR (maskupamerica) -filter:retweets until:2020-09-19 since:2020-09-18 ",result_type = 'recent', count = 1, tweet_mode = "extended")
tweets = api.search(q = " ((Trump2020 OR VOTEBIDEN OR BidenHarris2020 OR senate OR congress OR democrat OR democrats OR conservatives OR conservative OR liberal OR liberals OR potus OR republican OR trump OR fauci OR mcconnel OR pelosi OR Biden) AND (lockdown OR masks OR mask OR corona OR covid OR covid19 OR pandemic OR crisis OR virus OR disease OR socialdistancing OR quarantine OR rally OR CDC OR administration OR admin OR government OR govt)) OR (maskupamerica) -filter:retweets until:2020-09-20 since:2020-09-19 ",result_type = 'recent', count = 1, tweet_mode = "extended")

trim_tweets = []
trim_tweets = tweets['statuses']
f = open("E:/Class/IR2020/US/tweets_US_18th.json", "a", encoding="utf-8")
for _ in range(len(trim_tweets)):
    copy_poi(trim_tweets,_ )
    mentions(trim_tweets,_ )
    hashtags(trim_tweets,_ )
    tweet_urls(trim_tweets,_ )
    tweet = json.dumps(trim_tweets[_])
    f.write(tweet)       
f.close()

total_tweets = total_tweets + len(trim_tweets)
print(str(total_tweets))
f = open("E:/Class/IR2020/US/Total_US_18.txt", "w", encoding="utf-8")
f.write(str(total_tweets))
f.close()

max_id = trim_tweets[-1]["id"] -1

f = open("E:/Class/IR2020/US/Max_ID.txt", "w", encoding="utf-8")
f.write(str(max_id))
f.close()

#IT Tweet extraction
f = open("E:/Class/IR2020/US/Max_ID.txt", "r")
max_id = int(f.read())
f.close()

for a in range(10):
    
    #tweets = api.search(q = " ((Trump2020 OR VOTEBIDEN OR BidenHarris2020 OR senate OR congress OR democrat OR conservative OR liberal OR liberals OR potus OR republican OR trump OR fauci OR mcconnel OR pelosi OR Biden) AND (lockdown OR masks OR mask OR corona OR covid OR covid19 OR pandemic OR crisis OR virus OR disease OR socialdistancing OR quarantine OR rally OR CDC OR administration OR admin OR government OR govt)) OR (maskupamerica) -filter:retweets until:2020-09-15 since:2020-09-14 ",result_type = 'recent', count = 100, tweet_mode = "extended", max_id=max_id)
    #tweets = api.search(q = " ((Trump2020 OR VOTEBIDEN OR BidenHarris2020 OR senate OR congress OR democrat OR conservative OR liberal OR liberals OR potus OR republican OR trump OR fauci OR mcconnel OR pelosi OR Biden) AND (lockdown OR masks OR mask OR corona OR covid OR covid19 OR pandemic OR crisis OR virus OR disease OR socialdistancing OR quarantine OR rally OR CDC OR administration OR admin OR government OR govt)) OR (maskupamerica) -filter:retweets until:2020-09-16 since:2020-09-15 ",result_type = 'recent', count = 100, tweet_mode = "extended", max_id=max_id)
    #tweets = api.search(q = " ((Trump2020 OR VOTEBIDEN OR BidenHarris2020 OR senate OR congress OR democrat OR conservative OR liberal OR liberals OR potus OR republican OR trump OR fauci OR mcconnel OR pelosi OR Biden) AND (lockdown OR masks OR mask OR corona OR covid OR covid19 OR pandemic OR crisis OR virus OR disease OR socialdistancing OR quarantine OR rally OR CDC OR administration OR admin OR government OR govt)) OR (maskupamerica) -filter:retweets until:2020-09-17 since:2020-09-16 ",result_type = 'recent', count = 100, tweet_mode = "extended", max_id=max_id)
    #tweets = api.search(q = " ((Trump2020 OR VOTEBIDEN OR BidenHarris2020 OR senate OR congress OR democrat OR conservative OR liberal OR liberals OR potus OR republican OR trump OR fauci OR mcconnel OR pelosi OR Biden) AND (lockdown OR masks OR mask OR corona OR covid OR covid19 OR pandemic OR crisis OR virus OR disease OR socialdistancing OR quarantine OR rally OR CDC OR administration OR admin OR government OR govt)) OR (maskupamerica) -filter:retweets until:2020-09-18 since:2020-09-17 ",result_type = 'recent', count = 100, tweet_mode = "extended", max_id=max_id)
    #tweets = api.search(q = " ((Trump2020 OR VOTEBIDEN OR BidenHarris2020 OR senate OR congress OR democrat OR conservative OR liberal OR liberals OR potus OR republican OR trump OR fauci OR mcconnel OR pelosi OR Biden) AND (lockdown OR masks OR mask OR corona OR covid OR covid19 OR pandemic OR crisis OR virus OR disease OR socialdistancing OR quarantine OR rally OR CDC OR administration OR admin OR government OR govt)) OR (maskupamerica) -filter:retweets until:2020-09-19 since:2020-09-18 ",result_type = 'recent', count = 100, tweet_mode = "extended", max_id=max_id)
    tweets = api.search(q = " ((Trump2020 OR VOTEBIDEN OR BidenHarris2020 OR senate OR congress OR democrat OR conservative OR liberal OR liberals OR potus OR republican OR trump OR fauci OR mcconnel OR pelosi OR Biden) AND (lockdown OR masks OR mask OR corona OR covid OR covid19 OR pandemic OR crisis OR virus OR disease OR socialdistancing OR quarantine OR rally OR CDC OR administration OR admin OR government OR govt)) OR (maskupamerica) -filter:retweets until:2020-09-20 since:2020-09-19 ",result_type = 'recent', count = 100, tweet_mode = "extended", max_id=max_id)
    trim_tweets = []
    trim_tweets = tweets['statuses']
    total_tweets = total_tweets + len(trim_tweets)
    
    f = open("E:/Class/IR2020/US/Total_US_18.txt", "w", encoding="utf-8")
    f.write(str(total_tweets))
    print(str(total_tweets))
    f.close()
    
    f = open("E:/Class/IR2020/US/tweets_US_18th.json", "a", encoding="utf-8")
    
    for _ in range(len(trim_tweets)):
        copy_poi(trim_tweets,_ )
        mentions(trim_tweets,_ )
        hashtags(trim_tweets,_ )
        tweet_urls(trim_tweets,_ )
        tweet = json.dumps(trim_tweets[_])
        max_id = trim_tweets[_]["id"] -1
        f.write(tweet)
    
    f.close()
    
f = open("E:/Class/IR2020/US/Max_ID.txt", "w", encoding="utf-8")
f.write(str(max_id))
f.close()

