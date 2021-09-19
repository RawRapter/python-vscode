"""
Program for Number of solutions to Modular Equations

Given A and B, the task is to find the number of possible values that X can take such that the given modular equation (A mod X) = B holds good. Here, X is also called a solution of the modular equation.

Examples:

Input : A = 26, B = 2
Output : 6
Explanation
X can be equal to any of {3, 4, 6, 8,
12, 24} as A modulus any of these values
equals 2 i. e., (26 mod 3) = (26 mod 4) 
= (26 mod 6) = (26 mod 8) =Output:2 

Input : 21 5
Output : 2
Explanation
X can be equal to any of {8, 16} as A modulus 
any of these values equals 5 i.e. (21 mod 
8) = (21 mod 16) = 5
"""

def mod(a,b):
    c = 0
    for i in range(1,a):
        if(a%i == b):
            c += 1
    return c
print(mod(21,5))