"""
Basic Factorial Program using function and recursion
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
Basic Program to make right angle triangle using * of 5
"""
z = 5
#z = int(input("")) #Uncomment this to take input, and comment above line
for j in range(1,z+1):
    print("*"*j)
"""
Basic Program Equilateral triangle
"""
y = 5
y1 = 5
for k in range(1,y+1):
    print(" "*y1,end="")
    print("* "*k)
    y1 -= 1