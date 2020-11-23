# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 22:08:38 2020

@author: Sudarshan Pol
"""

#functions

def preprocessing_corpus(corpus,stop_words,pstemmer): 
    temp = []
    post_dict = {}
    post_list = {}
    my_list = []   
    word_list = []
    for line in corpus:
        stemmed_words = []
        stop_filtered = []
        x = line.split("\t", 1)
        x[1] = x[1].lower()
        x[1] = x[1].replace("\n"," ")
        x[1] = re.sub("[^A-Za-z0-9]" ," " , x[1])
        x[1] = x[1].replace("    "," ")
        x[1] = x[1].replace("   "," ")
        x[1] = x[1].replace("  "," ")
        x[1] = x[1].strip()
        words = x[1].split(" ")

        for _ in words: 
            if not _ in stop_words: 
                stop_filtered.append(_)
            
        for _ in stop_filtered: 
            stemmed_words.append(pstemmer.stem(_)) 
        
        for _ in stemmed_words:
            word_list.append(_)
            
        z = [int(x[0]),stemmed_words]
        my_list.append(z)
        
    diction = list(dict.fromkeys(word_list))
    diction = sorted(diction)
    my_list = sorted(my_list)
    
    for _ in diction:
        post_list[_] = LinkedList()

    for i in my_list:
        for k in i[1]:
            if i[0] not in post_list[k].traverse_list():
                post_list[k].insert_at_end(i[0])

    for item in post_list.items():
        post_dict[item[0]] = int(len(item[1].traverse_list()))
            
    #post_dict_list = list(post_dict.items())
    #post_list_list = list(post_list.items())
    
    return post_dict,post_list

def preprocessing_query(query):
    stemmed_words = []
    stop_filtered = []
    
    query = query.lower()
    query = re.sub("[^A-Za-z0-9]" ," " ,query)
    query = query.strip()
    words = query.split(" ")

    
    for _ in words: 
            if not _ in stop_words: 
                stop_filtered.append(_)
                
    for _ in stop_filtered: 
            stemmed_words.append(pstemmer.stem(_))
            
    return stemmed_words
    
def matching(q_words,post_list):
    result = {}
    
    for word in q_words:
        if word in post_list.keys():
            result[word] = post_list[word]
    
    return result

def order(q_words):
    order = []
    output_sort = []
    final = []
    for word in q_words:
        order.append(post_dict[word])
        order.append(word)
        output_sort.append(order)
        order = []
    output_sort.sort()
    for _ in range(0,len(output_sort)):
        final.append(output_sort[_][1])
        
    return final
        
        
def search_sort(result,post_dict,post_list):
    order = []
    output_sort = []
    for word in result.keys():
        order.append(post_dict[word])
        order.append(post_list[word].traverse_list())
        output_sort.append(order)
        order = []
    output_sort.sort()
    return output_sort
    
def intersect(a,b,count):
    final = []
    
    n = a.start_node
    m = b.start_node
    while n is not None and m is not None:
        if n.value == m.value:
            final.append(n.value)
            count = count + 1
            n = n.next
            m = m.next
        elif n.value < m.value:
            count = count + 1
            n = n.next 
        else:
            count = count + 1
            m = m.next
            
    return final,count

