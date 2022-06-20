"""
This set is related to tuple python programs
"""
#Import Files
from operator import rshift
import sys, re
from itertools import chain,product
from typing import Dict

#Tuples
Tuple1 = ("anant", "arun", "kumar", "tiwari", "uttar", "pradesh")
Tuple2 = (8,4,6,3,2,1,9,7,5)
Tuple3 = (1,7)
Tuple4 = (4,2)
Tuple5 = ([1], [2], [3], [4])
Tuple6 = ((1, "anant", 2), (3, "arun", 4))

#lists
list1 = [6, 7, 8, 9]
list5 = ["anant", "arun", "kumar", "tiwari"]
keys1 = ["key","value","ID"]

#List of tuple
list2 = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
list3 = [(3,),(1,2,3),(5,6),(3,5,7,9)]
list4 = [("anant",4),("arun",2),("tiwari",3),("kumar",1)]

"""
1) Program to Find the size of a Tuple
"""
#Method 1, using __sizeof__ (Doesn't Include Garbage Space)
print("Size of element is ",Tuple1.__sizeof__()," bytes")

#Method 2, using sys library (Includes Garbage Space)
print("Size of element is ",sys.getsizeof(Tuple1)," bytes")

"""
2) Program to find Maximum and Minimum K elements in Tuple
"""
#Method 1, using slicing and sorted
def KSetMinMax(x,k):
    x = sorted(x)
    x1 = x[:k] + x[-k:]
    return tuple(x1)
print(KSetMinMax(Tuple2,2))
#Time is very small that it is showing 0

#Method 2, using loops and sorted
def KSetMinMax1(x,k):
    x = list(sorted(x))
    result = []
    for id,ele in enumerate(x):
        if id < k or id >= (len(x) - k):
            result.append(ele)
    return tuple(result)
print(KSetMinMax1(Tuple2,2))
#Time taken:  0.003995180130004883

"""
3) Program to Create a list of tuples from given list having number and its cube in each tuple
"""
#Method 1, normal way
def NumCubeList(x):
    result = []
    for i in x:
        result.append((i,pow(i,3)))
    return result
print(NumCubeList(list1))
#Time taken:  0.0040013790130615234

#Method 2, using list comprehension
def NumCubeList1(x):
    result = [(i,pow(i,3)) for i in x]
    return result
print(NumCubeList(list1))
#Time taken:  0.003994941711425781

"""
4) Programm to Adding Tuple to List and vice – versa
"""
#Method 1, using loops
def tupletolist(x,y):
    for i in y:
        x.append(i)
    return x
print(tupletolist(list1,Tuple2))
#Time taken:  0.004004716873168945

#Method 2, directly adding
list1 += Tuple2
print(list1)
#Time is very small that it is showing 0

#Method 3,using data type conversion
print(tuple(list(Tuple2) + list1))
#Time is very small that it is showing 0

"""
5) Program to Join Tuples if similar initial element
"""
#Using dictionary from GFG
def JoinIntialEletuple(x):
    rsult = []
    for i in x:
        if rsult and rsult[-1][0] == i[0]:
            rsult[-1].extend(i[1:])
        else:
            rsult.append([ele for ele in i])
    rsult = list(map(tuple,rsult))
    return rsult
print(JoinIntialEletuple(list2))
#Time taken:  0.0009980201721191406

"""
6) Program to Extract digits from Tuple list
"""
#From GFG
def ExtractDigits(x):
    temp = re.sub(r'[\[\]\(\), ]', '', str(x))
    res = [int(ele) for ele in set(temp)]
    return res
print(ExtractDigits(list2))
#Time taken:  0.0009970664978027344

"""
7) Program to get All pair combinations of 2 tuples
"""
#Method 1, using list comprehension
def TuplePairs(x,y):
    result = [(a,b) for a in x for b in y]
    result += [(a,b) for a in y for b in x]
    return result
print(TuplePairs(Tuple3,Tuple4))
#Time taken:  0.000997781753540039

#Method 2, using chain and product
def TuplePairs1(x,y):
    result = list(chain(product(x,y),product(y,x)))
    return result
print(TuplePairs1(Tuple3,Tuple4))
#Time taken:  0.0009987354278564453

"""
8) Program to Remove Tuples of Length K
"""
#Method 1, using list comprehension
def RemoveTuple(x,k):
    result = [i for i in x if len(i) != k]
    return result
print(RemoveTuple(list3,2))
#Time taken:  0.0009999275207519531
#Same can be done using normal for loop and if condition

#Method 2, using filter, lambda and length
def RemoveTuple1(x,k):
    result = list(filter(lambda i:len(i)!=k,x))
    return result
print(RemoveTuple1(list3,2))
#Time taken:  0.0009961128234863281


"""
9) Program to Sort a list of tuples by second Item
"""
#Method 1, using sort()
def SortTuple(x):
    x.sort(key = lambda x:x[1])
    return x
print(SortTuple(list4))
#Time taken:  0.003995180130004883

#Method 2, using sorted
def SortTuple1(x):
    return sorted(x,key=lambda x:x[1])
print(SortTuple1(list4))
#Time taken:  0.003994464874267578

#Method 3, manual sorting
def SortTuple2(x):
    length = len(x)
    for i in range(length):
        for j in range(length-i-1):
            if x[j][1] > x[j+1][1]:
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
    return x
print(SortTuple2(list4))
#Time taken:  0.003973484039306641

"""
10) Program to Order Tuples using external List
"""
#Method 1, using sorted
def OrderTuple(x,y):
    return sorted(x,key=lambda y:y)
print(OrderTuple(list4,list5))
#Time taken:  0.0039937496185302734

#Method 2, using sort
def OrderTuple1(x,y):
    x.sort(key=lambda y:y)
    return x
print(OrderTuple1(list4,list5))
#Time taken:  0.003994464874267578

#Method 3, using dictionary and list comprehnsion
def OrderTuple2(x,y):
    x1= dict(x)
    result = [(key,x1[key]) for key in y]
    return result
print(OrderTuple2(list4,list5))
#Time taken:  0.003991603851318359

"""
11) Program to Flatten tuple of List to tuple
"""
#Method 1
print(tuple(sum(Tuple5,[])))

"""
12) Program to Convert Nested Tuple to Custom Key Dictionary
"""
#Method 1
result = [{key:pair for key,pair in zip(keys1,sub)} for sub in Tuple6]
print(result)
#Time taken:  0.004037618637084961