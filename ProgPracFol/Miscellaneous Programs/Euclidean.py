"""
Program for Basic Euclidean algorithms
"""
#Basic
def gcd(a,b):
    #print(a,b)
    if(a==0):
        return b
    return gcd(b%a,a)

a = 16
b = 12
print(gcd(16,12))
