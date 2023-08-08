#This File contains Basic Programs
"""
1) Basic Factorial Program using function and recursion
"""
def factorial(x: int):
    """
    Function is calculating the factorial of the given integer using recursion method.
    Input: Integer
    Output: Integer
    """
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
2) Basic Program to make right angle triangle using * of 5.
"""
z = 5
#z = int(input("")) #Uncomment this to take input, and comment above line
for j in range(1,z+1):
    print("*"*j)

"""
3) Basic Program Equilateral triangle.
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
def count(g: int)->int:
    """
    function is calculating the number of digitd in the given number,
    by dividing the number by 10 with every iteration and increasing the count.
    Input: Integer
    Output: Integer
    """
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
#import math
num1 = 371
def armstrong(num: int)->str:
    """
    Function checks by getting the digits of the number and powering them to length of number,
    and adding together to compare if we are getting same number or not.
    Input: Integer
    Output: String (Sentence telling armstrong or not)
    """
    n = 0
    result = 0
    copynum = num
    n = len(str(num))
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
def palindrome(d: int)-> str:
    """
    Function is getting the digits of the number, left shifting it by multiplying
    it with 10 at each iteration and adding it the previous result.
    Input: Integer
    Output: String (Sentence telling if the number is palindrome or not)
    """
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
7) Basic Program to find fibonacci till specific place Method 1, Method 2 at 14
"""
e = 8 #we want first 8 fibonacci number
def fibonacci(e: int):
    """
    Function is having intitial two values , calculating next value by adding previous 2.
    Input: Integer
    Output: Integers
    """
    r,t,count1 = 0,1,0
    print(r,"",t,end=" ")
    while(count1<e):
        sum7 = r + t
        print(sum7,end=" ")
        r = t
        t = sum7
        count1 += 1
print(fibonacci(e))

"""
8) Basic Program to convert paragraph into dictionary, Word Key and word length Value
"""
lis = "I am anant arun interested in data analysis and devops"
dic = [{i : len(i)} for i in lis.split(" ")] #list comprehension is used
print(dic)
print()
a1,a2,a3 = 2,6,3
z = max(a1,a2,a3) #just checking max working or not
print(z)
print()

"""
9) Basic Program to calculate simple interest
"""
principle = float(input("Enter Principle Amount: "))
rate = float(input("Enter Rate: "))
time = int(input("Enter TIme: "))
def SimpleInterest(principle,rate,time):
    amount = principle * (1 + (rate * time)/100)
    return amount
amt = SimpleInterest(principle,rate,time)
print("Total Amount in SImple Interest is: ",amt)
print()

"""
10) Basic Program to calculate Compound interest
"""
principle1 = float(input("Enter Principle Amount: "))
rate1 = float(input("Enter Rate: "))
time1 = int(input("Enter TIme: "))
def CompoundInterest(principle1,rate1,time1):
    amount1 = principle1 * (1 + rate1/100) ** time1
    return amount1
amt1 = CompoundInterest(principle1,rate1,time1)
print("Total Amount in Compound Interest is ",amt1)
print()

"""
11) Basic Program to calculate Area of Circle
"""
import math
radius = 5
pie1 = math.pi
def circle(radius: int)->float:
    """
    Function is calculating the are of circle using basic formula pie*r*r,
    where r is the radius.
    Input: Integer
    Output: Float
    """
    area = pie1 * pow(radius,2)
    return area
area1 = circle(radius)
print("Area of the circle is {}".format(round(area1,2)))

"""
12) Basic Program to find all prime numbers in an Interval
"""
import math
print("Enter interval in which you want to have all the prime numbers")
start = int(input("Starting Number: "))
end = int(input("Ending Number: "))
for i in range(start,end + 1):
    if i > 1:
        for j in range(2,int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            print(i)
    else:
         print("Don't Give One or Negative Number")

"""
13) Basic Program to find the number is prime number or not
"""
num3 = int(input("Enter a number: "))
flag1 = False
for i in range(2,int(math.sqrt(num3))):
    if num3 % i == 0:
        flag1 = True
        break
if flag1 == True:
    print("Number is not a prime number")
else:
    print("Number is a Prime Number")

"""
14) Basic Program to get a nth fibonacci Number Method 2
"""
num4 = int(input("Enter Number at which you want fibonacci number"))
def fibonnaci2(num4: int):
    """
    Function is using recursion method and is giving end result only
    Input: Integer
    Output: Integer
    """
    if num4 < 0:
        print("Incorrect number please write positive number")
    elif num4 == 1:
        return 0
    elif num4 == 2:
        return 1
    else:
        return fibonnaci2(num4 -1) + fibonnaci2(num4 - 2)
print("Fibonacci Number at ",num4," is ",fibonnaci2(num4))

"""
15) Basic Program to check if given number is fibonacci
"""
num5 = int(input("Enter Number to check if given number is fibonacci"))
def fibonnaci3(d: int):
    def isperfectsquare(x: int):
        s = int(math.sqrt(x))
        return s*s == x
    def fibonaci(d):
        return isperfectsquare(d*d*5 + 4) or isperfectsquare(d*d*5 - 4)
    if fibonaci(d) == True:
        return "{} is a fibonacci number".format(d)
    else:
        return "{} is not a fibonacci number".format(d)
zk = fibonnaci3(num5)
print(zk)

"""
16) Basic Program to write ASCII value of a Character
"""
num6 = str(input("Enter Number you want to get ASCII value of "))
def getASCII(x):
    return ord(x)
zl = getASCII(num6)
print("ASCII value of {0} is {1}".format(num6,zl))

"""
17) Basic Program to find Sum of squares of first n natural numbers
"""
number = int(input())
def sqsum(x):
    sum = x * (x + 1) * (2*x + 1) / 6
    return sum
print(sqsum(number))

"""
18) Basic Program to find Sum of cube of first n natural numbers using Lambda
"""
number1 = int(input())
sqsum1 = lambda x : (x * (x + 1) / 2) ** 2
print(sqsum1(number1))