"""
#This file contains Basic Program related to Array, Questiona take from Geeks of Geeks
"""

"""
1) Python Program to find sum of array in multiple ways
"""
l1 = [1,2,3,4]
#Method 1, Using function
def arraysum(x: int)->int:
    sum = 0
    for i in x:
        sum += i
    return sum
print("Sum of elements of array is ",arraysum(l1))

#Method 2, Using inbuilt sum function
ans = sum(l1)
print("Sum is ",ans)

#Mehod 3, using lambda and reduce
import functools as fs
print("Here the sum is ",fs.reduce(lambda x,y: x + y , l1))

"""
2) Basic Program to find largest element in an array
"""
#Method 1
l2 = [1,7,2,5,8,3,10,12,6,9]
def maxlist(x: int)->int:
    max = x[0]
    for i in range(0,len(x)):
        if x[i] > max:
            max = x[i]
    return max
print(maxlist(l2))

#Method 2
print(max(l2))

"""
3) Basic Program for array rotation
"""
#Using the same list of above program
#Method 1 , by creating empty list and manipulating from that
def arrRotation(x: list,d: int)->list:
    arr = []
    for i in range(0,d):
        arr.append(x[i])
    for i in range(0,d):
        x.remove(x[0])
    print("Elements that are rotating: ",arr)
    for i in arr:
        x.append(i)
    return x
d = int(input("Enter number of Indexes to be rotated: "))
print(arrRotation(l2,d))

#Method 2, by really rotating the array
def leftrotate(x: list,d: int,n: int):
    for i in range(d):
        leftrotating(x,n)
    return x
def leftrotating(x: list,n: int):
    temp = x[0]
    for i in range(n-1):
        x[i] = x[i+1]
    x[n-1] = temp
print(leftrotate(l2,2,len(l2)))

"""
4) Basic Program to Split the array and add the first part to the end
"""
#Using the first method if array rotation as it is doing the same
def arrRotation(x: list,d: int):
    arr = []
    for i in range(0,d):
        arr.append(x[i])
    for i in range(0,d):
        x.remove(x[0])
    for i in arr:
        x.append(i)
    return x
d = int(input("Enter number of Indexes to be rotated: "))
print(arrRotation(l2,d))
"""
5) Program for Find reminder of array multiplication divided by n
"""
#again using l2 as a list here
# Method 1 using lambda , map , math library
import math
divno = int(input("Enter Value of N: "))
Arrayremainder = list(map(lambda x : x % divno ,l2))
arrayproduct = math.prod(Arrayremainder)
finalanswer = arrayproduct % divno
print(finalanswer)
# Time Taken - 0.0009942054748535156

# Method 2 using lambda , map , functool library //It takes more time than math function
from functools import reduce
divno = int(input("Enter Value of N: "))
Arrayremainder = list(map(lambda x : x % divno ,l2))
arrayproduct = reduce(lambda x,y: x*y , Arrayremainder)
finalanswer = arrayproduct % divno
print(finalanswer)
# Time Taken - 0.0019919872283935547

"""
6) Basic Program to check if given array is Monotonic
An array A is monotone increasing if for all i <= j, A[i] <= A[j]. An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
"""
#Method 1 naive method
l3 = [1,2,3,4]
def monotonic(a):
    x = False
    y = False
    i = 0
    if a[0] < a[1]:
        while a[i] <= a[i+1]:
            i += 1
            if a[i] == a[len(a)-1]:
                break
            continue
        if a[i] == a[len(a)-1]:
            x = True
    else:
        while a[i] >= a[i+1]:
            i += 1
            if a[i] == a[len(a)-1]:
                break            
            continue
        if a[i] == a[len(a)-1]:
            y = True
    if x or y:
        return True
    else:
        return False
print(monotonic(l3))

#Method 2 Pythonic way using all() function
def monotonic1(a: list)-> bool:
    return all(a[i] >= a[i+1] for i in range(len(a)-1)) or all(a[i] <= a[i+1] for i in range(len(a)-1))
print(monotonic1(l3))