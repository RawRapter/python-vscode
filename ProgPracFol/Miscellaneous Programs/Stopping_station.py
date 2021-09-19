"""
GFG
Program for Number of stopping station problem

There are 12 intermediate stations between two places A and B.
Find the number of ways in which a train can be made to stop at 4 
of these intermediate stations so that no two stopping stations are consecutive?

Examples –
Input  : n = 12, s = 4
Output : 126

Input  : n = 16, s = 5
Output : 792
"""

def stopping_station( p, n):
    num = 1
    dem = 1
    s = p
    while p != 1:
        dem *= p
        p-=1
      
    t = n - s + 1
    while t != (n-2 * s + 1):
        num *= t
        t-=1
    if (n - s + 1) >= s:
        return int(num/dem)
    else:
        return -1
  
# driver code 
num = stopping_station(4, 12)
if num != -1:
    print(num)
else:
    print("Not Possible")