"""
1) Basic Factorial Program using function and recursion
"""
def factorial(x):
    f = 1
    if x < 0:
        return "Factorial of negative number doesn't exist"
    elif x == 0:
        return 1
    elif x == 1:
        return x
    else:
        return x*factorial(x-1)
print("Enter any number")
x = 5
#x = int(input("Number is: ")) #Uncomment this to take input, and comment above line
print("Factorial of",x,"is: ",factorial(x))

"""
2) Basic Program to make right angle triangle using * of 5
"""
z = 5
#z = int(input("")) #Uncomment this to take input, and comment above line
for j in range(1,z+1):
    print("*"*j)
"""
3) Basic Program Equilateral triangle
"""
y = 5
y1 = 5
for k in range(1,y+1):
    print(" "*y1,end="")
    print("* "*k)
    y1 -= 1

"""
4) Basic Program to count number of digit in an integer
"""
g = 100
#g = int(input("")) #Uncomment this to take input, and comment above line
def count(g):
    c = 0
    while g!=0 :
        g //= 10
        c +=1
    return c
print(count(g))

"""
5) Basic program to check if number is Armstrong
"""
import math
num1 = 371
def armstrong(num):
    n = 0
    result = 0
    copynum = num
    n = len(str(num))
    # while copynum != 0: #same work as above line
    #     copynum /= copynum
    #     n += 1
    # copynum = num
    #print("Value of N",n)
    while copynum != 0:
        rem = copynum%10
        result += pow(rem,n)
        copynum //= 10
    #print("Value of result ",result)
    if result == num:
        return "Number {} is armstrong".format(num)
    else:
        return "Number {} is not armstrong".format(num)

x = armstrong(num1)
print(x)