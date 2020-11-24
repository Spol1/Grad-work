# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 13:03:09 2020

@author: Sudarshan Pol
"""

import re 
import sys
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
import json

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
        
class LinkedList:

    def __init__(self, index=0, mode="simple"):
        self.start_node = None # Head pointer
        self.end_node = None # Tail pointer
        # Additional attributes
        self.index = index 
        self.mode = "simple"

    # Method to traverse a created linked list
    def traverse_list(self):
        traversal = []
        if self.start_node is None:
            return []
        else:
            n = self.start_node
            # Start traversal from head, and go on till you reach None
            while n is not None:
                traversal.append(n.value)
                n = n.next
            return traversal

    # Method to insert elements in the linked list
    def insert_at_end(self, value):
        if 'list' in str(type(value)):
            self.mode = "list"

        # Initialze a linked list element of type "Node" 
        new_node = Node(value)
        n = self.start_node # Head pointer

        if self.start_node is None:
            self.start_node = new_node
            self.end_node = new_node
            return "Inserted"
        
        elif self.mode == "list":
            if self.start_node.value[self.index] >= value[self.index]:
                self.start_node = new_node
                self.start_node.next = n
                return "Inserted"

            elif self.end_node.value[self.index] <= value[self.index]:
                self.end_node.next = new_node
                self.end_node = new_node
                return "Inserted"

            else:
                while value[self.index] > n.value[self.index] and value[self.index] < self.end_node.value[self.index] and n.next is not None:
                    n = n.next

                m = self.start_node
                while m.next != n and m.next is not None:
                    m = m.next
                m.next = new_node
                new_node.next = n
                return "Inserted"
        else:
            if self.start_node.value >= value:
                self.start_node = new_node
                self.start_node.next = n
                return "Inserted"

            elif self.end_node.value <= value:
                self.end_node.next = new_node
                self.end_node = new_node
                return "Inserted"

            else:
                while value > n.value and value < self.end_node.value and n.next is not None:
                    n = n.next

                m = self.start_node
                while m.next != n and m.next is not None:
                    m = m.next
                m.next = new_node
                new_node.next = n
                return "Inserted"

linked_list = LinkedList() #Initialize
linked_post = LinkedList()

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
    
    return post_dict,post_list

def preprocessing_query(query):
    stemmed_words = []
    stop_filtered = []
    
    query = query.lower()
    query = re.sub("[^A-Za-z0-9]" ," " ,query)
    query = query.replace("    "," ")
    query = query.replace("   "," ")
    query = query.replace("  "," ")
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
    final = LinkedList()
    count = 0
    n = a.start_node
    m = b.start_node
    while n is not None and m is not None:
        if n.value == m.value:
            final.insert_at_end(n.value)
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

def DaatAND(q_words, post_list):

    count = 0
    count_final = 0
    output_list = order(q_words)
    if len(output_list) == 2:
         a = post_list[output_list[0]]
         b = post_list[output_list[1]]
         c,count = intersect(a,b, count)
         count_final = count_final + count
            
    elif len(output_list) > 2:
        for _ in range(0,int(len(output_list))-1):

            if _ == 0:
                a = post_list[output_list[_]]
                b = post_list[output_list[int(_)+1]]
            else:    
                a = c
                b = post_list[output_list[int(_)+1]]
            
            c, count = intersect(a,b,count)
            count_final = count_final + count 
    
    elif (output_list) == 1:
        c = post_list[output_list[_]]
        
    result = c.traverse_list()
    
    results_doc['results'] = result
    results_doc['num_docs'] = len(result)
    results_doc['num_comparisons'] = count_final
    output_doc[query.lower()] = results_doc
    
    return output_doc

#Main

output_doc = {}
final_doc = {}
post_list_list = {}
count = 0
stop_words = set(stopwords.words('english'))
pstemmer = PorterStemmer()

#take input

corpus_path = sys.argv[1] #'input_corpus.txt'
output_path = sys.argv[2] #'output.json'
query_path =  sys.argv[3] #'query.txt'

'''
corpus_path = 'input_corpus.txt' #sys.argv[1]
output_path = 'output.json' #sys.argv[2] 
query_path = 'query.txt' #sys.argv[3]
'''

#import
corpus = open(str(corpus_path), "r", encoding="utf8")

#Populate Dictionary and Postings List
post_dict,post_list = preprocessing_corpus(corpus,stop_words,pstemmer)
corpus.close()

#Intake Queries
queries = open(str(query_path), "r", encoding="utf8")
query_list = []

for line in queries:
    query_list.append(str(line))
queries.close()

for _ in range(len(query_list)):
    count = 0
    results_doc = {}
    query = query_list[_].replace("\n","")
    q_words = preprocessing_query(query)
    output_doc = DaatAND(q_words,post_list)
    for _ in q_words:
        if _ not in post_list_list.keys():
            post_list_list[_] = post_list[_].traverse_list()
        
    
final_doc['postingsList'] = post_list_list 
final_doc['daatAnd'] = output_doc
    
f = open(str(output_path), "a", encoding="utf-8") 
f.write(json.dumps(final_doc))       
f.close()