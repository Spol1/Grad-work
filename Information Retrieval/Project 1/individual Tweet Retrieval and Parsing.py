# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:47:59 2020

@author: Sudarshan Pol
"""

#Check Place ID
places = api.geo_search(query="IN", granularity="country")

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

#Andrew Cuomo
total_tweets = 0
tweets = []

#tweets = api.search(q = " (from:NYGovCuomo) until:2020-09-15 since:2020-09-14 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = " (from:NYGovCuomo) until:2020-09-16 since:2020-09-15 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = " (from:NYGovCuomo) until:2020-09-17 since:2020-09-16 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = " (from:NYGovCuomo) until:2020-09-18 since:2020-09-17 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = " (from:NYGovCuomo) until:2020-09-19 since:2020-09-18 ", count = 1, tweet_mode = "extended")
tweets = api.search(q = " (from:NYGovCuomo) until:2020-09-20 since:2020-09-19 ", count = 1, tweet_mode = "extended")

trim_tweets = []
trim_tweets = tweets['statuses']
#trim_tweets = api.user_timeline(screen_name = 'NYGovCuomo', count = 100, tweet_mode = "extended")


print(str(len(trim_tweets)))
    
f = open("E:/Class/IR2020/POI/US_Cuomo.json", "a", encoding="utf-8")
for _ in range(len(trim_tweets)):
    trim_tweets[_]['country'] = 'USA'
    copy_poi(trim_tweets,_ )
    mentions(trim_tweets,_ )
    hashtags(trim_tweets,_ )
    tweet_urls(trim_tweets,_ )
    tweet = json.dumps(trim_tweets[_])
    max_id = trim_tweets[_]["id"] -1
    f.write(tweet)       
f.close()


'''for a in range(5):
    trim_tweets = []
    trim_tweets = api.user_timeline(screen_name = 'NYGovCuomo', count = 100, tweet_mode = "extended", max_id = max_id)

    #trim_tweets = tweets['statuses']
    
    f = open("E:/Class/IR2020/POI/US_Cuomo.json", "a", encoding="utf-8")
    for _ in range(len(trim_tweets)):
        
        trim_tweets[_]['country'] = 'USA'
        copy_poi(trim_tweets,_ )
        mentions(trim_tweets,_ )
        hashtags(trim_tweets,_ )
        tweet_urls(trim_tweets,_ )
        
        tweet = json.dumps(trim_tweets[_])
        max_id = trim_tweets[_]["id"] -1
        f.write(tweet)  
    f.close()
    print(str(len(trim_tweets)))'''

#Jerome Adams 
total_tweets = 0
tweets = []
string_list = []

#tweets = api.search(q = " (from:Surgeon_General) until:2020-09-15 since:2020-09-14 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = " (from:Surgeon_General) until:2020-09-16 since:2020-09-15 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = " (from:Surgeon_General) until:2020-09-17 since:2020-09-16 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = " (from:Surgeon_General) until:2020-09-18 since:2020-09-17 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = " (from:Surgeon_General) until:2020-09-19 since:2020-09-18 ", count = 1, tweet_mode = "extended")
tweets = api.search(q = " (from:Surgeon_General) until:2020-09-20 since:2020-09-19 ", count = 1, tweet_mode = "extended")

trim_tweets = []
trim_tweets = tweets['statuses']
#trim_tweets = api.user_timeline(screen_name = 'Surgeon_General', count = 100, tweet_mode = "extended")

print(str(len(trim_tweets)))
    
f = open("E:/Class/IR2020/POI/US_Adams.json", "a", encoding="utf-8")
for _ in range(len(trim_tweets)):
    trim_tweets[_]['country'] = 'USA'
    copy_poi(trim_tweets,_ )
    mentions(trim_tweets,_ )
    hashtags(trim_tweets,_ )
    tweet_urls(trim_tweets,_ )
    tweet = json.dumps(trim_tweets[_])
    max_id = trim_tweets[_]["id"] -1
    f.write(tweet)       
f.close()

'''for a in range(5):
    trim_tweets = []
    trim_tweets = api.user_timeline(screen_name = 'Surgeon_General', count = 100, tweet_mode = "extended", max_id = max_id)

    #trim_tweets = tweets['statuses']
    
    f = open("E:/Class/IR2020/POI/US_Adams.json", "a", encoding="utf-8")
    for _ in range(len(trim_tweets)):
        
        trim_tweets[_]['country'] = 'USA'
        copy_poi(trim_tweets,_ )
        mentions(trim_tweets,_ )
        hashtags(trim_tweets,_ )
        tweet_urls(trim_tweets,_ )
        
        tweet = json.dumps(trim_tweets[_])
        max_id = trim_tweets[_]["id"] -1
        f.write(tweet)  
    f.close()
    print(str(len(trim_tweets)))'''


#Donald Trump
total_tweets = 0
tweets = []
string_list = []

#tweets = api.search(q = "(from:realdonaldtrump) until:2020-09-19 since:2020-09-18 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:realdonaldtrump) until:2020-09-20 since:2020-09-19 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:realdonaldtrump) until:2020-09-15 since:2020-09-14 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:realdonaldtrump) until:2020-09-16 since:2020-09-15 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:realdonaldtrump) until:2020-09-17 since:2020-09-16 ", count = 1, tweet_mode = "extended")
tweets = api.search(q = "(from:realdonaldtrump) until:2020-09-18 since:2020-09-17 ", count = 1, tweet_mode = "extended")

trim_tweets = []
trim_tweets = tweets['statuses']
#trim_tweets = api.user_timeline(screen_name = 'realdonaldtrump', count = 100, tweet_mode = "extended")

print(str(len(trim_tweets)))
    
f = open("E:/Class/IR2020/POI/US_Trump.json", "a", encoding="utf-8")
for _ in range(len(trim_tweets)):
    trim_tweets[_]['country'] = 'USA'
    copy_poi(trim_tweets,_ )
    mentions(trim_tweets,_ )
    hashtags(trim_tweets,_ )
    tweet_urls(trim_tweets,_ )
    tweet = json.dumps(trim_tweets[_])
    max_id = trim_tweets[_]["id"] -1
    f.write(tweet)       
f.close()

'''for a in range(5):
    trim_tweets = []
    trim_tweets = api.user_timeline(screen_name = 'realdonaldtrump', count = 100, tweet_mode = "extended", max_id = max_id)

    #trim_tweets = tweets['statuses']
    
    f = open("E:/Class/IR2020/POI/US_Trump.json", "a", encoding="utf-8")
    for _ in range(len(trim_tweets)):
        
        trim_tweets[_]['country'] = 'USA'
        copy_poi(trim_tweets,_ )
        mentions(trim_tweets,_ )
        hashtags(trim_tweets,_ )
        tweet_urls(trim_tweets,_ )
        
        tweet = json.dumps(trim_tweets[_])
        max_id = trim_tweets[_]["id"] -1
        f.write(tweet)  
    f.close()
    print(str(len(trim_tweets)))
'''

#PM MODI
total_tweets = 0
tweets = []
string_list = []

#tweets = api.search(q = "(from:narendramodi) until:2020-09-19 since:2020-09-18 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:narendramodi) until:2020-09-20 since:2020-09-19 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:narendramodi) until:2020-09-15 since:2020-09-14 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:narendramodi) until:2020-09-16 since:2020-09-15 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:narendramodi) until:2020-09-17 since:2020-09-16 ", count = 1, tweet_mode = "extended")
tweets = api.search(q = "(from:narendramodi) until:2020-09-18 since:2020-09-17 ", count = 1, tweet_mode = "extended")

trim_tweets = []
trim_tweets = tweets['statuses']
#trim_tweets = api.user_timeline(screen_name = 'narendramodi', count = 100, tweet_mode = "extended")

print(str(len(trim_tweets)))
    
f = open("E:/Class/IR2020/POI/IN_Modi.json", "a", encoding="utf-8")
for _ in range(len(trim_tweets)):
    trim_tweets[_]['country'] = 'India'
    copy_poi(trim_tweets,_ )
    mentions(trim_tweets,_ )
    hashtags(trim_tweets,_ )
    tweet_urls(trim_tweets,_ )
    tweet = json.dumps(trim_tweets[_])
    max_id = trim_tweets[_]["id"] -1
    f.write(tweet)       
f.close()

'''for a in range(5):
    trim_tweets = []
    trim_tweets = api.user_timeline(screen_name = 'narendramodi', count = 100, tweet_mode = "extended", max_id = max_id)

    #trim_tweets = tweets['statuses']
    
    f = open("E:/Class/IR2020/POI/IN_Modi.json", "a", encoding="utf-8")
    for _ in range(len(trim_tweets)):
        
        trim_tweets[_]['country'] = 'India'
        copy_poi(trim_tweets,_ )
        mentions(trim_tweets,_ )
        hashtags(trim_tweets,_ )
        tweet_urls(trim_tweets,_ )
        
        tweet = json.dumps(trim_tweets[_])
        max_id = trim_tweets[_]["id"] -1
        f.write(tweet)  
    f.close()
    print(str(len(trim_tweets)))'''
    
#Ministry of Health
total_tweets = 0
tweets = []
string_list = []

#tweets = api.search(q = "(from:MoHFW_INDIA) until:2020-09-19 since:2020-09-18 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:MoHFW_INDIA) until:2020-09-20 since:2020-09-19 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:MoHFW_INDIA) until:2020-09-15 since:2020-09-14 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:MoHFW_INDIA) until:2020-09-16 since:2020-09-15 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:MoHFW_INDIA) until:2020-09-17 since:2020-09-16 ", count = 1, tweet_mode = "extended")
tweets = api.search(q = "(from:MoHFW_INDIA) until:2020-09-18 since:2020-09-17 ", count = 1, tweet_mode = "extended")

trim_tweets = []
trim_tweets = tweets['statuses']
#trim_tweets = api.user_timeline(screen_name = 'MoHFW_INDIA', count = 100, tweet_mode = "extended")

print(str(len(trim_tweets)))
    
f = open("E:/Class/IR2020/POI/IN_MoHealth.json", "a", encoding="utf-8")
for _ in range(len(trim_tweets)):
    trim_tweets[_]['country'] = 'India'
    copy_poi(trim_tweets,_ )
    mentions(trim_tweets,_ )
    hashtags(trim_tweets,_ )
    tweet_urls(trim_tweets,_ )
    tweet = json.dumps(trim_tweets[_])
    max_id = trim_tweets[_]["id"] -1
    f.write(tweet)       
f.close()

'''for a in range(6):
    trim_tweets = []
    trim_tweets = api.user_timeline(screen_name = 'MoHFW_INDIA', count = 100, tweet_mode = "extended", max_id = max_id)

    #trim_tweets = tweets['statuses']
    
    f = open("E:/Class/IR2020/POI/IN_MoHealth.json", "a", encoding="utf-8")
    for _ in range(len(trim_tweets)):
        
        trim_tweets[_]['country'] = 'India'
        copy_poi(trim_tweets,_ )
        mentions(trim_tweets,_ )
        hashtags(trim_tweets,_ )
        tweet_urls(trim_tweets,_ )
        
        tweet = json.dumps(trim_tweets[_])
        max_id = trim_tweets[_]["id"] -1
        f.write(tweet)  
    f.close()
    print(str(len(trim_tweets)))'''

#Dr Harsh Vardhan
total_tweets = 0
tweets = []
string_list = []

#tweets = api.search(q = "(from:drharshvardhan) until:2020-09-13 since:2020-09-12 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:drharshvardhan) until:2020-09-14 since:2020-09-13 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:drharshvardhan) until:2020-09-15 since:2020-09-14 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:drharshvardhan) until:2020-09-16 since:2020-09-15 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:drharshvardhan) until:2020-09-17 since:2020-09-16 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:drharshvardhan) until:2020-09-18 since:2020-09-17 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:drharshvardhan) until:2020-09-19 since:2020-09-18 ", count = 1, tweet_mode = "extended")
tweets = api.search(q = "(from:drharshvardhan) until:2020-09-20 since:2020-09-19 ", count = 1, tweet_mode = "extended")

trim_tweets = []
trim_tweets = tweets['statuses']
#trim_tweets = api.user_timeline(screen_name = 'drharshvardhan', count = 100, tweet_mode = "extended")

print(str(len(trim_tweets)))
    
f = open("E:/Class/IR2020/POI/IN_harshvardhan.json", "a", encoding="utf-8")
for _ in range(len(trim_tweets)):
    trim_tweets[_]['country'] = 'India'
    copy_poi(trim_tweets,_ )
    mentions(trim_tweets,_ )
    hashtags(trim_tweets,_ )
    tweet_urls(trim_tweets,_ )
    tweet = json.dumps(trim_tweets[_])
    max_id = trim_tweets[_]["id"] -1
    f.write(tweet)       
f.close()

'''for a in range(5):
    trim_tweets = []
    trim_tweets = api.user_timeline(screen_name = 'drharshvardhan', count = 100, tweet_mode = "extended", max_id = max_id)

    #trim_tweets = tweets['statuses']
    
    f = open("E:/Class/IR2020/POI/IN_harshvardhan.json", "a", encoding="utf-8")
    for _ in range(len(trim_tweets)):
        
        trim_tweets[_]['country'] = 'India'
        copy_poi(trim_tweets,_ )
        mentions(trim_tweets,_ )
        hashtags(trim_tweets,_ )
        tweet_urls(trim_tweets,_ )
        
        tweet = json.dumps(trim_tweets[_])
        max_id = trim_tweets[_]["id"] -1
        f.write(tweet)  
    f.close()
    print(str(len(trim_tweets)))'''

#Giuseppe Conte
total_tweets = 0
tweets = []
string_list = []

#tweets = api.search(q = "(from:GiuseppeConteIT) until:2020-09-13 since:2020-09-12 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:GiuseppeConteIT) until:2020-09-14 since:2020-09-13 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:GiuseppeConteIT) until:2020-09-15 since:2020-09-14 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:GiuseppeConteIT) until:2020-09-16 since:2020-09-15 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:GiuseppeConteIT) until:2020-09-17 since:2020-09-16 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:GiuseppeConteIT) until:2020-09-18 since:2020-09-17 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:GiuseppeConteIT) until:2020-09-19 since:2020-09-18 ", count = 1, tweet_mode = "extended")
tweets = api.search(q = "(from:GiuseppeConteIT) until:2020-09-20 since:2020-09-19 ", count = 1, tweet_mode = "extended")

trim_tweets = []
trim_tweets = tweets['statuses']
#trim_tweets = api.user_timeline(screen_name = 'GiuseppeConteIT', count = 100, tweet_mode = "extended")

print(str(len(trim_tweets)))
    
f = open("E:/Class/IR2020/POI/IT_Conte.json", "a", encoding="utf-8")
for _ in range(len(trim_tweets)):
    trim_tweets[_]['country'] = 'Italy'
    copy_poi(trim_tweets,_ )
    mentions(trim_tweets,_ )
    hashtags(trim_tweets,_ )
    tweet_urls(trim_tweets,_ )
    tweet = json.dumps(trim_tweets[_])
    max_id = trim_tweets[_]["id"] -1
    f.write(tweet)       
f.close()

'''for a in range(5):
    trim_tweets = []
    trim_tweets = api.user_timeline(screen_name = 'GiuseppeConteIT', count = 100, tweet_mode = "extended", max_id = max_id)

    #trim_tweets = tweets['statuses']
    
    f = open("E:/Class/IR2020/POI/IT_Conte.json", "a", encoding="utf-8")
    for _ in range(len(trim_tweets)):
        
        trim_tweets[_]['country'] = 'Italy'
        copy_poi(trim_tweets,_ )
        mentions(trim_tweets,_ )
        hashtags(trim_tweets,_ )
        tweet_urls(trim_tweets,_ )
        
        tweet = json.dumps(trim_tweets[_])
        max_id = trim_tweets[_]["id"] -1
        f.write(tweet)  
    f.close()
    print(str(len(trim_tweets)))'''
    
#Ministry of Health
total_tweets = 0
tweets = []
string_list = []

#tweets = api.search(q = "(from:MinisteroSalute) until:2020-09-13 since:2020-09-12 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:MinisteroSalute) until:2020-09-14 since:2020-09-13 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:MinisteroSalute) until:2020-09-15 since:2020-09-14 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:MinisteroSalute) until:2020-09-16 since:2020-09-15 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:MinisteroSalute) until:2020-09-17 since:2020-09-16 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:MinisteroSalute) until:2020-09-18 since:2020-09-17 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:MinisteroSalute) until:2020-09-19 since:2020-09-18 ", count = 1, tweet_mode = "extended")
tweets = api.search(q = "(from:MinisteroSalute) until:2020-09-20 since:2020-09-19 ", count = 1, tweet_mode = "extended")

trim_tweets = []
trim_tweets = tweets['statuses']
#trim_tweets = api.user_timeline(screen_name = 'MinisteroSalute', count = 100, tweet_mode = "extended")

print(str(len(trim_tweets)))
    
f = open("E:/Class/IR2020/POI/IT_MoHealth.json", "a", encoding="utf-8")
for _ in range(len(trim_tweets)):
    trim_tweets[_]['country'] = 'Italy'
    copy_poi(trim_tweets,_ )
    mentions(trim_tweets,_ )
    hashtags(trim_tweets,_ )
    tweet_urls(trim_tweets,_ )
    tweet = json.dumps(trim_tweets[_])
    max_id = trim_tweets[_]["id"] -1
    f.write(tweet)       
f.close()

'''for a in range(5):
    trim_tweets = []
    trim_tweets = api.user_timeline(screen_name = 'MinisteroSalute', count = 100, tweet_mode = "extended", max_id = max_id)

    #trim_tweets = tweets['statuses']
    
    f = open("E:/Class/IR2020/POI/IT_MoHealth.json", "a", encoding="utf-8")
    for _ in range(len(trim_tweets)):
        
        trim_tweets[_]['country'] = 'Italy'
        copy_poi(trim_tweets,_ )
        mentions(trim_tweets,_ )
        hashtags(trim_tweets,_ )
        tweet_urls(trim_tweets,_ )
        
        tweet = json.dumps(trim_tweets[_])
        max_id = trim_tweets[_]["id"] -1
        f.write(tweet)  
    f.close()
    print(str(len(trim_tweets)))'''
    
    
#Matteo Renzi
total_tweets = 0
tweets = []
string_list = []

#tweets = api.search(q = "(from:matteorenzi) until:2020-09-13 since:2020-09-12 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:matteorenzi) until:2020-09-14 since:2020-09-13 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:matteorenzi) until:2020-09-15 since:2020-09-14 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:matteorenzi) until:2020-09-16 since:2020-09-15 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:matteorenzi) until:2020-09-17 since:2020-09-16 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:matteorenzi) until:2020-09-18 since:2020-09-17 ", count = 1, tweet_mode = "extended")
#tweets = api.search(q = "(from:matteorenzi) until:2020-09-19 since:2020-09-18 ", count = 1, tweet_mode = "extended")
tweets = api.search(q = "(from:matteorenzi) until:2020-09-20 since:2020-09-19 ", count = 1, tweet_mode = "extended")

trim_tweets = []
trim_tweets = tweets['statuses']
#trim_tweets = api.user_timeline(screen_name = 'matteorenzi', count = 100, tweet_mode = "extended")

print(str(len(trim_tweets)))
    
f = open("E:/Class/IR2020/POI/IT_Renzi.json", "a", encoding="utf-8")
for _ in range(len(trim_tweets)):
    trim_tweets[_]['country'] = 'Italy'
    copy_poi(trim_tweets,_ )
    mentions(trim_tweets,_ )
    hashtags(trim_tweets,_ )
    tweet_urls(trim_tweets,_ )
    tweet = json.dumps(trim_tweets[_])
    max_id = trim_tweets[_]["id"] -1
    f.write(tweet)       
f.close()

'''for a in range(5):
    trim_tweets = []
    trim_tweets = api.user_timeline(screen_name = 'matteorenzi', count = 100, tweet_mode = "extended", max_id = max_id)

    #trim_tweets = tweets['statuses']
    
    f = open("E:/Class/IR2020/POI/IT_Renzi.json", "a", encoding="utf-8")
    for _ in range(len(trim_tweets)):
        
        trim_tweets[_]['country'] = 'Italy'
        copy_poi(trim_tweets,_ )
        mentions(trim_tweets,_ )
        hashtags(trim_tweets,_ )
        tweet_urls(trim_tweets,_ )
        
        tweet = json.dumps(trim_tweets[_])
        max_id = trim_tweets[_]["id"] -1
        f.write(tweet)  
    f.close()
    print(str(len(trim_tweets)))'''