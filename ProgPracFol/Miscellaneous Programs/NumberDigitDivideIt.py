"""
Program for Check if all digits of a number divide it

Given a number n, find whether all digits of n divide it or not.
Examples: 
Input : 128
Output : Yes
128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Input : 130
Output : No
"""
def digitdivide(x):
    m = x
    try:
        while(x):
            n = x%10
            if(m%n == 0):
                x //= 10
                continue
            else:
                return "All digits are not dividing: ",m
        return "All digits are dividing: ",m
    except:
        return "Error Coming!!!"

print(digitdivide(51)) 