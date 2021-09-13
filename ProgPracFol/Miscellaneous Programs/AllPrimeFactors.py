"""
Following are the steps to find all prime factors.
1) While n is divisible by 2, print 2 and divide n by 2.
2) After step 1, n must be odd. Now start a loop from i = 3 to square root of n. 
While i divides n, print i and divide n by i, increment i by 2 and continue.
3) If n is a prime number and is greater than 2, then n will not become 1 by above two steps. So print n if it is greater than 2.
"""
import math

def prime_factor(n: int)->int:
    #Step 1
    while(n%2==0):
        print(2)
        n /= 2

    #Step 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while(n%i==0):
            print(i)
            n /= i
    #Step 3
    if n>2:
        print(int(n))

print(prime_factor(520))