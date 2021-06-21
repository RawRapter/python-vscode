"""
This set is related to dictionary python programs, question taken from GeeksOfGeeks
"""
import itertools as it
import functools as ft
a = { 'a': [5, 6, 7, 8], 'a': [6, 12, 10, 8], 'c': [10, 11, 7, 5], 'd': [1, 2, 5] }
b = {'a': 200, 'b':400, 'c':600}
c = {'x': 25, 'y':18, 'z':45}

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