"""
This set is related to dictionary python programs, question taken from GeeksOfGeeks
"""
import itertools as it
import functools as ft
from operator import itemgetter
from collections import Counter
from collections import OrderedDict
a = { 'a': [5, 6, 7, 8], 'a': [6, 12, 10, 8], 'c': [10, 11, 7, 5], 'd': [1, 2, 5] }
b = {'e': 200, 'f':400, 'g':600}
c = {'x': 25, 'y':18, 'z':45}
lis = [{ "name" : "Anant", "age" : 24}, 
{ "name" : "Ananya", "age" : 19 },
{ "name" : "Unnati" , "age" : 19 }]
a1 = {"name": ["Jan", "Feb," ,"March"], "month": [1, 2, 3]}
votes = ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john","johnny", "jamie", "johnny", "john"]
dict1 = {'c': [3], 'b': [12, 10], 'a': [19, 4]}
arr = ['cat', 'dog', 'tac', 'god', 'act']
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

"""
10) Basic Program to Append Dictionary Keys and Values ( In order ) in list
"""
#Method 1, using loops, list, keys and values
def DictList(x):
    l = []
    for i in x.keys():
        l.append(i)
    for i in x.values():
        l.append(i)
    return l
print(DictList(b))
#Time taken:  0.0039980411529541016

#Method 2, directly converting keys and values to list
def DictList1(x):
    return list(x.keys()) + list(x.values())
print(DictList1(b))
#Time taken:  0.0

#Method 3, using chain, keys and values
def DictList2(x):
    return list(it.chain(x.keys(),x.values()))
print(DictList2(b))
#Time taken:  0.0039937496185302734

"""
11) Basic Program to Sort Python Dictionaries by Key or Value
"""
#Method 1, using loop and sorted ,sorted keys only
for i in sorted(b.keys()):
    print(i, end = " ")
#Time taken:  0.00399470329284668

#Method 2, using loop and sorting through keys but printing both keys and values
for i in sorted(b):
    print((i,b[i]), end = " ")
#Time taken:  0.003993988037109375

"""
12) Basic Program to Sort Dictionary key and values List
"""
#Method 1, using loop and sorted ,sorted keys and values
res = dict()
for i in sorted(dict1):
    res[i] = sorted(dict1[i])
print(res)
#Time taken:  0.0010178089141845703

#Method 2, using dictionary comprehension
res1 = {key:sorted(dict1[key]) for key in sorted(dict1)}
print(res1)
#Time taken:  0.0010051727294921875

"""
13) Basic Program to Handling missing keys in Python dictionaries
"""
#Method 1, using get()
print(c.get('w'))
#Time taken:  0.000997781753540039

"""
14) Basic program dictionary with keys having multiple inputs
"""
#Here, only need to show having multiple keys for single value
dictz = {}
x,y,z = 1,2,3
dictz[x,y,z] = x + y + z
x,y,z = 8,2,2
dictz[x,y,z] = x + y - z
x,y,z = 4,2,8
dictz[x,y,z] = x - y - z
x,y,z = 9,3,7
dictz[x,y,z] = x + y * z
print(dictz)

"""
15) Basic Program to Print anagrams together in Python using List and Dictionary
"""
def allanagram(x):
    dictk = {}
    for i in x:
        key = ' '.join(sorted(x))
        if key in dictk.keys():
            dictk[key].append(i)
        else:
            dictk[key] = []
            dictk[key].append(i)
    output = ""
    for key,value in dictk.items():
        output = output + ' '.join(value) + ' '
    return output
print(allanagram(str))
#Not Working Ignore

"""
16) Basic Program K’th Non-repeating Character in Python using List Comprehension and OrderedDict
"""
#Method 1, doing as per the question asked
def KthNonRep(x,k):
    dict = OrderedDict.fromkeys(x,0) #Intializing values to 0 for every character
    #print(dict)
    for i in x:
        dict[i] += 1
    answerdict = [key for (key,value) in dict.items() if value == 1]
    #print(answerdict)
    if len(answerdict) < k:
        return "List doesnt have the kth non repeating character"
    else:
        return answerdict[k-1]
k=2
print(KthNonRep(str,k))
#Time taken:  0.000997304916381836

#Method 2, using list comprehension , dictionary comprehension
def KthNonRep1(x,k):
    l1 = list(x)
    d1 = {keys:x.count(keys) for keys in l1}
    l2 = [keys for keys,value in d1.items() if value == 1]
    if len(l2) < k:
        return "List doesnt have the kth non repeating character"
    else:
        return l2[k-1]
k=2
print(KthNonRep1(str,k))
#Time taken:  0.0009963512420654297

"""
17) Basic program to Check if binary representations of two numbers are anagram
"""
def checkBinaryAnagram(n1,n2):
    bin1 = bin(n1)[2:]
    bin2 = bin(n2)[2:]
    zeros = abs(len(bin1) - len(bin2))
    if(len(bin1)>len(bin2)):
        bin2 = zeros*'0' + bin2
    else:
        bin1 = zeros*'0' + bin1
    dict1 = Counter(bin1)
    dict2 = Counter(bin2)
    if dict1 == dict2:
        return "Yes"
    else:
        return "No"
print(checkBinaryAnagram(8,4))
#Time taken:  0.003991127014160156