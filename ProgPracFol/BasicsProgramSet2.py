#This file contains Basic Program related to Array
"""
1) Python Program to find sum of array in multiple ways
"""
l1 = [1,2,3,4]
#Using function
def arraysum(x):
    sum = 0
    for i in x:
        sum += i
    return sum
print("Sum of elements of array is ",arraysum(l1))

#Using inbuilt sum function
ans = sum(l1)
print("Sum is ",ans)

#using lambda and reduce
import functools as fs
print("Here the sum is ",fs.reduce(lambda x,y: x + y , l1))