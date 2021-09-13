"""
GFG
Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number. 
For example, if n is 10, the output should be “2, 3, 5, 7”. If n is 20, the output should be “2, 3, 5, 7, 11, 13, 17, 19”.
"""
def Sieve_of_Eratosthenes(n: int):
    prime = [True for i in range(n+1)]

    p = 2
    while(p*p<=n):
        if(prime[p] == True):
            for i in range(p**p,n+1,p):
                prime[i] = False
        p+=1
    
    prime[0] = False
    prime[1] = False

    for p in range(n+1):
        if prime[p]:
            print(p)

n = 35
print(Sieve_of_Eratosthenes(n))