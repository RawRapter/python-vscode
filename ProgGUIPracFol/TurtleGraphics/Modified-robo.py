"""
Creating Robot , all body parts are triangles of different sizes and colors.
"""

import turtle as t
import time as ti

#Creating function to make rectangle as per our size and color
def rectangle(hor,ver,col):
    t.pendown()
    t.pensize(1)
    t.color(col)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()

#Penup to go desired position for starting
t.penup()
t.speed('slow')
#Making background color Blue
t.bgcolor('Dodger blue')

#Creating left foot
t.goto(-100,-150)
rectangle(50,20,'blue')
#Creating Right Foot
t.goto(-30,-150)
rectangle(50,20,'blue')

#creating right leg
t.goto(-25,-50)
rectangle(15,100,'grey')
#creating lefft leg
t.goto(-55,-50)
rectangle(-15,100,'grey')

#Creatiing Body
t.goto(-90,100)
rectangle(100,150,'red')

#creating left hand above elbow part
t.goto(-150,70)
rectangle(60,15,'grey')
#creating left hand below elbow part
t.goto(-150,110)
rectangle(15,40,'grey')

#creating right hand above elbow part
t.goto(10,70)
rectangle(60,15,'grey')
#creating right hand below elbow part
t.goto(55,110)
rectangle(15,40,'grey')

#creating neck
t.goto(-50,120)
rectangle(15,20,'grey')

#creating face
t.goto(-85,170)
rectangle(80,50,'red')

#creating joint eyes
t.goto(-60,160)
rectangle(30,10,'white')

#creating both eye pupils this time different eye location
t.goto(-60,160)
rectangle(5,5,'black')
t.goto(-45,155)
rectangle(5,5,'black')

#Creating mouth little tilted
t.goto(-65,135)
t.right(5) #tilting turtle
rectangle(40,5,'black')

#Creating left palm
t.goto(-155,130)
rectangle(25,25,'green')
t.goto(-147,130)
rectangle(10,15,t.bgcolor())

#Creating Right Palm
t.goto(50,130)
rectangle(25,25,'green')
t.goto(58,130)
rectangle(10,15,t.bgcolor())

t.hideturtle()
ti.sleep(10)
t.hideturtle()