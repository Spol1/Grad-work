# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 22:03:09 2020

@author: Sudarshan Pol
"""

#IT Generate Max ID
total_tweets = 0
string_list = []
max_id = []
tweets = api.search(q = "((governo OR conte OR ministro OR Comuni OR (Consiglio dei Ministri) OR italiano OR Italia) AND (covid OR covid19 OR corona OR pandemia OR vaccini OR Sanitario OR sacrifico OR antigenico OR scuole OR sicurezza OR virus)) OR (Consiglio dei Ministri) OR (ordinanza) OR (vaccini) OR (confinamento) OR (Servizio Sanitario Nazionale)-filter:retweets until:2020-09-13 since:2020-09-12 ", result_type = 'recent', count = 1, tweet_mode = "extended" )
#tweets = api.search(q = "((governo OR conte OR ministro OR Comuni OR (Consiglio dei Ministri) OR italiano OR Italia) AND (covid OR covid19 OR corona OR pandemia OR vaccini OR Sanitario OR sacrifico OR antigenico OR scuole OR sicurezza OR virus)) OR (Consiglio dei Ministri) OR (ordinanza) OR (vaccini) OR (confinamento) OR (Servizio Sanitario Nazionale)-filter:retweets until:2020-09-14 since:2020-09-13 ", result_type = 'recent', count = 1, tweet_mode = "extended" )

#tweets = api.search(q = "((governo OR conte OR ministro OR Comuni OR (Consiglio dei Ministri) OR italiano OR Italia) AND (covid OR covid19 OR corona OR pandemia OR vaccini OR Sanitario OR sacrifico OR antigenico OR scuole OR sicurezza OR virus)) OR (Consiglio dei Ministri) OR (ordinanza) OR (vaccini) OR (confinamento) OR (Servizio Sanitario Nazionale)-filter:retweets until:2020-09-15 since:2020-09-14 ", result_type = 'recent', count = 1, tweet_mode = "extended" )
#tweets = api.search(q = "((governo OR conte OR ministro OR Comuni OR (Consiglio dei Ministri) OR italiano OR Italia) AND (covid OR covid19 OR corona OR pandemia OR vaccini OR Sanitario OR sacrifico OR antigenico OR scuole OR sicurezza OR virus)) OR (Consiglio dei Ministri) OR (ordinanza) OR (vaccini) OR (confinamento) OR (Servizio Sanitario Nazionale)-filter:retweets until:2020-09-16 since:2020-09-15 ", result_type = 'recent', count = 1, tweet_mode = "extended" )
#tweets = api.search(q = "((governo OR conte OR ministro OR Comuni OR (Consiglio dei Ministri) OR italiano OR Italia) AND (covid OR covid19 OR corona OR pandemia OR vaccini OR Sanitario OR sacrifico OR antigenico OR scuole OR sicurezza OR virus)) OR (Consiglio dei Ministri) OR (ordinanza) OR (vaccini) OR (confinamento) OR (Servizio Sanitario Nazionale)-filter:retweets until:2020-09-17 since:2020-09-16 ", result_type = 'recent', count = 1, tweet_mode = "extended" )
#tweets = api.search(q = "((governo OR conte OR ministro OR Comuni OR (Consiglio dei Ministri) OR italiano OR Italia) AND (covid OR covid19 OR corona OR pandemia OR vaccini OR Sanitario OR sacrifico OR antigenico OR scuole OR sicurezza OR virus)) OR (Consiglio dei Ministri) OR (ordinanza) OR (vaccini) OR (confinamento) OR (Servizio Sanitario Nazionale)-filter:retweets until:2020-09-18 since:2020-09-17 ", result_type = 'recent', count = 1, tweet_mode = "extended" )
#tweets = api.search(q = "((governo OR conte OR ministro OR Comuni OR (Consiglio dei Ministri) OR italiano OR Italia) AND (covid OR covid19 OR corona OR pandemia OR vaccini OR Sanitario OR sacrifico OR antigenico OR scuole OR sicurezza OR virus)) OR (Consiglio dei Ministri) OR (ordinanza) OR (vaccini) OR (confinamento) OR (Servizio Sanitario Nazionale)-filter:retweets until:2020-09-19 since:2020-09-18 ", result_type = 'recent', count = 1, tweet_mode = "extended" )
tweets = api.search(q = "((governo OR conte OR ministro OR Comuni OR (Consiglio dei Ministri) OR italiano OR Italia) AND (covid OR covid19 OR corona OR pandemia OR vaccini OR Sanitario OR sacrifico OR antigenico OR scuole OR sicurezza OR virus)) OR (Consiglio dei Ministri) OR (ordinanza) OR (vaccini) OR (confinamento) OR (Servizio Sanitario Nazionale)-filter:retweets until:2020-09-20 since:2020-09-19 ", result_type = 'recent', count = 1, tweet_mode = "extended" )

trim_tweets = []
trim_tweets = tweets['statuses']
f = open("E:/Class/IR2020/IT/tweets_IT_18th.json", "a", encoding="utf-8")
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
f = open("E:/Class/IR2020/IT/Total_IT_18.txt", "w", encoding="utf-8")
f.write(str(total_tweets))
f.close()

max_id = trim_tweets[-1]["id"] -1

f = open("E:/Class/IR2020/IT/Max_ID.txt", "w", encoding="utf-8")
f.write(str(max_id))
f.close()

#IT Tweet extraction
f = open("E:/Class/IR2020/IT/Max_ID.txt", "r")
max_id = int(f.read())
f.close()

for a in range(10):
    tweets = api.search(q = "((governo OR conte OR ministro OR Comuni OR (Consiglio dei Ministri) OR italiano OR Italia) AND (covid OR covid19 OR corona OR pandemia OR vaccini OR Sanitario OR sacrifico OR antigenico OR scuole OR sicurezza OR virus)) OR (Consiglio dei Ministri) OR (ordinanza) OR (vaccini) OR (confinamento) OR (Servizio Sanitario Nazionale) -filter:retweets until:2020-09-20 since:2020-09-19", count = 100, tweet_mode = "extended", max_id = max_id)
    #tweets = api.search(q = "((governo OR conte OR ministro OR Comuni OR (Consiglio dei Ministri) OR italiano OR Italia) AND (covid OR covid19 OR corona OR pandemia OR vaccini OR Sanitario OR sacrifico OR antigenico OR scuole OR sicurezza OR virus)) OR (Consiglio dei Ministri) OR (ordinanza) OR (vaccini) OR (confinamento) OR (Servizio Sanitario Nazionale) -filter:retweets until:2020-09-14 since:2020-09-13", count = 100, tweet_mode = "extended", max_id = max_id)
    
    #tweets = api.search(q = "((governo OR conte OR ministro OR Comuni OR (Consiglio dei Ministri) OR italiano OR Italia) AND (covid OR covid19 OR corona OR pandemia OR vaccini OR Sanitario OR sacrifico OR antigenico OR scuole OR sicurezza OR virus)) OR (Consiglio dei Ministri) OR (ordinanza) OR (vaccini) OR (confinamento) OR (Servizio Sanitario Nazionale) -filter:retweets until:2020-09-15 since:2020-09-14", count = 100, tweet_mode = "extended", max_id = max_id)
    #tweets = api.search(q = "((governo OR conte OR ministro OR Comuni OR (Consiglio dei Ministri) OR italiano OR Italia) AND (covid OR covid19 OR corona OR pandemia OR vaccini OR Sanitario OR sacrifico OR antigenico OR scuole OR sicurezza OR virus)) OR (Consiglio dei Ministri) OR (ordinanza) OR (vaccini) OR (confinamento) OR (Servizio Sanitario Nazionale) -filter:retweets until:2020-09-16 since:2020-09-15", count = 100, tweet_mode = "extended", max_id = max_id)
    #tweets = api.search(q = "((governo OR conte OR ministro OR Comuni OR (Consiglio dei Ministri) OR italiano OR Italia) AND (covid OR covid19 OR corona OR pandemia OR vaccini OR Sanitario OR sacrifico OR antigenico OR scuole OR sicurezza OR virus)) OR (Consiglio dei Ministri) OR (ordinanza) OR (vaccini) OR (confinamento) OR (Servizio Sanitario Nazionale) -filter:retweets until:2020-09-17 since:2020-09-16", count = 100, tweet_mode = "extended", max_id = max_id)
    #tweets = api.search(q = "((governo OR conte OR ministro OR Comuni OR (Consiglio dei Ministri) OR italiano OR Italia) AND (covid OR covid19 OR corona OR pandemia OR vaccini OR Sanitario OR sacrifico OR antigenico OR scuole OR sicurezza OR virus)) OR (Consiglio dei Ministri) OR (ordinanza) OR (vaccini) OR (confinamento) OR (Servizio Sanitario Nazionale) -filter:retweets until:2020-09-18 since:2020-09-17", count = 100, tweet_mode = "extended", max_id = max_id)
    #tweets = api.search(q = "((governo OR conte OR ministro OR Comuni OR (Consiglio dei Ministri) OR italiano OR Italia) AND (covid OR covid19 OR corona OR pandemia OR vaccini OR Sanitario OR sacrifico OR antigenico OR scuole OR sicurezza OR virus)) OR (Consiglio dei Ministri) OR (ordinanza) OR (vaccini) OR (confinamento) OR (Servizio Sanitario Nazionale) -filter:retweets until:2020-09-19 since:2020-09-18", count = 100, tweet_mode = "extended", max_id = max_id)
    
    trim_tweets = []
    trim_tweets = tweets['statuses']
    total_tweets = total_tweets + len(trim_tweets)
    
    f = open("E:/Class/IR2020/IT/Total_IT_18.txt", "w", encoding="utf-8")
    f.write(str(total_tweets))
    print(str(total_tweets))
    f.close()
    
    f = open("E:/Class/IR2020/IT/tweets_IT_18th.json", "a", encoding="utf-8")
    
    for _ in range(len(trim_tweets)):
        copy_poi(trim_tweets,_ )
        mentions(trim_tweets,_ )
        hashtags(trim_tweets,_ )
        tweet_urls(trim_tweets,_ )
        tweet = json.dumps(trim_tweets[_])
        max_id = trim_tweets[_]["id"] -1
        f.write(tweet)
    
    f.close()
    
f = open("E:/Class/IR2020/IT/Max_ID.txt", "w", encoding="utf-8")
f.write(str(max_id))
f.close()