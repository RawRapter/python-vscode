"""
This set is related to dictionary python programs, question taken from GeeksOfGeeks
"""
import itertools as it
import functools as ft
from operator import itemgetter
from collections import Counter
a = { 'a': [5, 6, 7, 8], 'a': [6, 12, 10, 8], 'c': [10, 11, 7, 5], 'd': [1, 2, 5] }
b = {'e': 200, 'f':400, 'g':600}
c = {'x': 25, 'y':18, 'z':45}
lis = [{ "name" : "Anant", "age" : 24}, 
{ "name" : "Ananya", "age" : 19 },
{ "name" : "Unnati" , "age" : 19 }]
a1 = {"name": ["Jan", "Feb," ,"March"], "month": [1, 2, 3]}
votes = ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john","johnny", "jamie", "johnny", "john"]

"""
1) Basic program to Extract Unique values dictionary values
"""
#Method 1 , Using sorted(), set comprehension , values() 
def DictionaryUniqueValue(x):
    return list(sorted({ele for val in x.values() for ele in val}))
print(DictionaryUniqueValue(a))
#Time taken:  0.0010039806365966797

#Method 2, using chain
def DictionaryUniqueValue1(x):
    return list(sorted(set(it.chain(*x.values()))))
print(DictionaryUniqueValue1(a))
#Time taken:  0.0009984970092773438

"""
2) Basic Program to find the sum of all items in a dictionary
"""
#Method 1, iterating through values
def DictionaryValuesSum(x):
    result = 0
    for i in x.values():
        result += i
    return result
print(DictionaryValuesSum(b))
#Time taken:  0.0009925365447998047

#Method 2, directly iterating on dictionary
def DictionaryValuesSum1(x):
    result = 0
    for i in x:
        result += x[i]
    return result
print(DictionaryValuesSum1(b))
#Time taken:  0.0009937286376953125

#Method 3, using list comprehension and sum()
def DictionaryValuesSum2(x):
    return sum([i for i in x.values()])
print(DictionaryValuesSum2(c))
#Time taken:  0.000989675521850586

"""
3) Basic Program to Ways to remove a key from dictionary
"""
#Method 1, using del
del c['x']
print(c)
#Time taken:  0.0009965896606445312

#Method 2, using pop
deleted = c.pop('x')
print(deleted)
print(c)
#Time taken:  0.0009987354278564453

#Method 3, ldict. comprehension printing whole dictionary except that not require
new_list = {key:value for key,value in c.items() if key != 'x'}
print(new_list)
#Time taken:  0.000997781753540039

"""
4) Basic Program to sort list of dictionaries by values in Python – Using itemgetter
"""
#Sorting By Age Only
print(sorted(lis, key=itemgetter('age')))
#Sorting By Age and Name
print(sorted(lis, key=itemgetter('age','Name')))
#Reverse Sort by Age
print(sorted(lis, key=itemgetter('age'),reverse=True))

"""
5) Basic Program to sort list of dictionaries by values in Python – Using lambda function
"""
#Sorting By Age and Name
print(sorted(lis, key = lambda i: (i['age'],i['name'])))
#Sorting By Age only
print(sorted(lis, key = lambda i: i['age']))
#Reverse Sorting
print(sorted(lis, key = lambda i: i['age'], reverse= True))

"""
6) Basic program for Merging two Dictionaries
"""
#Method 1, using **
def DictMerge(x,y):
    return {**x ,**y}
print(DictMerge(a,b))
#Time taken:  0.0009968280792236328

#Method 2, using update()
def DictMerge1(x,y):
    x.update(y)
    return x
print(DictMerge1(a,b))
#Time taken:  0.0009989738464355469

"""
7) Basic Program Convert key-values list to flat dictionary
"""
#Using Zip
z = dict(zip(a1["month"],a1["name"]))
print(z)

"""
8) Basic program for Insertion at the beginning in OrderedDict
"""
#Method 1, using reverse amd update
def BegOrderedDict(x):
    x1 = dict(reversed(x.items()))
    x1.update({'a':'3'})
    x2 = dict(reversed(x1.items()))
    return x2
print(BegOrderedDict(b))

"""
9) Basic Program Dictionary and counter in Python to find winner of election
"""
#Method 1, using counter
def election(x):
    votc = Counter(x)
    k = max(votc.values())
    lst = [i for i in votc.keys() if votc[i] == k]
    lst1 = sorted(lst)
    return lst1[0]
print("Election Who won is: ",election(votes))
#Time taken:  0.0029973983764648438

#Method 2, using dictionary comprehension
def election(x):
    votc = {key:x.count(key) for key in x}
    k = max(votc.values())
    lst = [i for i in votc.keys() if votc[i] == k]
    lst1 = sorted(lst)
    return lst1[0]
print("Election Who won is: ",election(votes))
#Time taken:  0.0019865036010742188