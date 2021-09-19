"""
Check if a triangle of positive area is possible with the given angles

Given three angles. The task is to check if it is possible to have a triangle of positive area with these angles. If it is possible print “YES” else print “NO”.
Examples: 
 

Input : ang1 = 50, ang2 = 60, ang3 = 70 
Output : YES

Input : ang1 = 50, ang2 = 65, ang3 = 80
Output : NO
"""

def triangle(x: int,y: int,z: int):
    if( x != 0 and y != 0 and z != 0 and (x+y+z) == 180):
        if((x+y)>z and (y+z)>x and (x+z)>y):
            return "Yes"
        else:
            return "No"
    else:
        return "No"

a, b, c = 50, 60, 70
print(triangle(a,b,c))