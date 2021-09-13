"""
GFG
Program for Smallest K digit number divisible by X
Integers X and K are given. The task is to find smallest K-digit number divisible by X.

Examples:

Input : X = 83, K = 5
Output : 10043
10040 is the smallest 5 digit
number that is multiple of 83.

Input : X = 5, K = 2
Output : 10

An efficient solution would be :

Compute MIN : smallest K-digit number (1000...K-times)
If, MIN % X is 0, ans = MIN
else, ans = (MIN + X) - ((MIN + X) % X))
This is because there will be a number in 
range [MIN...MIN+X] divisible by X.
"""

def min(x,k):
    minimum = 10**(k-1)
    if(minimum%x == 0):
        return minimum
    else:
        return ((minimum+x)-((minimum+x)%x))

x = 83
k = 5
print(min(x,k))