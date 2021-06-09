"""
This File contains Pythons Program related to List, Questiona take from Geeks of Geeks.
Some Libraries are imported before all the Programs Please check them before trying any program
"""
#Creating some List for testing
L1 = [12, 35, 9, 56, 24]
L2 = [1, 2, 3]
L3 = [10,20,30,40,50]
L4 = [2,3,7,13,17,23]
L5 = [-1,1,-2,2,-3,3,-4,4]
L7 = [12,[], 35,[], 9,[], 56, 24]
L6 = [[2 ,1, 3],
 [4, 5, 7],
 [6, 9, 8]]
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

"""
13) Basic program to print even numbers in a list
"""
#Method 1, naive way 1 , creating new empty list and appending even elements
def EvenElementList1(x):
    x1 =[]
    for i in x:
        if i % 2 == 0:
            x1.append(i)
    return x1
print(EvenElementList1(L1))
#Time taken:  0.0009970664978027344

#Method 2, naive way 2, directly printing the elements, here none will be there in output as there is no return and 2 print
def EvenElementList3(x):
    for i in x:
        if i % 2 == 0:
            print(i,end=" ")

print(EvenElementList3(L1))
#Time taken:  0.0019915103912353516

#Method 3, Naive way 3 Using while loop, here none will be there in output as there is no return and 2 print
def EvenElementList2(x):
    i = 0
    while i < len(x):
        if x[i] % 2 == 0:
            print(x[i],end=" ")
        i += 1
print(EvenElementList2(L1))
#Time taken:  0.0019927024841308594

#Method 4, Pythonic way using lambda
def EvenElementList4(x):
    x1 = list(filter(lambda x: (x % 2 == 0), x))
    return x1
print(EvenElementList4(L1))
#Time taken:  0.0009965896606445312

#Method 5, Pythonic way using list comprehension
def EvenElementList(x):
    return [i for i in x if i % 2 == 0]
print(EvenElementList(L1))
#Time taken:  0.000997304916381836

"""
14) Basic program to print odd numbers in a List
"""
#Method 1, naive way 1 , creating new empty list and appending odd elements
def OddElementList1(x):
    x1 =[]
    for i in x:
        if i % 2 != 0:
            x1.append(i)
    return x1
print(OddElementList1(L1))
#Time taken:  0.0029916763305664062

#Method 2, naive way 2, directly printing the elements, here none will be there in output as there is no return and 2 print
def OddElementList3(x):
    for i in x:
        if i % 2 != 0:
            print(i,end=" ")

print(OddElementList3(L1))
#Time taken:  0.0009980201721191406

#Method 3, Naive way 3 Using while loop, here none will be there in output as there is no return and 2 print
def OddElementList2(x):
    i = 0
    while i < len(x):
        if x[i] % 2 != 0:
            print(x[i],end=" ")
        i += 1
print(OddElementList2(L1))
#Time taken:  0.001972675323486328

#Method 4, Pythonic way using lambda
def OddElementList4(x):
    x1 = list(filter(lambda x: (x % 2 != 0), x))
    return x1
print(OddElementList4(L1))
#Time taken:  0.000993490219116211

#Method 5, Pythonic way using list comprehension
def OddElementList(x):
    return [i for i in x if i % 2 != 0]
print(OddElementList(L1))
#Time taken:  0.0010035037994384766

"""
15) Basic program to print positive numbers in a list
"""
#Method 1 , List Comprehension
def PositiveList(x):
    return [ i for i in x if i > 0]
print(PositiveList(L5))
#Time taken:  0.0009975433349609375

#Method 2, using filter
def PositiveList1(x):
    return list(filter(lambda i : i > 0 , x))
print(PositiveList1(L5))
#Time taken:  0.0009953975677490234

#Method 3 , Naive Method using for loop
def PositiveList2(x):
    for i in x:
        if i >= 0:
            print(i, end = " ")
print(PositiveList2(L5))
#Time taken:  0.0019981861114501953

#Method 4 , Naive Method using while loop
def PositiveList3(x):
    i = 0
    while i < len(x):
        if x[i] >= 0:
            print(x[i], end = " ")
        i += 1    
print(PositiveList3(L5))
#Time taken:  0.0019979476928710938

"""
16) Basic program to print negative numbers in a list
"""
#Method 1 , List Comprehension
def PositiveList(x):
    return [ i for i in x if i < 0]
print(PositiveList(L5))
#Time taken:  0.0009975433349609375

#Method 2, using filter
def PositiveList1(x):
    return list(filter(lambda i : i < 0 , x))
print(PositiveList1(L5))
#Time taken:  0.0009953975677490234

#Method 3 , Naive Method using for loop
def PositiveList2(x):
    for i in x:
        if i < 0:
            print(i, end = " ")
print(PositiveList2(L5))
#Time taken:  0.0019981861114501953

#Method 4 , Naive Method using while loop
def PositiveList3(x):
    i = 0
    while i < len(x):
        if x[i] < 0:
            print(x[i], end = " ")
        i += 1    
print(PositiveList3(L5))
#Time taken:  0.0019979476928710938

"""
17) Basic program to print all positive numbers in a range
"""
n1 = int(input("Start: "))
n2 = int(input("End: "))

#Method 1, Using List Comprehension
pos = [i for in range(n1,n2 + 1) if i > 0]
print(pos)
#Time taken:  2.662982940673828

#Method 2, iterating
for i in range(n1,n2 + 1):
    if i > 0:
        print(i, end = " ")
#Time taken:  1.2213096618652344

"""
18) Basic program to print all positive numbers in a range
"""
n1 = int(input("Start: "))
n2 = int(input("End: "))

#Method 1, Using List Comprehension
pos = [i for i in range(n1,n2 + 1) if i < 0]
print(pos)
#Time taken:  1.6453924179077148

#Method 2, iterating
for i in range(n1,n2 + 1):
    if i < 0:
        print(i, end = " ")
#Time taken:  1.3188226222991943

"""
19) Basic Remove multiple elements from a list in Python
"""

#Method 1, using List comprehension
print("Our List: \n",L1)
n1 = int(input("Enter number of element you want to remove: "))
x = list(map(int, input("Enter {n} value(s): ").split()))
#x = [int(x) for x in input("Enter multiple value: ").split()]
main1 = [i for i in L1 if i not in x]
print(main1)

"""
20) Basic Remove empty List from List
"""
#Method 1, using list comprehension
print(L7)
x = [i for i in L7 if i!=[]]
print(x)
#Time taken:  0.0009961128234863281

#Method 2 , using filter
print(L7)
x = list(filter(None,L7))
print(x)
#Time taken:  0.000995635986328125