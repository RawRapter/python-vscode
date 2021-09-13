"""
GFG Site
Python Program for Maximum height when coins are arranged in a triangle
We have N coins which need to arrange in form of a triangle, i.e. first row will have 1 coin, 
second row will have 2 coins and so on, we need to tell maximum height which we can achieve by using these N coins.

Input : N = 7
Output : 3
Maximum height will be 3, putting 1, 2 and
then 3 coins. It is not possible to use 1 
coin left.
"""
import math

""" def squareRoot(n):
	x = n
	y = 1

	e = 0.000001 # e decides the accuracy level
	while (x - y > e):
		x = (x + y) / 2
		y = n/x
	return x """


def findMaximumHeight(N):

	n = 1 + 8*N
    
	maxH = (-1 + math.sqrt(n)) / 2
	return int(maxH)


# Driver code to test above method
N = 12
print(findMaximumHeight(N))