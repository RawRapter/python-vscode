"""
Given a number n, we need to find the product of all of its unique prime factors.
"""

import math

#Method 1
def product_Prime_Factors(n: int)->int:
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
    return math.prod(j1)

print(product_Prime_Factors(30))

#Method 2
#Here, we are taking unique factor using if conditions and directly multiple the result into variable product
def product_Prime_Factors1(n: int)->int:
    product = 1
      
    if (n % 2 == 0):
        product *= 2
        while (n%2 == 0):
            n = n/2
              
    for i in range (3, int(math.sqrt(n)), 2):
        if (n % i == 0):
            product = product * i
            while (n%i == 0):
                n = n/i
                  
    if (n > 2):
        product = product * n
          
    return product

print(product_Prime_Factors1(10))