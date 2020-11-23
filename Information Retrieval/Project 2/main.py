# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 22:08:38 2020

@author: Sudarshan Pol
"""

#Main

start = time.time()
output_doc = {}
final_doc = {}
post_list_list = {}
count = 0
stop_words = set(stopwords.words('english'))
pstemmer = PorterStemmer()

#take input
corpus_path = 'input_corpus.txt' #sys.argv[1]
output_path = 'output.json' #sys.argv[2] 
query_path = 'query.txt' #sys.argv[3]

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
#    result = matching(q_words,post_list)
#    output_list = search_sort(result,post_dict,post_list)
    output_list = order(q_words)
    
    a =[]
    b =[]
    

    if len(output_list) == 2:
         a = post_list[output_list[0]]
         b = post_list[output_list[1]]
         a,count = intersect(a,b, count)
            
    elif len(output_list) > 2:
        for _ in range(0,int(len(output_list))-2):

            if _ == 0:
                a = post_list[output_list[_]]
                b = post_list[output_list[int(_)+1]]

            a, count = intersect(a,b,count)
            b = post_list[output_list[int(_)+2]]
    
    elif (output_list) == 1:
        a = post_list[output_list[_]].traverse_list()
    
    results_doc['results'] = a
    results_doc['num_docs'] = len(a)
    results_doc['num_comparisons'] = count
    output_doc[query.lower()] = results_doc

for k,v in post_list.items():
    post_list_list[k] = v.traverse_list()
    
final_doc['postingsList'] = post_list_list 
final_doc['daatAND'] = output_doc
    
f = open(str(output_path), "a", encoding="utf-8") 
f.write(json.dumps(final_doc))       
f.close()

end = time.time()

print(f"Runtime of the program is {end - start}")