import math

def max_prime_factor(n):
    max_prime = -1

    #Number of 2s that divides n
    while n%2 ==0:
        max_prime = 2
        n = n >> 1

    #all even done above, checking odd numbers
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i ==0:
            max_prime = i
            n = n/i
    #when n is prime
    if n > 2:
        max_prime = n
    
    return int(max_prime)

print(max_prime_factor(15))