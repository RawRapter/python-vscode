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
print("")
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
print("")
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
print("")
"""
6) Basic Program to check if number is palindrome or not
"""
num2 = 121
def palindrome(d):
    remainder = 0
    revnum = 0
    n = len(str(d))
    copynum2 = d
    while copynum2 != 0:
        remainder = copynum2%10
        revnum = revnum * 10 + remainder
        copynum2 //= 10
    if d == revnum:
        return "Given Numer {} is palindrome".format(d)
    else:
        return "Given Numer {} is not palindrome".format(d)
print(palindrome(num2))
print("")
"""
7) Basic Program to find fibonacci till specific place
"""
e = 8 #we want first 8 fibonaci number
def fibonacci(e):
    r,t,count1 = 0,1,0
    print(r,"",t,end=" ")
    while(count1<e):
        sum7 = r + t
        print(sum7,end=" ")
        r = t
        t = sum7
        count1 += 1
print(fibonacci(e))