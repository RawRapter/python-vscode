"""
GFG
Program for Find minimum sum of factors of number

Given a number, find minimum sum of its factors.

Examples:

Input : 12
Output : 7
Explanation: 
Following are different ways to factorize 12 and
sum of factors in different ways.
12 = 12 * 1 = 12 + 1 = 13
12 = 2 * 6 = 2 + 6 = 8
12 = 3 * 4 = 3 + 4 = 7
12 = 2 * 2 * 3 = 2 + 2 + 3 = 7
Therefore minimum sum is 7

Input : 105
Output : 15
"""

def min_sum(n):
    sum = 0

    i = 2
    while(i*i <= n):
        while(n % i == 0):
            sum += i
            n /= i
        i += 1
    sum += n
    return sum

n = 105
print(min_sum(n))