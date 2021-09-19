"""
Sum to Even factors of the given prime number
"""

import math

def sum_odd_Prime_Factors(n: int)->int:
    j = set()
    #Step 1
    while(n%2==0):
        j.add(2)
        n /= 2

    #Step 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while(n%i==0):
            j.add(i)
            n /= i
    #Step 3
    if n>2:
        j.add(int(n))
    
    j1 = list(j)
    print(j1)
    #going for odd sum
    sum = 1
    for i in j1:
        if(not(i&1)):
            sum += i
    return sum

print(sum_odd_Prime_Factors(30))