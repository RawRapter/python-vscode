"""
This File contains Pythons Program related to List, Questiona take from Geeks of Geeks.
Some Libraries are imported before all the Programs Please check them before trying any program
"""
#Creating some List for testing
L1 = [12, 35, 9, 56, 24]
L2 = [1, 2, 3]
L3 = [10,20,30,40,50]
L4 = [2,3,7,13,17,23]
#Import Libraries that can be required in the programs
import functools as fs
import numpy as np
import math
"""
1) Basic program to interchange first and last elements in a list
"""
#Method 1 Basic Swap
def interchange(x):
    temp = x[0]
    x[0] = x[-1]
    x[-1] = temp
    return x
print(interchange(L1))
#Time taken:  0.0009970664978027344

#Method 2 Pythonic Swap
def interchange1(x):
    x[0],x[-1] = x[-1],x[0]
    return x
print(interchange1(L1))
#Time taken:  0.0009958744049072266

"""
2) Basic program to swap two elements in a list(input list and 2 places to be swapped, taking first elements as position one(not index))
"""
def Swap2ListEle(x,a,b):
    x[a],x[b] = x[b],x[a]
    return x
a = input("Enter First Position: ")
b = input("Enter Second Position: ")
print(Swap2ListEle(L1,a -1,b -1))
#Time taken:  0.0010004043579101562

"""
3) Basic Ways to find length of list
"""
#First way
print(len(L1))
#Second Way naive one counting
count = 0
for i in L1:
    count += 1
print(count)
#Third way by importing operator length_hint
from operator import length_hint
print(length_hint(L1))

"""
4) Basic Ways to check if element exists in list
"""
#Method 1: Naive one Iterating through all list
def checkEleNaive(x,a):
    for i in x:
        if i == a:
            return "Element found in the list"
    return "Element Not Found"
print(checkEleNaive(L1,9))
#Time taken:  0.0020017623901367188

#Method 2: Using in
def checkEleNaive1(x,a):
    if a in x:
        return "Element found in the list"
    return "Element Not Found"
print(checkEleNaive1(L1,9))
#Time taken:  0.0009968280792236328

"""
5) Basic Different ways to clear a list in Python
"""
#Method 1 , using clear method
print("Before Clear: ",L1)
L1.clear()
print("After Clear: ",L1)

#Method 2, Multiplying all elements by 0 This will make elements 0
print(map(lambda x : x*0, L2))

#Method 3, reinitializing
L3=[]
print(L3)

#Method 4, multiplying list with 0
L4 *= 0 
print(L4)

#Method 5, using del function
del L1[:]
print(L1)

"""
6) Basic program Reversing a List
"""
#Method 1 , using reversed function
def reverse1(x):
    return [i for i in reversed(x)]
print(reverse1(L1))

#Method 2 , using reverse
def reverse2(x):
    x.reverse()
    return x
print(reverse2(L2))

#Method 3, using slicing
def reverse3(x):
    x1 = x[::-1]
    return x1
print(reverse3(L3))

"""
7) Basic program to find sum of elements in list
"""
def listsum(x):
    sum = 0
    for i in x:
        sum += i
    return sum
print("Sum of elements of array is ",listsum(L1))

#Using inbuilt sum function
ans = sum(L1)
print("Sum is ",ans)

#using lambda and reduce
print("Here the sum is ",fs.reduce(lambda x,y: x + y , L1))

"""
8) Basic Multiply all numbers in the list
"""
#Method 1, using reduce
def ListMultiplyReduce(x):
    ans = fs.reduce(lambda x,y:x*y, x)
    return ans
print(ListMultiplyReduce(L2))
#Time taken:  0.0009980201721191406

#Method 2 , using traversal
def ListMultiplyTraverse(x):
    ans = 1
    for i in x:
        ans *= i
    return ans
print(ListMultiplyTraverse(L1))
#Time taken:  0.000997304916381836

#Method 3, using numpy
def ListMultiplyNumpy(x):
    ans = np.prod(x)
    return ans
print(ListMultiplyNumpy(L1))
#Time taken:  0.0008940696716308594

#Method 4, using math library
def ListMultiplyMath(x):
    ans = math.prod(x)
    return ans
print(ListMultiplyMath(L1))
#Time taken:  0.0009989738464355469

"""
9) Basic program to find smallest number in a list
"""
#Method 1, using numpy min
def SmallElementList(x):
    ans = np.min(x)
    return ans
print(SmallElementList(L1))
#Time taken:  0.002989053726196289

#Method 2, traversing
def  SmallElementsListTraverse(x):
    min = x[0]
    for i in range(len(x)):
        if x[i] < min:
            min = x[i]
    return min
print(SmallElementsListTraverse(L1))
#Time taken:  0.002994537353515625

#Method 3, using sort() function
def SmallElementListSort(x):
    x.sort()
    return x[0]
print(SmallElementListSort(L1))
#Time taken:  0.0009975433349609375

#Method 4, using inbuilt min
print(min(L1))
#Time taken:  0.0020165443420410156

"""
10) Basic program to find largest number in a list
"""
#Method 1, using numpy max
def LargeElementList(x):
    ans = np.max(x)
    return ans
print(LargeElementList(L1))
#Time taken:  0.003988504409790039

#Method 2, traversing
def  LargeElementsListTraverse(x):
    max = x[0]
    for i in range(len(x)):
        if x[i] > max:
            max = x[i]
    return max
print(LargeElementsListTraverse(L1))
#Time taken:  0.0020012855529785156

#Method 3, using sort() function
def LargeElementListSort(x):
    x.sort()
    return x[-1]
print(LargeElementListSort(L1))
#Time taken:  0.000995635986328125

#Method 4, using inbuilt min
print(max(L1))
#Time taken:  0.0009975433349609375

"""
11) Basic program to find second largest number in a list
"""
#Method 1 , Using Sort
def SecondLargeElementListSort(x):
    x.sort()
    return x[-2]
print(SecondLargeElementListSort(L1))
#Time taken:  0.0010037422180175781

#Method 2, Using sorted
print(sorted(L1)[-2])
#Time taken:  0.0019876956939697266

#Method 3, removing max thus second largest becomes max by converting to set
def SecondLargeElementListRemove(x):
    set1 = set(x)
    set1.remove(max(set1))
    return max(set1)
print(SecondLargeElementListRemove(L1))
#Time taken:  0.000997304916381836

#Method 4, removing max thus second largest becomes max
def SecondLargeElementListRemove1(x):
    x.remove(max(x))
    return max(x)
print(SecondLargeElementListRemove1(L3))
#Time taken:  0.0019948482513427734

"""
12) Basic program to find N largest elements from a list
"""
#Method 1, using sort
n1 = int(input("Tell a number you want number of largest numbers from list: "))
def NLargest(x):
    x.sort(reverse = True)
    return x[0:n1]
print(NLargest(L1))

#Method 2, using sorted
n1 = int(input("Tell a number you want number of largest numbers from list: "))
print(sorted(L1,reverse=True)[0:n1])

#Method 3, using sort but not reversing
n1 = int(input("Tell a number you want number of largest numbers from list: "))
L1.sort()
print(L1[-n1:])

#Method 4, using traversal, remove, append
n1 = int(input("Tell a number you want number of largest numbers from list: "))
def Nlargest1(x,n1):
    newx = []
    for i in range(n1):
        max = 0
        for i in range(len(x)):
            if x[i] > max:
                max = x[i]
        x.remove(max)
        newx.append(max)
    return newx
print(Nlargest1(L1,n1))